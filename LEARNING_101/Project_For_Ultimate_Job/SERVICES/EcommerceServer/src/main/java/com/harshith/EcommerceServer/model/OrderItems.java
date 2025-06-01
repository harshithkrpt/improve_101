package com.harshith.EcommerceServer.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToOne;

@Entity
public class OrderItems {

    public OrderItems() {
    }

    @Id
    private int id;

    @OneToOne
    private Products products;

    @OneToOne
    private Orders orders;

    @Column(nullable = false)
    private double price;

    @Column(nullable = false)
    private int quantity;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "OrderItems [id=" + id + ", products=" + products + ", orders=" + orders + ", price=" + price
                + ", quantity=" + quantity + "]";
    }
}
