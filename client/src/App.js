import React from 'react';
import { Router, Switch, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { createBrowserHistory } from 'history';

import { News, Blogs, Reports, About, Home, Admin, DataEntry } from './screens';
import { HeaderComponent } from './components';
import {store} from './services/Store';

export default function App() {
  const history = createBrowserHistory()

  return (
    <Provider store={store}>
      <Router history={history}>
        <HeaderComponent/>
        <Switch>
          <Route path="/admin/article/new">
            <DataEntry/>
          </Route>
          <Route path="/admin">
            <Admin/>
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
