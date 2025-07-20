import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <div className="p-6 bg-blue-500 text-white text-xl rounded shadow">
  🔥 If you see a blue box, Tailwind is back!
</div>

  </React.StrictMode>
);
