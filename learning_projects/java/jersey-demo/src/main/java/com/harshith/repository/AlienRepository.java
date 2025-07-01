package com.harshith.repository;

import com.harshith.Alien.Alien;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class AlienRepository {
    List<Alien> aliens;

    public AlienRepository() {
        aliens =  new ArrayList<>();
        aliens.add(new Alien(1, "Harshith","harshith.krpt@gmail.com"));
        aliens.add(new Alien(2, "Kurapti", "harshith@gmail.com"));
    }

    public List<Alien> getAliens() {
        return aliens;
    }

    public Alien getAlienById(double id) {
        return  aliens.stream().filter(a -> a.getId() == id).findFirst().orElse(null);
    }

    public void Create(Alien al) {
        aliens.add(al);
    }
}
