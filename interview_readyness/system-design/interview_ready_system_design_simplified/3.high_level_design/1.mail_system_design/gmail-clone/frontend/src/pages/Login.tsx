import { useState } from 'react';
import { loginUser } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Button } from "@/components/ui/button"

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await loginUser(email, password);
      login(data.email); // assuming email comes back
      alert('Login successful!');
    } catch {
      alert('Login failed.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-16 space-y-4">
      <input className="w-full p-2 border" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input className="w-full p-2 border" type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <Button type="submit">Login</Button>
    </form>
  );
}
