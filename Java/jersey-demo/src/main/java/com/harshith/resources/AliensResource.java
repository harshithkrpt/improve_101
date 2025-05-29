package com.harshith.resources;


import com.harshith.Alien.Alien;
import com.harshith.repository.AlienRepository;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;

import java.util.ArrayList;
import java.util.List;

@Path("/aliens")
public class AliensResource {

    AlienRepository alienRepository = new AlienRepository();

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Alien> getAliens() {
        return alienRepository.getAliens();
    }


    @GET
    @Produces(MediaType.APPLICATION_XML)
    @Path("/alien/{id}")
    public Alien getAlienById(@PathParam("id") int id) {
        return alienRepository.getAlienById(id);
    }

    @POST
    @Path("/alien")
    public Alien createAlien(Alien al) {
        return al;
    }
}
