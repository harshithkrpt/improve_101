import { BrowserRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import { AuthProvider, useAuth } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeProvider';
import { Navbar } from './components/Navbar';

function Home() {
  const { user } = useAuth();
  return (
    <div className="p-6">
      <h1 className="mt-6 text-xl font-bold">Welcome, {user ?? 'Guest'}!</h1>
    </div>
  );
}

function ProtectedRoute() {
  const { user, token } = useAuth();
  return user && token ? <Outlet /> : <Navigate to="/login" replace />;
}

function PublicOnlyRoute() {
  const { user, token } = useAuth();
  return user && token ? <Navigate to="/" replace /> : <Outlet />;
}

export default function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <Router>
          <Navbar />
          <Routes>
            <Route element={<ProtectedRoute />}>
              <Route path="/" element={<Home />} />
            </Route>
            <Route element={<PublicOnlyRoute />}>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
            </Route>
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
}