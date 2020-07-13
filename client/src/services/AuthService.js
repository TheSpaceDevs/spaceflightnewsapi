export default {
  login: user => {
    return fetch('/v2/users/login', {
      method: 'post',
      body: JSON.stringify(user),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(res => res.json())
      .then(data => data);
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
  isAuthenticated: () => {
    return fetch('/v2/users/sync')
      .then(res => {
        if (res.status !== 401) {
          return res.json().then(data => data);
        } else {
          return { isAuthenticated: false, user: { email: '', roles: [] } };
        }
      });
  },
};