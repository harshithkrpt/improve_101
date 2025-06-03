package com.harshith.EcommerceServer.repository;


import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Category;

public interface CategoryRepository extends JpaRepository<Category,Integer> {

}
