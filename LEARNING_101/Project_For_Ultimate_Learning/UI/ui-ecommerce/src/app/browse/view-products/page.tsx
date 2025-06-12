"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { authFetch } from "@/lib/authFetch";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Edit, Trash2 } from "lucide-react";
import { ConfirmationModal } from "@/components/ConfirmationModal";

interface Category { id: number; name: string; }
interface Product {
  id: number;
  name: string;
  price: number;
  stock: number;
  isActive: boolean;
  productImage: string;
  categories: Category;
}
interface PageResponse { content: Product[]; last: boolean; }

export default function ViewProducts() {
  const router = useRouter();
  const [products, setProducts] = useState<Product[]>([]);
  const [page, setPage] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  const loaderRef = useRef<HTMLDivElement>(null);
  const observer = useRef<IntersectionObserver>(null);
  const PAGE_SIZE = 20;
  const didInitialFetch = useRef(false);

  const fetchPage = useCallback(async (pageNum: number) => {
    setIsLoading(true);
    try {
      const res = await authFetch(
        `http://localhost:8081/product/get-products?page=${pageNum}&size=${PAGE_SIZE}`
      );
      const data: PageResponse = await res.json();
      setProducts((prev) => [...prev, ...data.content]);
      setHasMore(!data.last);
    } catch (err) {
      console.error("Fetch error:", err);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (!didInitialFetch.current) {
      fetchPage(0);
      didInitialFetch.current = true;
    }
  }, [fetchPage]);

  useEffect(() => {
    if (page > 0) fetchPage(page);
  }, [page, fetchPage]);

  useEffect(() => {
    observer.current?.disconnect();
    observer.current = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && hasMore && !isLoading) {
          setPage((p) => p + 1);
        }
      },
      { rootMargin: "200px" }
    );
    if (loaderRef.current) observer.current.observe(loaderRef.current);
    return () => observer.current?.disconnect();
  }, [hasMore, isLoading]);

  const handleDelete = async (id: number) => {
    try {
      await authFetch(`http://localhost:8081/product/delete-product/${id}`, {
        method: "PUT",
      });
      setProducts((prev) => prev.filter((p) => p.id !== id));
    } catch (err) {
      console.error("Delete failed:", err);
    }
  };

  const handleUpdateNav = (id: number) => {
    router.push(`/update/${id}`);
  };

  return (
    <div className="p-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      {products.map((product) => (
        <div key={product.id} className="relative group">
          {/* ─── Hover Actions ───────────────────────────── */}
          <div className="absolute top-2 right-2 flex space-x-1 opacity-0 group-hover:opacity-100 transition-opacity">
            {/* Edit */}
            <Button
              variant="ghost"
              size="icon"
              onClick={() => handleUpdateNav(product.id)}
            >
              <Edit className="h-4 w-4" />
            </Button>

            {/* Delete wrapped in your ConfirmationModal */}
            <ConfirmationModal
              title="Delete product?"
              description={`Are you sure you want to delete "${product.name}"?`}
              confirmText="Delete"
              cancelText="Cancel"
              onConfirm={() => handleDelete(product.id)}
            >
              <Button variant="ghost" size="icon">
                <Trash2 className="h-4 w-4 text-red-500" />
              </Button>
            </ConfirmationModal>
          </div>

          {/* ─── Product Card ────────────────────────────── */}
          <Card className="flex flex-col overflow-hidden">
            <CardHeader className="p-0">
              <div className="w-full h-48 relative">
                <Image
                  src={product.productImage}
                  alt={product.name}
                  fill
                  className="object-cover"
                />
              </div>
            </CardHeader>
            <CardContent className="flex-1">
              <CardTitle>{product.name}</CardTitle>
              <CardDescription>{product.categories.name}</CardDescription>
            </CardContent>
            <CardFooter className="justify-between">
              <span className="font-semibold">
                ₹{product.price.toLocaleString()}
              </span>
              <span className="text-sm text-muted-foreground">
                {product.stock} in stock
              </span>
            </CardFooter>
          </Card>
        </div>
      ))}

      <div ref={loaderRef} className="h-2 col-span-full" />
      {isLoading && <p className="col-span-full text-center">Loading more…</p>}
      {!hasMore && (
        <p className="col-span-full text-center text-muted-foreground">
          No more products
        </p>
      )}
    </div>
  );
}
