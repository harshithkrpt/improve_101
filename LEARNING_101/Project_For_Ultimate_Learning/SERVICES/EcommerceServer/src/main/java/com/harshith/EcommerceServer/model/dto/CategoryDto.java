package com.harshith.EcommerceServer.model.dto;


/**
 * DTO used when creating or updating a Category.
 * We omit the `id` here for creation; JPA will generate it.
 */
public class CategoryDto {

    // TODO: Adding Validations annotations
    private String name;

    public CategoryDto() { }

    public CategoryDto(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "CategoryDto [name=" + name + "]";
    }
}
