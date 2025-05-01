# 📊 Proyecto de Ventas - Fullstack App (Vue.js + Django + GraphQL)

Este proyecto contiene una aplicación completa de estadísticas de ventas, usando:

- **Backend:** Django + Graphene-Django + SQLite
- **Frontend:** Vue 3 + Chart.js + Apollo (GraphQL)
## 🌐 Funcionalidades

- Gráficos de ventas mensuales y por producto
- Estadísticas básicas como promedio, mediana y moda de ventas
- Consumo de API GraphQL desde el frontend

## 📁 Estructura del Proyecto

├── ventas_project # Backend Django 
    ├── requirements.txt # Dependencias del backend 
├── ventas-frontend # Frontend Vue 3 
    ├── frontend-deps.txt # Dependencias del frontend 
└── README.md

## ⚙️ Requisitos

- Python 3.10+
- Node.js 18+ y npm
- (opcional) Virtualenv para aislar el entorno Python

---

## 🚀 Instalación

### Backend (Django)

```bash
cd ventas_project
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver


### Frontend (Vue)
''bash
cd ventas-frontend
npm install (frontend-deps.txt)
npm run dev

## Endpoints
GraphQL Playground: http://localhost:8000/graphql/
Frontend App: http://localhost:5173/



