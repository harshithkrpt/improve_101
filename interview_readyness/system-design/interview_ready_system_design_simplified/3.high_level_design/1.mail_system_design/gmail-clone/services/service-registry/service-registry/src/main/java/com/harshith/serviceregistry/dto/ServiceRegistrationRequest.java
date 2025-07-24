package com.harshith.serviceregistry.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class ServiceRegistrationRequest {
    @NotBlank
    private String name;
    @NotBlank
    private String address;
    @NotNull
    private Integer port;

    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public Integer getPort() { return port; }
    public void setPort(Integer port) { this.port = port; }
} 