import jwt from "jsonwebtoken"


export const validateToken = (token: string) => {
    const JWT_SECRET = process.env.JWT_SECRET;
    console.log(JWT_SECRET);
    try {
        return jwt.verify(token, JWT_SECRET);
    }
    catch(err) {
        return false;
    }
}

export function requireAuth(handler) {
  return async (context) => {
    const token = context.req.cookies.token || "";
    if (!token) {
      return {
        redirect: { destination: "/login", permanent: false },
      };
    }
    const payload = validateToken(token);
    if (!payload) {
      return {
    redirect: { destination: "/login", permanent: false },
      };
    }
    // Attach user info to context
    context.user = { userId: payload.userId, username: payload.username };
    return handler(context, context.user);
  };
}