// src/app/layout.tsx
import type { Metadata } from 'next';
import { ThemeProvider } from 'next-themes';
import './globals.css';

import { Header } from '@/components/Header';

export const metadata: Metadata = {
  title: 'Ecommerce App',
  description: 'description for adding description api',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-background text-foreground">
        <ThemeProvider attribute="class" defaultTheme="system">
          <Header/>
          <main className="p-4">
            {children}
          </main>
        </ThemeProvider>
      </body>
    </html>
  );
}
