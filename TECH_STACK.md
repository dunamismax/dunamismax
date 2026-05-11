# Kotlin / PostgreSQL Tech Stack

The single stack I use across every project I own. One language, one
database, one VM. Everything below is the default; anything outside it
has to earn its place.

## Core

- Kotlin 2.2.20+
- JDK 21
- Gradle Kotlin DSL

## Backend

- Spring Boot 4.0.6
- Spring MVC
- Virtual threads
- kotlinx.serialization
- Spring Data JDBC
- jOOQ
- Flyway

## Database

- PostgreSQL 18
- pgcrypto
- pg_trgm
- pg_stat_statements
- pgvector only for AI/RAG
- PostGIS only for maps/GIS

## Frontend

- Thymeleaf
- HTMX
- Tailwind

## Testing

- Spring Boot Test
- Testcontainers PostgreSQL

## Local dev

- Docker Compose
- justfile

## Deploy

- Ubuntu VM
- Caddy for HTTPS/reverse proxy
- Spring Boot fat jar
- systemd service
- PostgreSQL on the VM
- GitHub Actions deploy over SSH
- Flyway migrations
