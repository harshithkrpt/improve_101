// src/app/browse/add-product/page.tsx
"use client";
import { authFetch } from "@/lib/authFetch";

import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select";
import { useForm } from "react-hook-form";

type Category = { id: number; name: string };

interface ProductForm {
  name: string;
  categoryId: number;
  price: number;
  stock: number;
  productImage: string;
}

export default function AddProductPage() {
  const router = useRouter();
  const [categories, setCategories] = useState<Category[]>([]);
  const form = useForm<ProductForm>({
    defaultValues: {
      name: "",
      categoryId: 0,
      price: 0,
      stock: 0,
      productImage: "",
    },
  });

  useEffect(() => {
    (async () => {
      const res = await authFetch("http://localhost:8081/category/get");
      const cats = await res.json();
      setCategories(cats);
    })();
  }, []);

  const onSubmit = async (values: ProductForm) => {
    // find the selected categoryName
    const cat = categories.find((c) => c.id === values.categoryId);
    const payload = {
      ...values,
      categoryName: cat ? cat.name : "",
    };

    const res = await authFetch("http://localhost:8081/product/add-product", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      router.push("/browse");
    } else {
      console.error("Create failed", await res.text());
    }
  };

  return (
    <div
      className="
        max-w-lg mx-auto mt-12 p-6
        bg-background-light dark:bg-background-dark
        border border-border-light dark:border-border-dark
        rounded-lg shadow
      "
    >
      <h2 className="text-2xl font-semibold mb-6 text-text-light dark:text-text-dark">
        Add New Product
      </h2>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          {/* Product Name */}
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Product Name</FormLabel>
                <FormControl>
                  <Input placeholder="e.g. Wireless Headphones" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Category Select */}
          <FormField
            control={form.control}
            name="categoryId"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Category</FormLabel>
                <FormControl>
                  <Select
                    onValueChange={(v) => field.onChange(Number(v))}
                    value={field.value.toString()}
                  >
                    <SelectTrigger>
                      <SelectValue placeholder="Select a category" />
                    </SelectTrigger>
                    <SelectContent>
                      {categories.map((cat) => (
                        <SelectItem key={cat.id} value={cat.id.toString()}>
                          {cat.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Price */}
          <FormField
            control={form.control}
            name="price"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Price (₹)</FormLabel>
                <FormControl>
                  <Input type="number" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Stock */}
          <FormField
            control={form.control}
            name="stock"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Stock Quantity</FormLabel>
                <FormControl>
                  <Input type="number" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Product Image URL */}
          <FormField
            control={form.control}
            name="productImage"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Image URL</FormLabel>
                <FormControl>
                  <Input
                    placeholder="https://example.com/image.png"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <Button type="submit" className="w-full">
            Add Product
          </Button>
        </form>
      </Form>
    </div>
  );
}
