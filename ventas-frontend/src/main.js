import { createApp, h } from 'vue';
import App from './App.vue';
import router from './router';
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client/core';
import { DefaultApolloClient } from '@vue/apollo-composable';
import './assets/main.css'



const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/',
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
});

const app = createApp(App);

// Proveer Apollo Client para toda la aplicación
app.provide(DefaultApolloClient, apolloClient);

// Usar Vue Router
app.use(router);

// Montar la aplicación
app.mount('#app');


