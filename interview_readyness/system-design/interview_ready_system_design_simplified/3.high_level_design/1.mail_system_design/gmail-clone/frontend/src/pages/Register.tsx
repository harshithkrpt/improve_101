import { useForm } from 'react-hook-form';
import { useRegisterUserMutation } from '../services/userService';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useTranslation } from 'react-i18next';
import { toast } from 'sonner';
import { CheckCircle2Icon, AlertCircleIcon } from 'lucide-react';

const registerSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
  confirmPassword: z.string().min(6, 'Confirm Password is required'),
}).refine((data) => data.password === data.confirmPassword, {
  message: 'Passwords do not match',
  path: ['confirmPassword'],
});

export default function Register() {
  const { t } = useTranslation();
  const { register, handleSubmit, formState: { errors }, reset } = useForm<z.infer<typeof registerSchema>>({
    resolver: zodResolver(registerSchema),
  });
  const { user, token } = useAuth();
  const navigate = useNavigate();
  const [registerUser, { isLoading }] = useRegisterUserMutation();

  useEffect(() => {
    if (user && token && navigate) {
      navigate("/");
    }
  }, [user, token, navigate]);

  const onSubmit = async (data: z.infer<typeof registerSchema>) => {
    try {
      await registerUser(data).unwrap();
      toast.success(t('register_success'), {
        icon: <CheckCircle2Icon className="text-green-500" />,
      });
      reset();
      navigate("/login");
    } catch {
      toast.error(t('register_failed'), {
        icon: <AlertCircleIcon className="text-red-500" />,
      });
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="max-w-sm mx-auto mt-20">
      <Card>
        <CardHeader>
          <CardTitle className="text-center">{t('register')}</CardTitle>
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
          <div className="space-y-2">
            <Label htmlFor="confirmPassword">{t('confirm_password')}</Label>
            <Input
              id="confirmPassword"
              type="password"
              placeholder="••••••••"
              {...register('confirmPassword')}
            />
            {errors.confirmPassword && <span className="text-red-500 text-xs">{errors.confirmPassword.message}</span>}
          </div>
          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? t('register') + '...' : t('register')}
          </Button>
        </CardContent>
      </Card>
    </form>
  );
}
