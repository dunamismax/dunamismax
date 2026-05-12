# Java / PostgreSQL Full Stack

The default stack I use across projects I own unless the product calls for
something outside it. One language, one database, one VM. Anything outside the
default has to earn its place.

## Core

- Java 25 LTS
- Spring Boot 4.0.6+
- Maven
- JDK toolchains
- Java records
- Java virtual threads

## Backend

- Spring MVC
- Embedded Tomcat
- Jackson 3
- Jakarta Validation
- Spring Boot Actuator
- Spring Security only when needed
- jOOQ
- Flyway
- HikariCP

## Database

- PostgreSQL 18
- uuidv7 primary keys
- pgcrypto
- pg_trgm
- pg_stat_statements
- pgvector only for AI/RAG
- PostGIS only for maps/GIS

## Frontend

- Thymeleaf
- HTMX
- Tailwind CSS
- Vanilla JavaScript
- Alpine.js only when needed

## Testing

- JUnit 5
- AssertJ
- Spring Boot Test
- Testcontainers PostgreSQL
- Flyway migration tests
- Playwright only for critical browser flows

## Local dev

- Docker Compose
- justfile
- Maven wrapper
- `.env` for local config
- Mailpit when testing email

## Deploy

- Ubuntu LTS VM
- Caddy for HTTPS/reverse proxy
- Spring Boot fat jar
- systemd service
- PostgreSQL on the VM
- GitHub Actions deploy over SSH
- Flyway migrations
- `pg_dump` backups
- offsite backup copy
