package com.harshith.resources;

import com.harshith.Alien.Alien;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/alien")
public class AlienResource {
    @GET
    @Produces(MediaType.APPLICATION_XML)
    public Alien getAlien() {
        Alien alien = new Alien();
        alien.setEmail("harshith@gmail.com");
        alien.setId(100);
        alien.setName("Harshith Kurapati");
        
        return alien;
    }


}
