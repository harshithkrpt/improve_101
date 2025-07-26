import { Button } from "@/components/ui/button";
import { useTheme } from "@/context/ThemeProvider";
import { useTranslation } from 'react-i18next';

export function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();
  const { t } = useTranslation();
  return (
    <Button variant="outline" onClick={toggleTheme}>
      {t('switch_to_mode', { mode: theme === 'light' ? t('dark') : t('light') })}
    </Button>
  );
}