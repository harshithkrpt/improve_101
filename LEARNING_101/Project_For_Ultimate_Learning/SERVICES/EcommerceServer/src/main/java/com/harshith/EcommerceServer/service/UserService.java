package com.harshith.EcommerceServer.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.harshith.EcommerceServer.model.entity.User;
import com.harshith.EcommerceServer.repository.UserRepository;

@Service
public class UserService {
    
    @Autowired
    UserRepository userRepo;

    public List<User> getAllUsers() {
        return userRepo.findAll();
    }
}
