import { createSlice, configureStore } from '@reduxjs/toolkit';

const userSlice = createSlice({
  name: 'user',
  initialState: {
    token: '',
    isAuthenticated: false,
    name: "",
    email: "",
    roles: "",
  },
  reducers: {
    authenticate: (state, update) => {
      state.token = update.payload.access_token;
      state.isAuthenticated = update.payload.isAuthenticated;
      state.name = update.payload.user.firstname
      state.email = update.payload.user.email
      state.roles = update.payload.user.roles
    },
  },
});

export const { authenticate } = userSlice.actions;

export const store = configureStore({ reducer: { user: userSlice.reducer } });