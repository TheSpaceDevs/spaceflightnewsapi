import axios from 'axios';
import {logout} from './Store';

export default {
  setupInterceptors: (history, store) => {
    axios.interceptors.response.use(response => {
      return response;
    }, error => {

      if (error.response.status === 401) {
        store.dispatch(logout())
        history.push('/login');
      }

      return Promise.reject(error);
    });
  },
};
