// src/apollo.js
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client/core'

const httpLink = createHttpLink({
  uri: 'http://localhost:8000/graphql/', // Ajusta si tu endpoint es otro
})

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})

export default apolloClient
