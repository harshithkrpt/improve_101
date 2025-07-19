import { Link } from 'react-router-dom';
import { ThemeToggle } from './ThemeToggle';
import { Button } from "@/components/ui/button";
import { useAuth } from '@/context/AuthContext';

export function Navbar() {
  const { user, logout } = useAuth();

  return (
    <div className="w-full border-b py-4 px-6 flex items-center justify-between">
      <div className="flex gap-4 items-center">
        <Button variant="ghost" asChild>
          <Link to="/">Home</Link>
        </Button>
        <Button variant="ghost" asChild>
          <Link to="/login">Login</Link>
        </Button>
        <Button variant="ghost" asChild>
          <Link to="/register">Register</Link>
        </Button>
      </div>
      <div className="flex items-center gap-4">
        <ThemeToggle />
        {user && (
          <Button variant="outline" onClick={logout}>
            Logout
          </Button>
        )}
      </div>
    </div>
  );
}