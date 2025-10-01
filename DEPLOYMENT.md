# RemoteAgentFramework Deployment Guide

## Educational Cybersecurity Simulation Framework
**⚠️ CRITICAL: VM ISOLATION REQUIRED - FOR EDUCATIONAL USE ONLY ⚠️**

### Table of Contents
1. [Pre-Deployment Requirements](#pre-deployment-requirements)
2. [Security Prerequisites](#security-prerequisites)
3. [Quick Start Guide](#quick-start-guide)
4. [Production Deployment (Educational)](#production-deployment-educational)
5. [Security Configuration](#security-configuration)
6. [Monitoring and Maintenance](#monitoring-and-maintenance)
7. [Troubleshooting](#troubleshooting)
8. [Educational Compliance](#educational-compliance)

---

## Pre-Deployment Requirements

### ⚠️ MANDATORY SAFETY REQUIREMENTS

1. **VM Isolation (CRITICAL)**
   - Framework MUST run only in isolated virtual machines
   - No direct deployment on physical machines
   - VM must be isolated from production networks
   - Educational network only

2. **Institutional Oversight**
   - Qualified cybersecurity instructor required
   - Institutional approval for educational use
   - Safety protocols established
   - Emergency procedures documented

3. **Legal Compliance**
   - Educational use license agreement signed
   - Institutional liability coverage
   - Student safety training completed
   - Usage monitoring procedures in place

### System Requirements

**Minimum Hardware (VM)**
- CPU: 4 cores
- RAM: 8GB
- Storage: 50GB
- Network: Isolated educational network

**Recommended Hardware (VM)**
- CPU: 8 cores
- RAM: 16GB
- Storage: 100GB
- Network: Dedicated educational VLAN

**Software Requirements**
- Docker 24.0+
- Docker Compose 2.20+
- Git 2.30+
- Linux/macOS/Windows with VM support

---

## Security Prerequisites

### 1. Virtual Machine Setup

**VMware/VirtualBox Configuration:**
```bash
# Example VM configuration
VM_NAME="RemoteAgentFramework-Educational"
VM_MEMORY="8192"  # 8GB RAM
VM_DISK="100GB"
VM_NETWORK="host-only"  # CRITICAL: No bridge mode
VM_SNAPSHOT="clean-educational-env"
```

**VM Network Isolation:**
- Use host-only or internal networks only
- No NAT or bridge connections to production networks
- Firewall rules to block external access
- Educational VLAN if in institutional environment

### 2. Educational Environment Preparation

**Create isolated educational user:**
```bash
# Create dedicated educational user
sudo useradd -m -s /bin/bash edu-cybersec
sudo usermod -aG docker edu-cybersec

# Switch to educational user
sudo su - edu-cybersec
```

**Set educational environment variables:**
```bash
export EDUCATIONAL_FRAMEWORK=RemoteAgentFramework
export VM_ISOLATION_REQUIRED=true
export LOCALHOST_ONLY=true
export SAFETY_VERIFIED=true
export EDUCATIONAL_MODE=true
```

### 3. Security Hardening

**Update system:**
```bash
sudo apt update && sudo apt upgrade -y
sudo yum update -y  # For RHEL/CentOS
```

**Install security tools:**
```bash
# Install security monitoring tools
sudo apt install -y fail2ban ufw rkhunter clamav
```

**Configure firewall (localhost only):**
```bash
# Ubuntu/Debian
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default deny outgoing
sudo ufw allow 127.0.0.1

# Allow only localhost connections
sudo ufw allow from 127.0.0.1 to any port 3000
sudo ufw allow from 127.0.0.1 to any port 8080
sudo ufw allow from 127.0.0.1 to any port 5432
```

---

## Quick Start Guide

### 1. Clone Repository (Educational VM Only)

```bash
# Clone to educational VM
git clone https://github.com/educational/RemoteAgentFramework.git
cd RemoteAgentFramework

# Verify educational safety
./verify-safety.sh
```

### 2. Environment Setup

```bash
# Run educational environment setup
chmod +x setup-dev-environment.sh
./setup-dev-environment.sh

# Follow interactive prompts for VM confirmation
```

### 3. Configuration

```bash
# Copy educational environment template
cp .env.educational .env

# Edit configuration for your educational environment
nano .env
```

**Required .env Configuration:**
```bash
# Educational Framework Configuration
EDUCATIONAL_FRAMEWORK=RemoteAgentFramework
FRAMEWORK_VERSION=1.0.0
EDUCATIONAL_MODE=true
VM_ISOLATION_REQUIRED=true

# Safety Configuration
LOCALHOST_ONLY=true
SAFE_SIMULATION_ONLY=true
MALICIOUS_CODE_NEUTRALIZED=true

# Database (educational only)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cyberproject_db
DB_USER=cyberproject_user
DB_PASSWORD=CHANGE_FOR_YOUR_EDUCATIONAL_ENV

# JWT Security (educational only)
JWT_SECRET=GENERATE_SECURE_SECRET_FOR_EDUCATION
JWT_EXPIRATION=43200000

# Educational Instructor Contact
INSTRUCTOR_EMAIL=instructor@university.edu
INSTITUTION_NAME="University Cybersecurity Program"
```

### 4. Deploy with Docker

```bash
# Start educational services
docker-compose up -d

# Verify deployment
docker-compose ps
docker-compose logs
```

### 5. Verify Educational Safety

```bash
# Run comprehensive safety verification
./verify-safety.sh

# Check educational compliance
curl http://localhost:8080/educational/safety
```

### 6. Access Educational Interface

- **Dashboard**: http://localhost:3000
- **API Documentation**: http://localhost:8080/swagger-ui.html
- **Database Admin**: http://localhost:8080/h2-console (dev only)

---

## Production Deployment (Educational)

### 1. Secure Configuration

**Production .env configuration:**
```bash
# Production Educational Environment
NODE_ENV=production
SPRING_PROFILES_ACTIVE=prod

# Enhanced Security
SSL_ENABLED=true
HTTPS_ONLY=true
SECURE_COOKIES=true
CSRF_PROTECTION=true

# Monitoring
LOG_LEVEL=INFO
AUDIT_LOGGING=true
EDUCATIONAL_MONITORING=true
SAFETY_ALERTS=true

# Institutional Configuration
INSTITUTION_ID=YOUR_INSTITUTION_ID
INSTRUCTOR_SUPERVISION=required
STUDENT_SAFETY_TRAINING=verified
```

### 2. SSL/TLS Configuration (Educational)

**Generate educational certificates:**
```bash
# Create educational CA
openssl genrsa -out educational-ca.key 4096
openssl req -new -x509 -days 365 -key educational-ca.key -out educational-ca.crt \
  -subj "/C=US/ST=State/L=City/O=Educational Institution/OU=Cybersecurity Program/CN=Educational CA"

# Generate server certificate
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr \
  -subj "/C=US/ST=State/L=City/O=Educational Institution/OU=Cybersecurity Program/CN=localhost"
openssl x509 -req -days 365 -in server.csr -CA educational-ca.crt -CAkey educational-ca.key -out server.crt
```

### 3. Database Security

**PostgreSQL production configuration:**
```sql
-- Create educational database with security
CREATE DATABASE cyberproject_db WITH 
  ENCODING 'UTF8'
  LC_COLLATE 'en_US.UTF-8'
  LC_CTYPE 'en_US.UTF-8'
  TEMPLATE template0;

-- Create educational user with limited privileges
CREATE ROLE cyberproject_user WITH
  LOGIN
  NOSUPERUSER
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION
  PASSWORD 'secure_educational_password';

-- Grant minimal required permissions
GRANT CONNECT ON DATABASE cyberproject_db TO cyberproject_user;
GRANT USAGE ON SCHEMA public TO cyberproject_user;
GRANT CREATE ON SCHEMA public TO cyberproject_user;
```

### 4. Production Docker Compose

**docker-compose.prod.yml:**
```yaml
version: '3.8'

services:
  database:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: cyberproject_db
      POSTGRES_USER: cyberproject_user
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./ssl:/var/lib/postgresql/ssl:ro
    command: >
      postgres
      -c ssl=on
      -c ssl_cert_file=/var/lib/postgresql/ssl/server.crt
      -c ssl_key_file=/var/lib/postgresql/ssl/server.key

  controller-service:
    build:
      context: ./SE-335-01_agent-controller-service
      dockerfile: Dockerfile.prod
    environment:
      SPRING_PROFILES_ACTIVE: prod
      SPRING_DATASOURCE_URL: jdbc:postgresql://database:5432/cyberproject_db?sslmode=require
      SPRING_DATASOURCE_PASSWORD_FILE: /run/secrets/db_password
      JWT_SECRET_FILE: /run/secrets/jwt_secret
    secrets:
      - db_password
      - jwt_secret
    depends_on:
      - database

secrets:
  db_password:
    file: ./secrets/db_password.txt
  jwt_secret:
    file: ./secrets/jwt_secret.txt

volumes:
  postgres_data:
    driver: local
```

---

## Security Configuration

### 1. Spring Boot Security (Production)

**application-prod.yml:**
```yaml
server:
  port: 8080
  address: 127.0.0.1
  ssl:
    enabled: true
    key-store: classpath:educational-keystore.p12
    key-store-password: educational_keystore_password
    key-store-type: PKCS12
  servlet:
    session:
      cookie:
        secure: true
        http-only: true
        same-site: strict

spring:
  security:
    require-ssl: true
  datasource:
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000

application:
  security:
    jwt:
      expiration: 43200000  # 12 hours for educational sessions
    educational:
      instructor-supervision-required: true
      student-safety-training-verified: true
      vm-isolation-enforced: true
```

### 2. Nginx Security Configuration

**nginx.prod.conf:**
```nginx
server {
    listen 443 ssl http2;
    server_name localhost;
    
    # Educational SSL configuration
    ssl_certificate /etc/ssl/certs/educational.crt;
    ssl_certificate_key /etc/ssl/private/educational.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    
    # Security headers for educational environment
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options DENY always;
    add_header X-Content-Type-Options nosniff always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header X-Educational-Framework "RemoteAgentFramework" always;
    add_header X-Educational-Warning "VM-ISOLATION-REQUIRED" always;
    
    # Educational access restrictions
    allow 127.0.0.1;
    allow ::1;
    deny all;
    
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
        
        # Educational content security policy
        add_header Content-Security-Policy "
          default-src 'self';
          script-src 'self' 'unsafe-inline';
          style-src 'self' 'unsafe-inline';
          img-src 'self' data:;
          connect-src 'self' wss://localhost:8080;
          base-uri 'self';
          form-action 'self';
          frame-ancestors 'none';
        " always;
    }
    
    # Proxy to educational API
    location /api/ {
        proxy_pass https://localhost:8080/;
        proxy_ssl_verify off;  # Educational self-signed certs
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Educational-Access "supervised";
    }
}
```

---

## Monitoring and Maintenance

### 1. Educational Monitoring Setup

**Monitoring stack:**
```yaml
# monitoring/docker-compose.yml
version: '3.8'

services:
  educational-monitor:
    image: prom/prometheus:latest
    ports:
      - "127.0.0.1:9090:9090"
    volumes:
      - ./prometheus-educational.yml:/etc/prometheus/prometheus.yml
    
  educational-alerts:
    image: prom/alertmanager:latest
    ports:
      - "127.0.0.1:9093:9093"
    volumes:
      - ./alertmanager-educational.yml:/etc/alertmanager/alertmanager.yml
```

### 2. Log Management

**Centralized logging:**
```bash
# Create educational log aggregation
mkdir -p /var/log/educational-framework

# Configure log rotation
cat > /etc/logrotate.d/educational-framework << EOF
/var/log/educational-framework/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 640 edu-cybersec edu-cybersec
    postrotate
        # Educational safety: Archive logs for compliance
        tar -czf /var/log/educational-framework/archive/logs-$(date +%Y%m%d).tar.gz /var/log/educational-framework/*.log.1
    endscript
}
EOF
```

### 3. Health Checks

**Educational health monitoring:**
```bash
#!/bin/bash
# educational-health-check.sh

echo "🔍 Educational Framework Health Check"

# Check VM isolation
check_vm_isolation() {
    echo "Checking VM isolation..."
    if systemd-detect-virt >/dev/null 2>&1; then
        echo "✅ VM isolation verified"
    else
        echo "❌ VM isolation check failed"
        return 1
    fi
}

# Check educational services
check_services() {
    echo "Checking educational services..."
    
    # Check database
    if docker-compose exec database pg_isready >/dev/null 2>&1; then
        echo "✅ Database healthy"
    else
        echo "❌ Database unhealthy"
        return 1
    fi
    
    # Check controller
    if curl -f http://localhost:8080/actuator/health >/dev/null 2>&1; then
        echo "✅ Controller service healthy"
    else
        echo "❌ Controller service unhealthy"
        return 1
    fi
    
    # Check dashboard
    if curl -f http://localhost:3000 >/dev/null 2>&1; then
        echo "✅ Dashboard healthy"
    else
        echo "❌ Dashboard unhealthy"
        return 1
    fi
}

# Check educational safety
check_educational_safety() {
    echo "Checking educational safety measures..."
    
    # Verify safety endpoint
    SAFETY_RESPONSE=$(curl -s http://localhost:8080/educational/safety)
    if echo "$SAFETY_RESPONSE" | jq -e '.vmIsolationRequired == true' >/dev/null 2>&1; then
        echo "✅ Educational safety verified"
    else
        echo "❌ Educational safety check failed"
        return 1
    fi
}

# Run all checks
check_vm_isolation && check_services && check_educational_safety
```

### 4. Backup and Recovery

**Educational data backup:**
```bash
#!/bin/bash
# educational-backup.sh

BACKUP_DIR="/var/backups/educational-framework"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup database
docker-compose exec database pg_dump -U cyberproject_user cyberproject_db | \
  gzip > "$BACKUP_DIR/database_$DATE.sql.gz"

# Backup configuration
tar -czf "$BACKUP_DIR/config_$DATE.tar.gz" .env docker-compose.yml

# Backup educational logs
tar -czf "$BACKUP_DIR/logs_$DATE.tar.gz" /var/log/educational-framework/

echo "Educational backup completed: $BACKUP_DIR"
```

---

## Troubleshooting

### Common Issues

1. **VM Isolation Not Detected**
   ```bash
   # Verify VM environment
   systemd-detect-virt
   dmesg | grep -i virtual
   lscpu | grep -i hypervisor
   ```

2. **Educational Services Not Starting**
   ```bash
   # Check Docker logs
   docker-compose logs database
   docker-compose logs controller-service
   docker-compose logs dashboard
   
   # Verify network configuration
   docker network ls
   docker network inspect cyberproject_raf-network
   ```

3. **Educational Safety Verification Failed**
   ```bash
   # Run safety verification
   ./verify-safety.sh
   
   # Check environment variables
   env | grep EDUCATIONAL
   
   # Verify localhost bindings
   netstat -tlnp | grep -E ':(3000|8080|5432)'
   ```

4. **Database Connection Issues**
   ```bash
   # Test database connectivity
   docker-compose exec database psql -U cyberproject_user -d cyberproject_db -c "SELECT 1;"
   
   # Check database logs
   docker-compose logs database | tail -50
   ```

### Performance Optimization

**VM Resource Allocation:**
```bash
# Optimize VM for educational use
echo 'vm.swappiness=10' >> /etc/sysctl.conf
echo 'vm.dirty_ratio=15' >> /etc/sysctl.conf
echo 'vm.dirty_background_ratio=5' >> /etc/sysctl.conf
sysctl -p
```

**Docker Optimization:**
```json
{
  "storage-driver": "overlay2",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "5"
  },
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Hard": 64000,
      "Soft": 64000
    }
  }
}
```

---

## Educational Compliance

### Deployment Checklist

**Pre-Deployment:**
- [ ] VM isolation verified
- [ ] Instructor oversight confirmed
- [ ] Educational license approved
- [ ] Safety training completed
- [ ] Network isolation configured
- [ ] Institutional approval obtained

**Deployment:**
- [ ] Educational environment setup
- [ ] Safety verification passed
- [ ] Localhost-only binding confirmed
- [ ] Educational markers present
- [ ] Monitoring configured
- [ ] Backup procedures tested

**Post-Deployment:**
- [ ] Educational compliance verified
- [ ] Student access controls tested
- [ ] Instructor oversight functional
- [ ] Safety monitoring active
- [ ] Emergency procedures documented
- [ ] Usage logging enabled

### Compliance Documentation

**Required Documentation:**
1. Institutional approval letter
2. Instructor qualifications certificate
3. Student safety training records
4. VM isolation verification report
5. Educational use agreement
6. Emergency response procedures

### Regular Compliance Checks

**Monthly Reviews:**
- Educational safety measures verification
- VM isolation status check
- Student usage monitoring review
- Instructor oversight documentation
- Safety incident reports (if any)
- Educational outcome assessments

---

**⚠️ IMPORTANT REMINDER: This framework is for educational use only and requires proper institutional oversight, qualified instruction, and VM isolation for safe operation. Never deploy in production environments or without proper safety measures.**