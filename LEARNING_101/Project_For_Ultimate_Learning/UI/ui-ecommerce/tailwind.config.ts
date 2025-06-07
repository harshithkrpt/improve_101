import { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class", // or 'media' if you prefer OS-level dark mode
  theme: {
    extend: {
      colors: {
        // Primary brand blue
        primary: {
          light: "#93C5FD", // 100
          DEFAULT: "#3B82F6", // 500
          dark: "#1E40AF", // 800
        },
        // A complementary accent
        accent: {
          light: "#60A5FA",
          DEFAULT: "#2563EB",
          dark: "#1E3A8A",
        },
        // Background layers
        bg: {
          light: "#F8FAFC", // page background (light)
          dark: "#111827", // page background (dark)
        },
        surface: {
          light: "#FFFFFF", // cards, panels (light)
          dark: "#1F2937", // cards, panels (dark)
        },
        // Text colors
        text: {
          light: "#1F2937", // headings/text (light)
          dark: "#F9FAFB", // headings/text (dark)
        },
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ["dark"],
      textColor: ["dark"],
      borderColor: ["dark"],
    },
  },
  plugins: [],
};

export default config;
