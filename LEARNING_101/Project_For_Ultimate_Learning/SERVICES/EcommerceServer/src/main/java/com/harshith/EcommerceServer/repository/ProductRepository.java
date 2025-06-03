package com.harshith.EcommerceServer.repository;
import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Product;


public interface ProductRepository extends JpaRepository<Product, Integer> {

}
