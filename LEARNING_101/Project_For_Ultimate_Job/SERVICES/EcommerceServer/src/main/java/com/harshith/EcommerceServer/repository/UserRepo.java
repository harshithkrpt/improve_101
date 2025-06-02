package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.Users;

public interface UserRepo extends JpaRepository<Users, Integer> {

}