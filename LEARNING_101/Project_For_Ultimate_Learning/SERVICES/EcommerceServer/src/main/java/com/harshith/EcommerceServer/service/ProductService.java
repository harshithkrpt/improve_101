package com.harshith.EcommerceServer.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.harshith.EcommerceServer.dto.ProductDto;
import com.harshith.EcommerceServer.model.entity.Category;
import com.harshith.EcommerceServer.model.entity.Product;
import com.harshith.EcommerceServer.repository.CategoryRepository;
import com.harshith.EcommerceServer.repository.ProductRepository;

@Service
public class ProductService {
    @Autowired
    ProductRepository productRepository;

    @Autowired
    CategoryRepository categoryRepository;


    // TODO: How & Where to Add Validations
    public Product addProduct(ProductDto productDto) {
        Category category = null;
        if(productDto.getCategoryId() != 0 || productDto.getCategoryName() != "") {
             category = categoryRepository.findById(productDto.getCategoryId()).orElseGet(() ->  categoryRepository.save(new Category(productDto.getCategoryName())));
        }
        // Now Extract all the productDto and add it to product entity
        Product product = new Product();
        product.setCategories(category);
        product.setName(productDto.getName());
        product.setPrice(productDto.getPrice());
        product.setStock(productDto.getStock());
        product.setProductImage(productDto.getProductImage());
        Product sProduct = productRepository.save(product);

        return sProduct;
    }
}
