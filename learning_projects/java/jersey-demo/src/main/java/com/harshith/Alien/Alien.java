package com.harshith.Alien;


import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "alien")
public class Alien {
    private double id;
    private String name;
    private String email;

    public Alien() {}

    public Alien(double id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    @XmlElement
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @XmlElement
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlElement
    public double getId() {
        return id;
    }

    public void setId(double id) {
        this.id = id;
    }
}
