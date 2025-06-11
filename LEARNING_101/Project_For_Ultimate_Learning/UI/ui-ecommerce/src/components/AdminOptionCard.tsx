import React from "react";
import Link from "next/link";
import { Card, CardContent, CardTitle } from "@/components/ui/card";

export interface AdminOptionCardProps {
  title: string;
  Icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
  href: string;
}

export function AdminOptionCard({ title, Icon, href }: AdminOptionCardProps) {
  return (
    <Card
     
      className="bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark rounded-2xl shadow-lg hover:shadow-xl transition-shadow"
    >
      <Link  href={href}>
      <CardContent className="flex flex-col items-center p-6">
        <Icon className="h-12 w-12 mb-4" />
        <CardTitle className="text-lg">{title}</CardTitle>
      </CardContent>
      </Link>
    </Card>
  );
}