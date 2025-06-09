package com.harshith.EcommerceServer.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.harshith.EcommerceServer.dto.ProductDto;
import com.harshith.EcommerceServer.dto.ProductUpdateDto;
import com.harshith.EcommerceServer.model.entity.Product;
import com.harshith.EcommerceServer.service.ProductService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductService productService;

    @PostMapping("/add-product")
    public ResponseEntity<Product> addProduct(@RequestBody ProductDto productDto) {
        Product product = productService.addProduct(productDto);
        if (product != null) {
            return ResponseEntity.ok().body(product);
        } else {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
        }
    }

    @GetMapping("/get-products")
    public Page<Product> getMethodName(@RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(defaultValue = "id,asc") String[] sort) {
        return productService.getProducts(size, page, sort);
    }

    @PutMapping("/delete-product/{id}")
    public ResponseEntity<Boolean> deleteProduct(@PathVariable Integer id) {
        Boolean isDeleted = productService.deleleProduct(id);
        if (isDeleted) {
            return ResponseEntity.ok().body(true);
        } else {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(false);
        }
    }

    @PutMapping("/update/{id}")
    public ResponseEntity<Boolean> updateProduct(@PathVariable String id,
            @RequestBody ProductUpdateDto productUpdateDto) {
        Boolean isUpdated = productService.updateProduct(Integer.parseInt(id), productUpdateDto.getProductName(),
                productUpdateDto.getStock(), productUpdateDto.getPrice());
        return isUpdated ? ResponseEntity.ok().body(isUpdated)
                : ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(isUpdated);
    }
}
