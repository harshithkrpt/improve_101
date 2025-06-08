"use client";
import { useState, useEffect } from "react";
import { usePathname } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { LogoutButton } from "./LogoutButton";
import { LoggedInButtons } from "./LoginButton";
import { ThemeSwitch } from "./ThemeSwitch";

export function Header() {
  const [loggedIn, setLoggedIn] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    setLoggedIn(
      document.cookie.split("; ").some((c) => c.startsWith("token="))
    );
  }, [pathname]);

  return (
    <header className="sticky top-0 z-40 w-full bg-background text-foreground shadow-sm border-b border-border">
      <div className="container mx-auto flex items-center justify-between p-4">
        <Link href="/" className="flex items-center gap-2">
          <Image
            src="/ecommerce.png"
            priority
            width={32}
            height={32}
            alt="Ecommerce Logo"
          />
          <span className="text-xl font-semibold">Ecommerce App</span>
        </Link>
        <div className="flex items-center gap-2">
          <ThemeSwitch />
          {loggedIn ? <LogoutButton /> : <LoggedInButtons />}
        </div>
      </div>
    </header>)
}

