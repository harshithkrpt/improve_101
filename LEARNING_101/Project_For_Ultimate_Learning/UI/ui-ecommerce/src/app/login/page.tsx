// src/app/login/page.tsx (or wherever your LoginPage lives)
"use client";

import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function LoginPage() {
  const router = useRouter();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      const res = await fetch("http://localhost:8081/auth/user/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.message || "Login failed");
      }

      const { accessToken }: { accessToken: string } = data;
      document.cookie = `token=${accessToken}; path=/;`;
      router.push("/browse");
      router.refresh();
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-16 p-6 bg-background border border-border rounded-lg shadow-sm">
      <h1 className="text-2xl font-semibold mb-6 text-foreground">Login</h1>

      {error && (
        <p className="mb-4 text-sm font-medium text-destructive">
          {error}
        </p>
      )}

      <form onSubmit={handleSubmit} className="space-y-5">
        <div className="space-y-2">
          <Label htmlFor="username">Username</Label>
          <Input
            id="username"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter username"
          />
        </div>

        <div className="space-y-2">
          <Label htmlFor="password">Password</Label>
          <Input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter password"
          />
        </div>

        <Button type="submit" className="w-full">
          Log In
        </Button>
      </form>

      <p className="mt-6 text-center text-sm text-foreground">
        Don’t have an account?{" "}
        <Link href="/register" passHref>
          <Button variant="link">Register</Button>
        </Link>
      </p>
    </div>
  );
}
