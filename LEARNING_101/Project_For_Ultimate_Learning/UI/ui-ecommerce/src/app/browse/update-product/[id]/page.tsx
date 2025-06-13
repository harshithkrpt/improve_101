// app/update/[id]/page.tsx
"use client";

import { useEffect } from "react";
import { useRouter, useParams } from "next/navigation";
import { useForm } from "react-hook-form";
import { authFetch } from "@/lib/authFetch";

import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { Button } from "@/components/ui/button";

interface FormValues {
  name: string;
  price: number;
  stock: number;
  productImage: string;
  isActive: boolean;
}

export default function UpdateProductPage() {
  const { id } = useParams();                 
  const router = useRouter();
  const {
    register,
    handleSubmit,
    control,
    reset,
    formState: { isSubmitting },
  } = useForm<FormValues>();

  useEffect(() => {
    async function load() {
      try {
        const res = await authFetch(
          `http://localhost:8081/product/get-product/${id}`
        );
        const product = await res.json();
        reset({
          name: product.name,
          price: product.price,
          stock: product.stock,
          productImage: product.productImage,
          isActive: product.isActive,
        });
      } catch (e) {
        console.error("Failed to load product", e);
      }
    }
    load();
  }, [id, reset]);


  const onSubmit = async (data: FormValues) => {
    try {
      await authFetch(
        `http://localhost:8081/product/update/${id}`,
        {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        }
      );
      router.push("/browse/view-products");
    } catch (e) {
      console.error("Update failed", e);
    }
  };

  return (
    <div className="max-w-lg mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-bold">Edit Product #{id}</h1>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
        {/* Name */}
        <div>
          <Label htmlFor="name">Name</Label>
          <Input
            id="name"
            placeholder="Product name"
            {...register("name", { required: true })}
          />
        </div>

        {/* Price */}
        <div>
          <Label htmlFor="price">Price (₹)</Label>
          <Input
            id="price"
            type="number"
            step="0.01"
            {...register("price", { valueAsNumber: true, min: 0 })}
          />
        </div>


        <div>
          <Label htmlFor="stock">Stock</Label>
          <Input
            id="stock"
            type="number"
            {...register("stock", { valueAsNumber: true, min: 0 })}
          />
        </div>


        <div className="flex justify-end space-x-2">
          <Button
            variant="outline"
            onClick={() => router.back()}
            disabled={isSubmitting}
          >
            Cancel
          </Button>
          <Button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Saving…" : "Save Changes"}
          </Button>
        </div>
      </form>
    </div>
  );
}
