package com.harshith.EcommerceServer.model.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "roles")
@NoArgsConstructor
@Getter
@Setter
public class Role {
    @Id
    private int id;

    @Column(name = "name", nullable = false, unique = true, length = 100)
    private String name;

    public Role(String name) {
        this.name = name;
    }
}
