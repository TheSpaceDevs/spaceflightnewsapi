import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import {News, Apps, Blogs, Reports, About, Home} from "./screens";
import { HeaderComponent } from "./components";

export default function App() {
  return (
    <Router>
      <HeaderComponent />
      <Switch>
        <Route path="/about">
          <About />
        </Route>
        <Route path="/reports">
          <Reports />
        </Route>
        <Route path="/blogs">
          <Blogs />
        </Route>
        <Route path="/apps">
          <Apps />
        </Route>
        <Route path="/news">
          <News />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}
