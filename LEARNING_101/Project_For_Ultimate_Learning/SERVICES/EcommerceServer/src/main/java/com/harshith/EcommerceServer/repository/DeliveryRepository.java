package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Delivery;

public interface DeliveryRepository extends JpaRepository<Delivery, Integer> {

}
