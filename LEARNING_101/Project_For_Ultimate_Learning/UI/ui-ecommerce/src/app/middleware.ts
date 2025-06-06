// middleware.ts
import { NextResponse, type NextRequest } from "next/server";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET!;

export function middleware(req: NextRequest) {
  const url = req.nextUrl.clone();
  const token = req.cookies.get("token")?.value;

  // 1️⃣ If the user is trying to access **any** path EXCEPT /login or /register,
  //    enforce that a valid token must exist.
  if (
    url.pathname.startsWith("/") &&
    !url.pathname.includes("/login") &&
    !url.pathname.includes("/register")
  ) {
    if (!token) {
      // No token → redirect to /login
      url.pathname = "/login";
      return NextResponse.redirect(url);
    }
    try {
      jwt.verify(token, JWT_SECRET);
      // valid → allow
    } catch {
      // invalid or expired → redirect to /login
      url.pathname = "/login";
      return NextResponse.redirect(url);
    }
  }

  // 2️⃣ If the user hits /login or /register but already has a valid token,
  //    send them to /home instead.
  if (url.pathname === "/login" || url.pathname === "/register") {
    if (token) {
      try {
        jwt.verify(token, JWT_SECRET);
        url.pathname = "/home";
        return NextResponse.redirect(url);
      } catch {
        // invalid token → let them stay on /login or /register
      }
    }
  }

  // 3️⃣ Otherwise, just continue
  return NextResponse.next();
}

export const config = {
  // Only run this middleware on “every path” — we’ll do the “except login/register” logic above.
  matcher: ["/:path*"],
};
