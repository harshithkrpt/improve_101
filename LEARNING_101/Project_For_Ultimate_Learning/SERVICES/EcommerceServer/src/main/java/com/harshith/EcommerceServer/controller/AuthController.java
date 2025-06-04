package com.harshith.EcommerceServer.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.dto.AuthRequest;
import com.harshith.EcommerceServer.dto.AuthResponse;
import com.harshith.EcommerceServer.model.entity.Role;
import com.harshith.EcommerceServer.model.entity.User;
import com.harshith.EcommerceServer.repository.RoleRepository;
import com.harshith.EcommerceServer.repository.UserRepository;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/auth/user")
public class AuthController {
    private final AuthenticationManager authenticationManager;
    private final UserRepository userRepository;
    private final RoleRepository roleRepository;
    private final PasswordEncoder passwordEncoder;

    public AuthController(AuthenticationManager authenticationManager, UserRepository userRepository,
            RoleRepository roleRepository, PasswordEncoder passwordEncoder) {
        this.authenticationManager = authenticationManager;
        this.passwordEncoder = passwordEncoder;
        this.roleRepository = roleRepository;
        this.userRepository = userRepository;
    }

    @PostMapping("/register")
    public ResponseEntity<AuthResponse> resister(@RequestBody AuthRequest authRequest) {
        String username = authRequest.getUsername();
        String password = authRequest.getPassword();

        // Not Check if Any User with Existing Name
        if (userRepository.findByUserName(username).isPresent()) {
            return ResponseEntity.status(HttpStatus.CONFLICT)
                    .body(new AuthResponse("username already exists", username));
        }

        User newUser = new User();
        newUser.setUserName(username);
        newUser.setPassword(passwordEncoder.encode(password));
        newUser.setEnabled(true);
        newUser.setFirstName(username);

        // Now Add a Basic ROLE_USER as the default role
        Role roleUser = roleRepository.findByName("ROLE_USER")
                .orElseGet(() -> roleRepository.save(new Role("ROLE_USER")));

        newUser.addRole(roleUser);

        userRepository.save(newUser);

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new AuthResponse("user registered successfully", username));

    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody AuthRequest authRequest) {
        UsernamePasswordAuthenticationToken usernamePasswordAuthenticationToken = new UsernamePasswordAuthenticationToken(
                authRequest.getUsername(), authRequest.getPassword());

        try {
            authenticationManager.authenticate(usernamePasswordAuthenticationToken);

            return ResponseEntity.status(HttpStatus.OK)
                    .body(new AuthResponse("login successful", authRequest.getUsername()));
        } catch (BadCredentialsException exception) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(new AuthResponse("credentials are invalid", authRequest.getUsername()));
        }
        

    }

}
