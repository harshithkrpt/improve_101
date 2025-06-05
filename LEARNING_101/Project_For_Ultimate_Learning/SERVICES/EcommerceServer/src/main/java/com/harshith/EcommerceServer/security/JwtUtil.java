package com.harshith.EcommerceServer.security;

import java.security.Key;
import java.util.Date;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.*;

@Component
public class JwtUtil {
    @Value("${jwt.secret}")
    private String jwtSecret;

    @Value("${jwt.expiration-ms}")
    private long jetExpirationMs;

    private Key getSigningKey() {
        return Keys.hmacShaKeyFor(jwtSecret.getBytes());
    }

    @SuppressWarnings("deprecation")
    public String generateToken(String username) {
        Date now = new Date();
        Date expiryDate = new Date(now.getTime() + jetExpirationMs);


    return Jwts.builder()
                   .setSubject(username)
                   .setIssuedAt(now)
                   .setExpiration(expiryDate)
                   .signWith(getSigningKey(), SignatureAlgorithm.HS256)
                   .compact();
    }

    @SuppressWarnings("deprecation")
    public String getUsernameFromJwt(String token) {
        return Jwts.parser()
                   .setSigningKey(getSigningKey())
                   .build()
                   .parseClaimsJws(token)
                   .getBody()
                   .getSubject();
    }

    @SuppressWarnings("deprecation")
    public boolean validateToken(String token) {
        try {
            Jwts.parser()
                .setSigningKey(getSigningKey())
                .build()
                .parseClaimsJws(token);
            return true;
        } catch (JwtException | IllegalArgumentException ex) {
            return false;
        }
    }
}
