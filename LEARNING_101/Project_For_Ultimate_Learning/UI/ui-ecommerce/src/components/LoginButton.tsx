// src/components/LoggedInButtons.tsx
"use client"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"

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
    <div className="flex gap-2">
      <Button onClick={handleLogin}>
        Login
      </Button>
      <Button onClick={handleRegister}>
        Register
      </Button>
    </div>
  )
}
