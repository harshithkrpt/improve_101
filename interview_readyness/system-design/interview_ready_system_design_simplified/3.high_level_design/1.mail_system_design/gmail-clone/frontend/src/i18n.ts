import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      welcome: 'Welcome',
      login: 'Login',
      register: 'Register',
      email: 'Email',
      password: 'Password',
      home: 'Home',
      logout: 'Logout',
      guest: 'Guest',
      switch_to_mode: 'Switch to {{mode}} Mode',
      dark: 'Dark',
      light: 'Light',
      login_success: 'Login successful!',
      login_failed: 'Login failed.',
      register_success: 'Registration successful!',
      register_failed: 'Registration failed.',
      confirm_password: 'Confirm Password',
      'Passwords do not match': 'Passwords do not match',
      'Confirm Password is required': 'Confirm Password is required',
    },
  },
  es: {
    translation: {
      welcome: 'Bienvenido',
      login: 'Iniciar sesión',
      register: 'Registrarse',
      email: 'Correo electrónico',
      password: 'Contraseña',
      home: 'Inicio',
      logout: 'Cerrar sesión',
      guest: 'Invitado',
      switch_to_mode: 'Cambiar a modo {{mode}}',
      dark: 'Oscuro',
      light: 'Claro',
      login_success: '¡Inicio de sesión exitoso!',
      login_failed: 'Error de inicio de sesión.',
      register_success: '¡Registro exitoso!',
      register_failed: 'Error de registro.',
      confirm_password: 'Confirmar contraseña',
      'Passwords do not match': 'Las contraseñas no coinciden',
      'Confirm Password is required': 'Se requiere confirmar la contraseña',
    },
  },
  te: {
    translation: {
      welcome: 'స్వాగతం',
      login: 'లాగిన్',
      register: 'నమోదు',
      email: 'ఇమెయిల్',
      password: 'పాస్వర్డ్',
      home: 'హోమ్',
      logout: 'లాగ్ అవుట్',
      guest: 'అతిథి',
      switch_to_mode: '{{mode}} మోడ్‌కు మార్చండి',
      dark: 'డార్క్',
      light: 'లైట్',
      login_success: 'లాగిన్ విజయవంతం!',
      login_failed: 'లాగిన్ విఫలమైంది.',
      register_success: 'నమోదు విజయవంతం!',
      register_failed: 'నమోదు విఫలమైంది.',
      confirm_password: 'పాస్వర్డ్‌ను నిర్ధారించండి',
      'Passwords do not match': 'పాస్వర్డ్లు సరిపోలడం లేదు',
      'Confirm Password is required': 'పాస్వర్డ్ నిర్ధారణ అవసరం',
    },
  },
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n; 