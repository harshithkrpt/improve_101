package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Payment;

public interface PaymentRepository extends JpaRepository<Payment, Integer> {

}
