package com.harshith.authservice.controller;

import com.harshith.authservice.service.AuthService;
import lombok.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {
    private final AuthService authService;

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@Valid @RequestBody SignupRequest req) {
        authService.signup(req.getEmail(), req.getPassword());
        return ResponseEntity.ok("User registered successfully");
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@Valid @RequestBody LoginRequest req) {
        String token = authService.login(req.getEmail(), req.getPassword());
        return ResponseEntity.ok(new LoginResponse(token));
    }

    @Data static class SignupRequest {
        private String email;
        private String password;
    }

    @Data @AllArgsConstructor static class LoginResponse {
        private String token;
    }

    @Data static class LoginRequest {
        private String email;
        private String password;
    }
}