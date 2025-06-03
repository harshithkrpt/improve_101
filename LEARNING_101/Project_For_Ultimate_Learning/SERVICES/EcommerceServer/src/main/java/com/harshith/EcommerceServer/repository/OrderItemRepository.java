package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Integer> {

}
