// src/app/layout.tsx
import type { Metadata } from "next";
import "./globals.css";

import { Header } from "@/components/Header";

export const metadata: Metadata = {
  title: "Ecommerce App",
  description: "description for adding description api",
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (
    <html lang="en">
      <body>
      <Header />
        {children}
      </body>
    </html>
  );
}
