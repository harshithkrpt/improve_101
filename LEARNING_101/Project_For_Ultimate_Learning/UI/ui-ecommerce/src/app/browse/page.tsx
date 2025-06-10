
// pages/admin.tsx
import React from "react";
import { AddProductIcon, DeleteProductIcon, UpdateProductIcon } from "@/components/icons/ProductIcons";
import { AdminOptionCard } from "@/components/AdminOptionCard";

export default function AdminPage() {
  const cards = [
    { title: "Add Product", Icon: AddProductIcon },
    { title: "Delete Product", Icon: DeleteProductIcon },
    { title: "Update Product", Icon: UpdateProductIcon },
  ];

  return (
    <main className="min-h-screen bg-background-light dark:bg-background-dark p-8">
      <h1 className="text-3xl font-bold text-text-light dark:text-text-dark mb-8">
        Admin Dashboard
      </h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {cards.map(({ title, Icon }) => (
          <AdminOptionCard key={title} title={title} Icon={Icon} />
        ))}
      </div>
    </main>
  );
}
