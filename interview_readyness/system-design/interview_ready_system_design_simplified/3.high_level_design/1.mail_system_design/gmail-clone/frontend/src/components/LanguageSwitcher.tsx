import { useTranslation } from 'react-i18next';
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from '@/components/ui/dropdown-menu';
import { Globe } from 'lucide-react';

export default function LanguageSwitcher() {
  const { i18n } = useTranslation();
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button className="flex items-center gap-1 px-2 py-1 rounded bg-gray-200 hover:bg-gray-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-gray-100 border border-gray-300 dark:border-gray-700">
          <Globe className="w-4 h-4" />
          <span className="hidden sm:inline">
            {i18n.language === 'en' ? 'English' : i18n.language === 'es' ? 'Español' : 'తెలుగు'}
          </span>
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700">
        <DropdownMenuItem onClick={() => i18n.changeLanguage('en')} className="dark:text-gray-100">
          English {i18n.language === 'en' && '✓'}
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => i18n.changeLanguage('es')} className="dark:text-gray-100">
          Español {i18n.language === 'es' && '✓'}
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => i18n.changeLanguage('te')} className="dark:text-gray-100">
          తెలుగు {i18n.language === 'te' && '✓'}
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
} 