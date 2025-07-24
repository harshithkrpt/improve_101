package com.harshith.serviceregistry.service;

import com.harshith.serviceregistry.dto.ServiceInfo;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class ServiceRegistryService {
    private final Map<String, ServiceInfo> registry = new ConcurrentHashMap<>();

    public void register(ServiceInfo info) {
        registry.put(info.getName(), info);
    }

    public Collection<ServiceInfo> getAllServices() {
        return registry.values();
    }

    public ServiceInfo getService(String name) {
        return registry.get(name);
    }
} 