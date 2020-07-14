import React, {useState, useEffect} from 'react';
import {useSelector, useDispatch} from 'react-redux';
import {authenticate} from '../services/Store';
import AuthService from '../services/AuthService';

const Admin = () => {
  const isAuthenticated = useSelector(state => state.user.isAuthenticated)
  const dispatch = useDispatch();
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  useEffect(() => {
    checkAuth()
  }, [])

  const checkAuth = async () => {
    try {
      const user = await AuthService.sync()
      dispatch(authenticate(user.data))
    } catch (e) {
    }
  }

  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      const user = await AuthService.login(email, password)
      dispatch(authenticate(user.data))
    } catch (e) {
    }
  }

  if (!isAuthenticated) {
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
  }

  return (
    <div>
      Ingelogd!
    </div>
  )
};

export default Admin;