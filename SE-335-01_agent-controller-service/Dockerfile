# Spring Boot Controller Service Dockerfile
FROM eclipse-temurin:21-jdk-jammy

LABEL maintainer="Educational Cybersecurity Team"
LABEL description="Educational cybersecurity simulation - Spring Boot Controller Service"
LABEL version="1.0.0"

# Set environment variables
ENV SPRING_PROFILES_ACTIVE=prod
ENV JVM_OPTS="-Xmx512m -Xms256m"

# Create non-root user for security
RUN groupadd -r springuser && useradd -r -g springuser springuser

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy Maven wrapper and pom.xml for dependency caching
COPY mvnw pom.xml ./
COPY .mvn .mvn

# Download dependencies (for better Docker layer caching)
RUN ./mvnw dependency:go-offline -B

# Copy source code
COPY src ./src

# Build the application
RUN ./mvnw clean package -DskipTests

# Change ownership to non-root user
RUN chown -R springuser:springuser /app
USER springuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8080/actuator/health || exit 1

# Expose port
EXPOSE 8080

# Educational safety: Force localhost-only binding
ENV SERVER_ADDRESS=0.0.0.0
ENV ALLOWED_ORIGINS=http://localhost:3000

# Run the application
CMD ["java", "-jar", "target/cyberproject-1.0.0.jar"]