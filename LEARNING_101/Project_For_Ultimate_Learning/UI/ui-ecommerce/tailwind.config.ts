import type { Config } from "tailwindcss";

const config: Config = {
  // Enable class-based dark mode
  darkMode: "class",
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
    // Add other paths as needed
  ],
  theme: {
    extend: {
      colors: {
        // Primary brand color
        primary: {
          light: "#2563EB", // blue-600
          DEFAULT: "#1D4ED8", // blue-700
          dark: "#1E40AF",   // blue-800
        },
        // Secondary accent color
        secondary: {
          light: "#EC4899", // pink-500
          DEFAULT: "#DB2777", // pink-600
          dark: "#9D174D",   // pink-700
        },
        // Neutral surfaces
        background: {
          light: "#FFFFFF", // white
          dark: "#111827", // gray-900
        },
        surface: {
          light: "#F9FAFB", // gray-50
          dark: "#1F2937", // gray-800
        },
        // Card backgrounds if needed
        card: {
          light: "#FFFFFF", // white
          dark: "#1E293B", // slate-800
        },
        // Text colors
        text: {
          light: "#111827", // gray-900
          dark: "#F9FAFB", // gray-50
        },
        // Border colors
        border: {
          light: "#E5E7EB", // gray-200
          dark: "#374151", // gray-700
        },
        // Highlight / accent tones
        accent: {
          light: "#F59E0B", // amber-500
          DEFAULT: "#D97706", // amber-600
          dark: "#B45309",   // amber-700
        },
      },
    },
  },
  plugins: [],
};

export default config;
