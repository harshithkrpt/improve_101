/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        'bg-light': '#ffffff',
        'bg-dark': '#000000',
        'text-light': '#1f2937',
        'text-dark': '#f9fafb',
        'primary-light': '#3b82f6',
        'primary-dark': '#ef4444',
      },
      animation: {
        accordionDown: 'accordion-down 0.2s ease-out',
        accordionUp: 'accordion-up 0.2s ease-out',
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
};
