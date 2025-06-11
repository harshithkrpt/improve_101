
// pages/admin.tsx
import React from "react";
import { AddProductIcon, DeleteProductIcon, UpdateProductIcon } from "@/components/icons/ProductIcons";
import { AdminOptionCard } from "@/components/AdminOptionCard";

export default function AdminPage() {
  const cards = [
    { title: "Add Product", Icon: AddProductIcon, href: "/browse/add-product" },
    { title: "Delete Product", Icon: DeleteProductIcon, href: "/browse/delete-product" },
    { title: "Update Product", Icon: UpdateProductIcon, href: "/browse/update-product" },
  ];


  return (
    <main className="min-h-screen bg-background-light dark:bg-background-dark p-8">
      <h1 className="text-3xl font-bold text-text-light dark:text-text-dark mb-8">
        Admin Dashboard
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {cards.map(({ title, Icon ,href}) => (
          <AdminOptionCard key={title} title={title} Icon={Icon} href={href}/>
        ))}
      </div>
    </main>
  );
}
