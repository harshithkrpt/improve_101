import React from "react";
import Link from "next/link";
import { Card, CardContent, CardTitle } from "@/components/ui/card";
import Image from "next/image";


export type AdminOptionCardBase = {
  title: string;
  href: string;
};

export type AdminOptionCardProps =
  | (AdminOptionCardBase & {
      isImage: true;
      imagePath: string;
      Icon?: never;
    })
  | (AdminOptionCardBase & {
      isImage: false;
      Icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
      imagePath?: never;
    });


export function AdminOptionCard({
  title,
  Icon,
  href,
  isImage = false,
  imagePath = "",
}: AdminOptionCardProps) {
  return (
    <Card className="bg-card-light dark:bg-card-dark text-text-light dark:text-text-dark rounded-2xl shadow-lg hover:shadow-xl transition-shadow">
      <Link href={href}>
        <CardContent className="flex flex-col items-center p-6">
          {isImage ? (
            <div className="my-5">
            <Image src={imagePath} alt="" 
                 width={150} height={150}/>
              </div>
          ) : (
            <Icon className="h-12 w-12 mb-4" />
          )}
          <CardTitle className="text-lg">{title}</CardTitle>
        </CardContent>
      </Link>
    </Card>
  );
}
