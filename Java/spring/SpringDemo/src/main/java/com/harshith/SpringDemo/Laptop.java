package com.harshith.SpringDemo;

import org.springframework.stereotype.Component;

@Component
public class Laptop {
    private String name;

    public Laptop() {
        this.name = "MacBook Pro";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}
