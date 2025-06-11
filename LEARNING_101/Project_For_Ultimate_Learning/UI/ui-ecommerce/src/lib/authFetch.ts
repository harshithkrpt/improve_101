// lib/authFetch.ts
export async function authFetch(
  input: RequestInfo,
  init: RequestInit = {}
): Promise<Response> {
  // grab your token from document.cookie
  const token = document.cookie
    .split("; ")
    .find((c) => c.startsWith("token="))
    ?.split("=")[1];

  // clone headers and inject Authorization
  const headers = new Headers(init.headers);
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  return fetch(input, {
    ...init,
    headers,
    // include cookies on cross-site calls if you ever need them:
    credentials: "include",
  });
}
