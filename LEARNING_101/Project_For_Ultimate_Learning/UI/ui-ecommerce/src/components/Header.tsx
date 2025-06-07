// src/components/Header.tsx
"use client"
import { useState, useEffect } from "react"
import { LogoutButton } from "./LogoutButton"
import { LoggedInButtons }  from "./LoginButton"
import { usePathname } from "next/navigation"
import Image from "next/image"
export function Header() {
  const [loggedIn, setLoggedIn] = useState(false)
  const pathname = usePathname()
  
  useEffect(() => {
    setLoggedIn(document.cookie.split("; ").some(c => c.startsWith("token=")))
  }, [pathname])

  return (
    <header className="p-4 bg-gray-100 flex justify-between items-center">
      <h1 className="text-xl font-bold">
        <Image src={"/ecommerce.png"} priority width={48} height={48}  alt={"ecommerce.png"}/>
      </h1>
      {loggedIn ? <LogoutButton/> : <LoggedInButtons/>}
    </header>
  )
}
