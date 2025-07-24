package com.harshith.serviceregistry.dto;

public class ServiceInfo {
    private String name;
    private String address;
    private Integer port;
    private long lastHeartbeat;

    public ServiceInfo(String name, String address, Integer port, long lastHeartbeat) {
        this.name = name;
        this.address = address;
        this.port = port;
        this.lastHeartbeat = lastHeartbeat;
    }

    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public Integer getPort() { return port; }
    public void setPort(Integer port) { this.port = port; }
    public long getLastHeartbeat() { return lastHeartbeat; }
    public void setLastHeartbeat(long lastHeartbeat) { this.lastHeartbeat = lastHeartbeat; }
} 