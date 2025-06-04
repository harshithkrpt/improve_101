package com.harshith.EcommerceServer.repository;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

import com.harshith.EcommerceServer.model.entity.Role;

public interface RoleRepository extends JpaRepository<Role, Integer> {
    Optional<Role> findByName(String name);
}
