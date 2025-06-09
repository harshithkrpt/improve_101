package com.harshith.EcommerceServer.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
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

    // sort -> id,asc | id,desc
    public Page<Product> getProducts(
        int size, int page, String [] sort) {
        Sort.Order order = Sort.Order.by(sort[0]).with(Sort.Direction.fromString(sort[1]));
        Pageable pageable = PageRequest.of(page,size, Sort.by(order));
        return productRepository.findAllByIsActiveTrue(pageable);
    }

    private Product getProductById(Integer id) {
        return productRepository.findById(id).orElseGet(null);
    }

    public Boolean deleleProduct(Integer productId) {
        if(productId <= 0) return false;

        Product product = this.getProductById(productId);

        if(product == null) {
            return false;
        }   
        
        try {
             product.setIsActive(false);
             productRepository.save(product);
             return true;
        }
        catch(Exception err) {
            return false;
        }
    }

    public Boolean updateProduct(Integer id, String productName, Integer stock, Double price) {
        Product product = this.getProductById(id);
        if(product == null) {
            return false;
        }
        if(productName != "") {
            product.setName(productName);
        }
        if(stock > 0) 
        {
            product.setStock(stock);
        }
        if(price > 0) {
            product.setPrice(price);
        }
        try {
            productRepository.save(product);
            return true;
        }
        catch(Exception exception) {
            return false;
        }
    }


    
}
