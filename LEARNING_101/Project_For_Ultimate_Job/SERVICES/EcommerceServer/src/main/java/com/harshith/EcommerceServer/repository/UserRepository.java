package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.User;

public interface UserRepository extends JpaRepository<User, Integer> {

}