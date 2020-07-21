import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router';
import { authenticate } from '../services/Store';
import AuthService from '../services/AuthService';


const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(true);
  const isAuthenticated = useSelector(state => state.user.isAuthenticated);
  const dispatch = useDispatch();
  const history = useHistory();

  useEffect(() => {
    checkLogin();
  }, []);

  const checkLogin = async () => {
    try {
      const user = await AuthService.sync();
      dispatch(authenticate(user.data));
    } catch (e) {
      if (e.response && e.response.status === 401) {
        setLoading(false);
      }
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const user = await AuthService.login(email, password);
      dispatch(authenticate(user.data));
    } catch (e) {
      alert(e);
    }
  };


  if (isAuthenticated) {
    history.push('/admin');
  }

  if (loading) {
    return null;
  }

  return (
    <div>
      <form onSubmit={(e) => handleLogin(e)}>
        <label>
          email
        </label>
        <input type="email" onChange={(e) => setEmail(e.target.value)}/>
        <label>
          password
        </label>
        <input type="password" onChange={(e) => setPassword(e.target.value)}/>
        <input type="submit"/>
      </form>
    </div>
  );
};

export default Login;
