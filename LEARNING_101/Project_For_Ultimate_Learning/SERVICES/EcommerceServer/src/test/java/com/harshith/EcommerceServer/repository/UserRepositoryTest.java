package com.harshith.EcommerceServer.repository;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.sql.Date;
import java.util.List;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase.Replace;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import com.harshith.EcommerceServer.model.entity.User;

@DataJpaTest
@ActiveProfiles("tests")
@AutoConfigureTestDatabase(replace = Replace.NONE)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class UserRepositoryTest {

    @Autowired
    private UserRepository userRepository;

    @BeforeAll
    void verifySchemaEmpty() {
        long count = userRepository.count();
        assertTrue(count == 0, "Schema should be accessible (count >= 0)");
    }

    @Test
    @DisplayName("findAll() -> returns exactly the two saved users")
    void test_findAllUsers() {
        // First user
        User user1 = new User();
        user1.setEmail("john@gmail.com");
        user1.setName("John");
        user1.setRegistrationDate(Date.valueOf("2022-10-10"));
        userRepository.save(user1);

        // Second user
        User user2 = new User();
        user2.setEmail("doe@gmail.com");
        user2.setName("Doe");
        user2.setRegistrationDate(Date.valueOf("2022-10-10"));
        userRepository.save(user2);

        // When we call findAll()
        List<User> users = userRepository.findAll();

        // Then: there should be exactly two
        assertEquals(2, users.size(), "findAll() should return exactly 2 users");

        // Because findAll() returns a List in unspecified order, we check both
        boolean foundJohn = users.stream().anyMatch(u -> "John".equals(u.getName()) && "john@gmail.com".equals(u.getEmail()));
        boolean foundDoe  = users.stream().anyMatch(u -> "Doe".equals(u.getName()) && "doe@gmail.com".equals(u.getEmail()));
        assertTrue(foundJohn, "Should find user1 (John) in the list");
        assertTrue(foundDoe,  "Should find user2 (Doe) in the list");
    }
}
