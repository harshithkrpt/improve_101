import { useState } from 'react';
import { registerUser } from '../services/api';
import { Button } from "@/components/ui/button"

export default function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await registerUser(email, password);
      alert('Registration successful!');
    } catch {
      alert('Registration failed.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-16 space-y-4">
      <input className="w-full p-2 border" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input className="w-full p-2 border" type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <Button type="submit">Register</Button>
    </form>
  );
}
