package com.harshith.EcommerceServer.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.model.dto.CategoryDto;
import com.harshith.EcommerceServer.model.dto.CategoryResponseDto;
import com.harshith.EcommerceServer.service.CategoryService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController()
@RequestMapping("/category")
public class CategoryController {
    
    @Autowired
    private CategoryService categoryService;

    @PostMapping("/add-category")
    public ResponseEntity<CategoryResponseDto> addNewCategory(@RequestBody CategoryDto categoryDto) {
        CategoryResponseDto categoryResponseDto = null;
        try {

            categoryResponseDto = categoryService.addCategory(categoryDto);

            return ResponseEntity.ok().body(categoryResponseDto);
        }
        catch(Exception e) {
            return ResponseEntity.internalServerError().body(categoryResponseDto);   
        }
    }
    
}
