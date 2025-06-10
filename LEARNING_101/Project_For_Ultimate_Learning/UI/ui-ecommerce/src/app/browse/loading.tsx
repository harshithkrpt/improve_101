// components/EcommerceSkeleton.tsx
import { Card, CardContent } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

export default function EcommerceSkeleton() {
  const placeholders = Array.from({ length: 8 });

  return (
    <div className="space-y-8 animate-pulse p-6 bg-surface-light dark:bg-surface-dark">
      {/* Header */}
      <div className="flex items-center justify-between">
        <Skeleton className="h-8 w-32 rounded-md" /> {/* Logo */}
        <div className="flex space-x-4">
          <Skeleton className="h-8 w-24 rounded-full" />
          <Skeleton className="h-8 w-24 rounded-full" />
        </div>
      </div>

      {/* Hero / Banner */}
      <Skeleton className="h-48 w-full rounded-lg" />

      {/* Search bar */}
      <Skeleton className="h-10 w-full max-w-md rounded-full" />

      {/* Product grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {placeholders.map((_, idx) => (
          <Card
            key={idx}
            className="space-y-4 bg-card-light dark:bg-card-dark"
          >
            <Skeleton className="h-40 w-full rounded-lg" /> {/* Image */}

            <CardContent className="space-y-2">
              <Skeleton className="h-4 w-3/4 rounded-md" />  {/* Title */}
              <Skeleton className="h-4 w-1/2 rounded-md" />  {/* Subtitle */}

              <div className="flex items-center space-x-2">
                <Skeleton className="h-6 w-16 rounded-full" /> {/* Price */}
                <Skeleton className="h-8 w-24 rounded-md" />  {/* Button */}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}