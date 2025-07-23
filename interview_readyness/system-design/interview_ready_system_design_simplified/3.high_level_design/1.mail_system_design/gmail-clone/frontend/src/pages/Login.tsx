import { useForm } from 'react-hook-form';
import { useLoginUserMutation } from '../services/userService';
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useTranslation } from 'react-i18next';
import { toast } from 'sonner';
import { CheckCircle2Icon } from 'lucide-react';
import { AlertCircleIcon } from 'lucide-react';

const loginSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
});

export default function Login() {
  const { t } = useTranslation();
  const { register, handleSubmit, formState: { errors } } = useForm<z.infer<typeof loginSchema>>({
    resolver: zodResolver(loginSchema),
  });
  const { login, user, token } = useAuth();
  const navigate = useNavigate();
  const [loginUser, { isLoading }] = useLoginUserMutation();

  useEffect(() => {
    if (user && token) {
      navigate("/");
    }
  }, [user, token, navigate]);

  const onSubmit = async (data: z.infer<typeof loginSchema>) => {
    try {
      const result = await loginUser(data).unwrap();
      login(result.email, result.token); // Save token
      toast.success(t('login_success'), {
        icon: <CheckCircle2Icon className="text-green-500" />,
      });
    } catch {
      toast.error(t('login_failed'), {
        icon: <AlertCircleIcon className="text-red-500" />,
      });
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="max-w-sm mx-auto mt-20">
      <Card>
        <CardHeader>
          <CardTitle className="text-center">{t('login')}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="email">{t('email')}</Label>
            <Input
              id="email"
              type="email"
              placeholder="you@example.com"
              {...register('email')}
            />
            {errors.email && <span className="text-red-500 text-xs">{errors.email.message}</span>}
          </div>
          <div className="space-y-2">
            <Label htmlFor="password">{t('password')}</Label>
            <Input
              id="password"
              type="password"
              placeholder="••••••••"
              {...register('password')}
            />
            {errors.password && <span className="text-red-500 text-xs">{errors.password.message}</span>}
          </div>
          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? t('login') + '...' : t('login')}
          </Button>
        </CardContent>
      </Card>
    </form>
  );
}
