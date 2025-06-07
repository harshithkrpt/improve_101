"use client"
import { useRouter } from "next/navigation"

export function LogoutButton() {
  const router = useRouter()
  
  const handleLogout = () => {
    document.cookie = "token=; path=/; max-age=0;"
    router.refresh()
    router.push("/login")
  }

  return (
    <button
      onClick={handleLogout}
      className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
    >
      Logout
    </button>
  )
}
