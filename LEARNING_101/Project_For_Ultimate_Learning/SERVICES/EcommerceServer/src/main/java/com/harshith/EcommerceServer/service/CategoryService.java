package com.harshith.EcommerceServer.service;

import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.harshith.EcommerceServer.model.dto.CategoryDto;
import com.harshith.EcommerceServer.model.dto.CategoryResponseDto;
import com.harshith.EcommerceServer.model.entity.Category;
import com.harshith.EcommerceServer.repository.CategoryRepository;

@Service
public class CategoryService {

    @Autowired
    private CategoryRepository categoryRepository;

    public List<Category> getCategories() {
        return categoryRepository.findAll();
    }

    public CategoryResponseDto addCategory(CategoryDto categoryDto) throws Exception {
        Category category = new Category();
        if(categoryDto.getName().length() == 0) {
            throw new Exception();
        }
        category.setName(categoryDto.getName());
        Category sCategory = categoryRepository.save(category);
        
        return new CategoryResponseDto(sCategory.getId(), sCategory.getName());
    }
}
