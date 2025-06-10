package com.harshith.EcommerceServer.config;

import javax.sql.DataSource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import liquibase.exception.LiquibaseException;
import liquibase.integration.spring.SpringLiquibase;

@Configuration
public class LiquibaseConfig {
    private static final Logger logger = LoggerFactory.getLogger(LiquibaseConfig.class);

    // LiquibaseConfig.java
    @Bean
    public SpringLiquibase liquibase(DataSource dataSource) {
        SpringLiquibase lb = new SpringLiquibase() {
            @Override
            public void afterPropertiesSet() throws LiquibaseException {
                logger.info("Starting Liquibase with changelog={}", getChangeLog());
                super.afterPropertiesSet();
                logger.info("Liquibase ran successfully");
            }
        };
        lb.setDataSource(dataSource);
        // <-- remove "classpath:/"
        lb.setChangeLog("db/changelog/db.changelog-master.xml");
        lb.setContexts("development,production");
        lb.setDefaultSchema("ecommercespring");
        lb.setShouldRun(true);
        return lb;
    }

}
