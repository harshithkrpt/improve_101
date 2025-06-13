package com.harshith.EcommerceServer.dto;

import lombok.Data;

@Data
public class ProductUpdateDto {
    private String name;
    private Integer stock;
    private Double price;
}
