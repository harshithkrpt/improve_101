package com.harshith.EcommerceServer.controller;

import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.model.entity.User;
import com.harshith.EcommerceServer.service.UserService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

// TODO: Add Authorization
@RestController()
@RequestMapping("/users")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/getAllUsers")
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

}
