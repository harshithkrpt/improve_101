package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Order;

public interface OrderRepository extends JpaRepository<Order, Integer> {
    
}
