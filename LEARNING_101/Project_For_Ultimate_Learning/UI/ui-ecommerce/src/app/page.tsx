import { cookies }   from 'next/headers'
import { redirect }  from 'next/navigation'
import { jwtVerify } from 'jose'

export default async function Home() {
  const cookieStore = await cookies()
  const token       = cookieStore.get('token')?.value

  // 1️⃣ No token → immediate redirect to /login
  if (!token) {
    redirect('/login')
  }

  const secret = new TextEncoder().encode(process.env.JWT_SECRET!)

  // 2️⃣ Try verifying token; if it fails, redirect to /login
  try {
    await jwtVerify(token, secret)
  } catch (err) {
    console.error('JWT verify failed:', err)
    redirect('/login')
  }

  // 3️⃣ If we get here, token is valid → send to /browse
  redirect('/browse')
}
