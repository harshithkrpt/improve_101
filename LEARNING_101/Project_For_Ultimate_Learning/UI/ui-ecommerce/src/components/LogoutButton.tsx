// src/components/LogoutButton.tsx
"use client"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"

export function LogoutButton() {
  const router = useRouter()
  
  const handleLogout = () => {
    document.cookie = "token=; path=/; max-age=0;"
    router.refresh()
    router.push("/login")
  }

  return (
    <Button
      variant="destructive"
      onClick={handleLogout}
    >
      Logout
    </Button>
  )
}