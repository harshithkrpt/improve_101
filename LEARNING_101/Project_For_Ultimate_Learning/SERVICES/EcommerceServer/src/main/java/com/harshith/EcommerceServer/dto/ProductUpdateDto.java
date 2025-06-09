package com.harshith.EcommerceServer.dto;

import lombok.Data;

@Data
public class ProductUpdateDto {
    private String productName;
    private Integer stock;
    private Double price;
}
