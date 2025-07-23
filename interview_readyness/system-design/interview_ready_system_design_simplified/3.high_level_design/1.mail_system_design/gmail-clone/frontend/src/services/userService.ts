import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001';

export const userApi = createApi({
  reducerPath: 'userApi',
  baseQuery: fetchBaseQuery({ baseUrl: BASE_URL }),
  endpoints: (builder) => ({
    loginUser: builder.mutation<any, { email: string; password: string }>({
      query: ({ email, password }) => ({
        url: '/api/auth/login',
        method: 'POST',
        body: { email, password },
      }),
    }),
    registerUser: builder.mutation<any, { email: string; password: string }>({
      query: ({ email, password }) => ({
        url: '/api/auth/signup',
        method: 'POST',
        body: { email, password },
      }),
    }),
  }),
});

export const { useLoginUserMutation, useRegisterUserMutation } = userApi; 