import { createSlice, configureStore } from '@reduxjs/toolkit';

const initialState = {
  isAuthenticated: false,
  name: "",
  email: "",
  roles: [],
}
const userSlice = createSlice({
  name: 'user',
  initialState: {
    isAuthenticated: initialState.isAuthenticated,
    name: initialState.name,
    email: initialState.email,
    roles: initialState.roles,
  },
  reducers: {
    authenticate: (state, update) => {
      state.isAuthenticated = update.payload.isAuthenticated;
      state.name = update.payload.user.firstname
      state.email = update.payload.user.email
      state.roles = update.payload.user.roles
    },
    logout: (state) => {
      state.isAuthenticated = initialState.isAuthenticated;
      state.name = initialState.name
      state.email = initialState.email
      state.roles = initialState.email
    },
  },
});

export const { authenticate, logout } = userSlice.actions;

export const store = configureStore({ reducer: { user: userSlice.reducer } });
