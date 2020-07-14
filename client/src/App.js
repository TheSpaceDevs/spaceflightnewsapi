import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Provider } from 'react-redux';

import { News, Blogs, Reports, About, Home, Admin } from './screens';
import { HeaderComponent } from './components';
import {store} from './services/Store';

export default function App() {
  return (
    <Provider store={store}>
      <Router>
        <HeaderComponent/>
        <Switch>
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
