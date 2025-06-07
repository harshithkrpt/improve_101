"use client"
import { useRouter } from "next/navigation"

export function LoggedInButtons() {
const router = useRouter()
  const handleLogin = () => {
      router.refresh()
    router.push("/login")
  }

  const handleRegister = () => {
    router.push("/register")
  }

  return (
    <div className="flex gap-1">

   
    <button
      onClick={handleLogin}
      className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-red-600 hover:cursor-pointer"
    >
      Login
    </button>
        <button
      onClick={handleRegister}
      className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-red-600 hover:cursor-pointer"
    >
      Register
    </button>
     </div>
  )
}



