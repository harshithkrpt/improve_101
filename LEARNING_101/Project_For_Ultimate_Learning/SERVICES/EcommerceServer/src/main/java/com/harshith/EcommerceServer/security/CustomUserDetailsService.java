package com.harshith.EcommerceServer.security;


import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.harshith.EcommerceServer.model.entity.User;
import com.harshith.EcommerceServer.repository.UserRepository;

@Service
public class CustomUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
        User user = userRepository.findByUserName(userName) .orElseThrow(() -> 
                new UsernameNotFoundException("User not found: " + userName)
            );

        return new CustomUserDetails(user);
    }
    
}
