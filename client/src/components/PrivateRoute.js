import React from 'react';
import { Route, Redirect } from 'react-router';
import { useSelector } from 'react-redux';

const PrivateRoute = ({ children, ...rest }) => {
  const isAuthenticated = useSelector(state => state.user.isAuthenticated);

  return (
    <Route
      {...rest}
      render={({ location }) =>
        isAuthenticated ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: '/login',
            }}
          />
        )
      }
    />
  );
};

export default PrivateRoute;
