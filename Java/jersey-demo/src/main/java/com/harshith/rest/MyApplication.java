package com.harshith.rest;

import jakarta.ws.rs.ApplicationPath;
import org.glassfish.jersey.server.ResourceConfig;
import org.glassfish.jersey.moxy.xml.MoxyXmlFeature;

@ApplicationPath("/api")
public class MyApplication extends ResourceConfig {
    public MyApplication() {
        packages("com.harshith.resources");
        register(MoxyXmlFeature.class);
    }
}
