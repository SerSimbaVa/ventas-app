import graphene
from graphene_django import DjangoObjectType
from .models import Sale, Product
from django.db.models import Avg
from statistics import median, mode
from django.db.models import Sum
from datetime import datetime
from django.db.models.functions import TruncMonth


class SaleType(graphene.ObjectType):
    id = graphene.Int()
    producto = graphene.String()
    cantidad = graphene.Int()
    fecha = graphene.Date()
    precio_unitario = graphene.Float()
    total = graphene.Float()

    def resolve_producto(self, info):
        return self.product.name

    def resolve_cantidad(self, info):
        return self.quantity

    def resolve_fecha(self, info):
        return self.date

    def resolve_precio_unitario(self, info):
        return float(self.product.price)

    def resolve_total(self, info):
        return float(self.quantity * self.product.price)


class SalesByProductType(graphene.ObjectType):
    producto = graphene.String()
    total_cantidad = graphene.Int()


class StatisticsType(graphene.ObjectType):
    total = graphene.Int()
    mean = graphene.Float()
    median = graphene.Float()
    mode = graphene.Int()


class SalesByMonthType(graphene.ObjectType):
    month = graphene.String()
    total_quantity = graphene.Int()


class Query(graphene.ObjectType):
    sales = graphene.List(SaleType)
    sales_statistics = graphene.Field(StatisticsType)
    sales_by_product = graphene.List(SalesByProductType)
    sales_by_month = graphene.List(SalesByMonthType)

    def resolve_sales(root, info):
        return Sale.objects.select_related('product').all()

    def resolve_sales_statistics(root, info):
        sales = Sale.objects.select_related('product').all()
        quantities = [sale.quantity for sale in sales]

        if not quantities:
            return StatisticsType(total=0, mean=0, median=0, mode=0)

        total = sum(quantities)
        mean = sum(quantities) / len(quantities)
        med = median(quantities)
        try:
            moda = mode(quantities)
        except:
            moda = quantities[0]  # fallback si no hay moda única

        return StatisticsType(
            total=total,
            mean=round(mean, 2),
            median=med,
            mode=moda
        )

    def resolve_sales_by_product(root, info):
        sales_data = (
            Sale.objects.values('product__name')
            .annotate(total_cantidad=Sum('quantity'))
            .order_by('-total_cantidad')
        )

        return [
            SalesByProductType(
                producto=entry['product__name'],
                total_cantidad=entry['total_cantidad']
            )
            for entry in sales_data
        ]

    def resolve_sales_by_month(root, info):
        sales = (
            Sale.objects.annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('month')
        )

        return [
            SalesByMonthType(
                month=entry['month'].strftime('%Y-%m'),
                total_quantity=entry['total_quantity']
            )
            for entry in sales
        ]


schema = graphene.Schema(query=Query)
