'use client';

import { useTheme } from 'next-themes';
import { Button } from '@/components/ui/button';

export function ThemeSwitch() {
  const { theme, setTheme } = useTheme();

  return (
    <Button
      variant="ghost"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      title="Toggle theme"
      className="ml-auto"
    >
      {theme === 'dark' ? '🌞 Light' : '🌙 Dark'}
    </Button>
  );
}
