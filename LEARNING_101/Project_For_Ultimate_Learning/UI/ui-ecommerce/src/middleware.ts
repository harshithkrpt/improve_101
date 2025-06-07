import { NextResponse, type NextRequest } from "next/server";
import { jwtVerify }  from "jose";
import { decodeProtectedHeader } from 'jose'

const secret = new TextEncoder().encode(process.env.JWT_SECRET!);


export const config = {
  // only run on /browse and leave static files, /login, /register alone
  matcher: ["/browse/:path*", "/login", "/register"],
};

export async function middleware(req: NextRequest) {
  const token = req.cookies.get("token")?.value;
 
  // Protect /browse/*
  if (req.nextUrl.pathname.startsWith("/browse")) {
    if (!token) {
      return NextResponse.redirect(new URL("/login", req.url));
    }
    try {
      console.log("🔐 JWT alg:", decodeProtectedHeader(token).alg)
      await jwtVerify(token, secret)
    } catch(err) {
      console.error({err});
      return NextResponse.redirect(new URL("/login", req.url));
    }
  }

  if (
    (req.nextUrl.pathname === "/login" ||
     req.nextUrl.pathname === "/register") &&
    token
  ) {
    try {
      await jwtVerify(token, secret);
      return NextResponse.redirect(new URL("/browse", req.url));
    } catch(err) {
      console.log(err);
    }
  }

  return NextResponse.next();
}