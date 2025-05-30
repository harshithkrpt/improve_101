package com.harshith.SpringDemo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Person {

    @Autowired
    Laptop laptop;

    public void speaking() {
        System.out.println("Hello Person I am speaking");
        System.out.println(laptop.getName());
    }
}
