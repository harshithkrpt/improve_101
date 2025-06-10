import React from "react";
import { Card, CardContent, CardTitle } from "@/components/ui/card";

export interface AdminOptionCardProps {
  title: string;
  Icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
  onClick?: () => void;
}

export function AdminOptionCard({ title, Icon, onClick }: AdminOptionCardProps) {
  return (
    <Card
      as="button"
      onClick={onClick}
      className="bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark rounded-2xl shadow-lg hover:shadow-xl transition-shadow"
    >
      <CardContent className="flex flex-col items-center p-6">
        <Icon className="h-12 w-12 mb-4" />
        <CardTitle className="text-lg">{title}</CardTitle>
      </CardContent>
    </Card>
  );
}