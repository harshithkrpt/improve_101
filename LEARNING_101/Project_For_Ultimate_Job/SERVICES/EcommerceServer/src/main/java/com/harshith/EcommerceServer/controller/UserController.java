package com.harshith.EcommerceServer.controller;

import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.model.Users;
import com.harshith.EcommerceServer.repository.UserRepo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController()
@RequestMapping("/users")
public class UserController {

    @Autowired
    UserRepo userRepo;

    @GetMapping("/getAllUsers")
    public List<Users> getAllUsers() {
        return userRepo.findAll();
    }

}
