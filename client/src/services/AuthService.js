import axios from 'axios';

export default {
  login: (email, password) => {
    return axios.post('/v2/users/login', {
      username: email,
      password: password,
    });
  },
  register: user => {
    return fetch('/v2/users/register', {
      method: 'post',
      body: JSON.stringify(user),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(res => res.json())
      .then(data => data);
  },
  logout: () => {
    return fetch('/v2/users/logout')
      .then(res => res.json())
      .then(data => data);
  },
  ping: () => {
    return axios.get('/v2/users/ping');
  },
};