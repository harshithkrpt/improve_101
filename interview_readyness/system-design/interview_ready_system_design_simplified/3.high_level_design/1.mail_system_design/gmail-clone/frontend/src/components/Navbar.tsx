import { Link } from "react-router-dom";
import { ThemeToggle } from "./ThemeToggle";
import LanguageSwitcher from './LanguageSwitcher';
import { useTranslation } from 'react-i18next';

import { NavigationMenu, NavigationMenuList, NavigationMenuItem, NavigationMenuLink } from "@/components/ui/navigation-menu";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { useAuth } from "@/context/AuthContext";

export function Navbar() {
  const { user, logout } = useAuth();
  const { t } = useTranslation();

  return (
    <div className="w-full border-b px-6 py-4 flex items-center justify-between">
      <NavigationMenu>
        <NavigationMenuList className="gap-4">
          <NavigationMenuItem>
            <NavigationMenuLink asChild>
              <Link to="/" className="text-sm font-medium">{t('home')}</Link>
            </NavigationMenuLink>
          </NavigationMenuItem>
          {!user && (
            <>
              <NavigationMenuItem>
                <NavigationMenuLink asChild>
                  <Link to="/login" className="text-sm font-medium">{t('login')}</Link>
                </NavigationMenuLink>
              </NavigationMenuItem>
              <NavigationMenuItem>
                <NavigationMenuLink asChild>
                  <Link to="/register" className="text-sm font-medium">{t('register')}</Link>
                </NavigationMenuLink>
              </NavigationMenuItem>
            </>
          )}
        </NavigationMenuList>
      </NavigationMenu>

      <div className="flex items-center gap-4">
        <LanguageSwitcher />
        <ThemeToggle />
        {user && (
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Avatar className="cursor-pointer h-8 w-8">
                <AvatarFallback>{user[0].toUpperCase()}</AvatarFallback>
              </Avatar>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem onClick={logout}>{t('logout')}</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        )}
      </div>
    </div>
  );
}
