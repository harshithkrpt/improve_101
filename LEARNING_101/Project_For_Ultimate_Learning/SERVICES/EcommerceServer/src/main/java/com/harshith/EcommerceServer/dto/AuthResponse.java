package com.harshith.EcommerceServer.dto;

public class AuthResponse {
    private String message;
    private String username;

    public AuthResponse(String message, String username) {
        this.message = message;
        this.username = username;
    }

    // Getters & setters
    public String getMessage() {
        return message;
    }

    public String getUsername() {
        return username;
    }
}
