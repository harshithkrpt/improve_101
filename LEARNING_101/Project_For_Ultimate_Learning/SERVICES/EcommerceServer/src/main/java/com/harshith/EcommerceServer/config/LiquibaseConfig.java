package com.harshith.EcommerceServer.config;

import javax.sql.DataSource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import liquibase.integration.spring.SpringLiquibase;

@Configuration
public class LiquibaseConfig {

    @Bean
    public SpringLiquibase liquibase(DataSource dataSource) {
        SpringLiquibase lb = new SpringLiquibase();
        lb.setDataSource(dataSource);
        lb.setChangeLog("classpath:/db/changelog/db.changelog-master.yaml");
        lb.setContexts("development,production");
        lb.setDefaultSchema("ecommercespring");
        lb.setShouldRun(true);
        return lb;
    }

}
