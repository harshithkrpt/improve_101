package com.harshith.EcommerceServer.dto;

public class JwtAuthResponse {
    private String accessToken;
    private String tokenType = "Bearer";
    private String username;

    public JwtAuthResponse(String accessToken, String tokenType) {
        this.accessToken = accessToken;
        this.tokenType = tokenType;
    }

    public String getAccessToken() {
        return accessToken;
    }

    public String getTokenType() {
        return tokenType;
    }

    public String getUsername() {
        return username;
    }
}
