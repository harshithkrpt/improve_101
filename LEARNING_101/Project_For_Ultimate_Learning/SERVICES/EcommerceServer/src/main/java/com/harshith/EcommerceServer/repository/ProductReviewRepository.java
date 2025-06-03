package com.harshith.EcommerceServer.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.ProductReview;

public interface ProductReviewRepository extends JpaRepository<ProductReview, Integer> {
}
