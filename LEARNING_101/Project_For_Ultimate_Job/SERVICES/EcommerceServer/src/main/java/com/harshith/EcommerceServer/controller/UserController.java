package com.harshith.EcommerceServer.controller;

import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.model.entity.User;
import com.harshith.EcommerceServer.repository.UserRepository;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController()
@RequestMapping("/users")
public class UserController {

    @Autowired
    UserRepository userRepo;

    @GetMapping("/getAllUsers")
    public List<User> getAllUsers() {
        return userRepo.findAll();
    }

}
