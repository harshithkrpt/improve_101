package com.harshith.serviceregistry.controller;

import com.harshith.serviceregistry.dto.ServiceRegistrationRequest;
import com.harshith.serviceregistry.dto.ServiceInfo;
import com.harshith.serviceregistry.service.ServiceRegistryService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Collection;

@RestController
public class ServiceRegistryController {
    private final ServiceRegistryService registryService;

    public ServiceRegistryController(ServiceRegistryService registryService) {
        this.registryService = registryService;
    }

    @PostMapping("/register")
    public ResponseEntity<String> register(@Valid @RequestBody ServiceRegistrationRequest request) {
        ServiceInfo info = new ServiceInfo(
            request.getName(),
            request.getAddress(),
            request.getPort(),
            System.currentTimeMillis()
        );
        registryService.register(info);
        return ResponseEntity.ok("Service registered");
    }

    @GetMapping("/services")
    public Collection<ServiceInfo> getAll() {
        return registryService.getAllServices();
    }

    @GetMapping("/services/{name}")
    public ResponseEntity<ServiceInfo> getByName(@PathVariable String name) {
        ServiceInfo info = registryService.getService(name);
        if (info == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(info);
    }
} 