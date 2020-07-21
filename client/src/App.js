import React from 'react';
import { Router, Switch, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { createBrowserHistory } from 'history';

import { News, Blogs, Reports, About, Home, Admin, DataEntry, Login } from './screens';
import { HeaderComponent, PrivateRoute } from './components';
import { store } from './services/Store';
import httpClient from './services/AxiosService'

export default function App() {
  const history = createBrowserHistory();
  httpClient.setupInterceptors(history, store)

  return (
    <Provider store={store}>
      <Router history={history}>
        <HeaderComponent/>
        <Switch>
          <Route path="/admin/article/new">
            <DataEntry/>
          </Route>
          <PrivateRoute path="/admin">
            <Admin/>
          </PrivateRoute>
          <Route path="/login">
            <Login/>
          </Route>
          <Route path="/about">
            <About/>
          </Route>
          <Route path="/reports">
            <Reports/>
          </Route>
          <Route path="/blogs">
            <Blogs/>
          </Route>
          <Route path="/news">
            <News/>
          </Route>
          <Route path="/">
            <Home/>
          </Route>
        </Switch>
      </Router>
    </Provider>
  );
}
