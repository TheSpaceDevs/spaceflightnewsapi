import { createSlice, configureStore } from '@reduxjs/toolkit';

const userSlice = createSlice({
  name: 'user',
  initialState: {
    isAuthenticated: false,
    name: "",
    email: "",
    roles: [],
  },
  reducers: {
    authenticate: (state, update) => {
      state.isAuthenticated = update.payload.isAuthenticated;
      state.name = update.payload.user.firstname
      state.email = update.payload.user.email
      state.roles = update.payload.user.roles
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.name = ""
      state.email = ""
      state.roles = []
    },
  },
});

export const { authenticate, logout } = userSlice.actions;

export const store = configureStore({ reducer: { user: userSlice.reducer } });
