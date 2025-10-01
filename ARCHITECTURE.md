# RemoteAgentFramework Architecture Documentation

## Educational Cybersecurity Simulation Framework
**⚠️ FOR EDUCATIONAL USE ONLY - VM ISOLATION REQUIRED ⚠️**

### Table of Contents
1. [System Overview](#system-overview)
2. [Architecture Diagram](#architecture-diagram)
3. [Component Details](#component-details)
4. [Security Architecture](#security-architecture)
5. [Educational Safety Measures](#educational-safety-measures)
6. [Data Flow](#data-flow)
7. [Deployment Architecture](#deployment-architecture)
8. [API Architecture](#api-architecture)

---

## System Overview

RemoteAgentFramework is an educational cybersecurity simulation platform designed to safely demonstrate Command & Control (C2) communication patterns and attack simulation techniques in a controlled learning environment.

### Key Principles
- **Educational Safety First**: All malicious functionality neutralized
- **VM Isolation Required**: Must run only in isolated virtual machines
- **Localhost-Only**: Network access restricted to localhost
- **Safe Simulations**: Real data replaced with educational simulations
- **Transparent Learning**: All code available for educational review

### Architecture Style
- **Microservices Architecture**: Containerized services
- **Event-Driven**: WebSocket-based real-time communication
- **RESTful API**: Standard HTTP/JSON API design
- **Layered Security**: Multiple security boundaries

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    EDUCATIONAL VM ISOLATION                     │
│                   (Required Safety Boundary)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │    React UI     │    │   Spring Boot   │    │ PostgreSQL  │  │
│  │    Dashboard    │◄──►│   Controller    │◄──►│  Database   │  │
│  │   (Port 3000)   │    │   (Port 8080)   │    │ (Port 5432) │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│           │                       │                             │
│           │              ┌────────▼────────┐                    │
│           │              │    WebSocket    │                    │
│           │              │   Communication │                    │
│           │              │   (Localhost)   │                    │
│           │              └────────┬────────┘                    │
│           │                       │                             │
│  ┌────────▼───────────────────────▼────────┐                    │
│  │         Educational Agent Clients       │                    │
│  │            (Python Simulation)          │                    │
│  │      ┌─────────────────────────────┐    │                    │
│  │      │   Safe Attack Simulations   │    │                    │
│  │      │   • Fake Cookie Generation  │    │                    │
│  │      │   • Test File Scanning      │    │                    │
│  │      │   • Demo Network Probes     │    │                    │
│  │      └─────────────────────────────┘    │                    │
│  └─────────────────────────────────────────┘                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                     DOCKER NETWORK ISOLATION                    │
│                         (172.20.0.0/16)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. React Dashboard (Frontend)
**Technology Stack:**
- React 18.3.1 with TypeScript support
- Material-UI for educational-friendly interface
- Axios for API communication
- WebSocket client for real-time updates
- Nginx for static file serving

**Key Features:**
- Real-time agent monitoring
- Educational attack simulation controls
- Safe log visualization
- User authentication (educational accounts)
- Educational safety warnings

**Security Measures:**
- Content Security Policy (CSP) headers
- Localhost-only API connections
- Educational framework identification headers
- XSS protection

### 2. Spring Boot Controller Service (Backend)
**Technology Stack:**
- Spring Boot 3.2.4 with Java 21
- Spring Security for authentication
- Spring WebSocket for real-time communication
- JPA/Hibernate for database access
- PostgreSQL database

**Key Features:**
- RESTful API for educational operations
- JWT-based authentication
- WebSocket communication hub
- Educational attack job management
- Safe logging and monitoring
- Educational safety verification endpoints

**Security Measures:**
- JWT token validation
- CORS configuration (localhost only)
- Input validation and sanitization
- Educational usage tracking
- Database access controls

### 3. Python Agent Client
**Technology Stack:**
- Python 3.10+ with Poetry dependency management
- WebSocket client for C2 communication
- Faker library for safe data generation
- Pydantic for data validation
- Pytest for educational testing

**Key Features:**
- Safe attack simulations (no real data access)
- Educational logging and reporting
- Localhost-only network communication
- Fake data generation for demonstrations
- Educational safety verification

**Security Measures:**
- Browser-cookie3 removed (replaced with faker)
- File system access limited to test directories
- Network access restricted to localhost
- All real attack vectors neutralized

### 4. PostgreSQL Database
**Configuration:**
- PostgreSQL 16 in Docker container
- Educational-only data storage
- Localhost-only connections
- Automated educational safety logging

**Schema Design:**
- User management (educational accounts)
- Attack job tracking (simulation only)
- Educational log storage
- Safety verification records

---

## Security Architecture

### Educational Safety Boundaries

1. **VM Isolation Boundary** (Outermost)
   - Framework must run only in isolated VMs
   - No production network access
   - Educational environment markers required

2. **Docker Network Isolation**
   - Custom bridge network (172.20.0.0/16)
   - Container-to-container communication only
   - No external network access

3. **Application Security Layer**
   - Localhost-only binding (127.0.0.1)
   - CORS restrictions
   - Authentication required
   - Input validation

4. **Educational Code Safety**
   - All malicious code neutralized
   - Safe simulations only
   - Fake data generation
   - Educational markers throughout

### Authentication Flow
```
Client → Login Request → Spring Security → JWT Generation → 
Database Verification → Token Response → Authenticated Access
```

### Authorization Levels
- **STUDENT**: View simulations, run pre-defined educational attacks
- **INSTRUCTOR**: Create educational scenarios, monitor students
- **ADMIN**: Full system administration, safety configuration

---

## Educational Safety Measures

### Code Neutralization
1. **Browser Cookie Access**: Removed browser-cookie3, replaced with Faker
2. **File System Access**: Limited to test/demo directories only
3. **Network Communication**: Forced localhost-only connections
4. **Data Extraction**: All real data replaced with educational simulations

### Safety Verification
- Automated safety tests in CI/CD pipeline
- Pre-commit hooks for educational compliance
- Runtime safety verification endpoints
- Educational environment variable checks

### Monitoring and Logging
- All educational activities logged
- Safety violation detection
- Educational usage analytics
- VM isolation verification

---

## Data Flow

### Educational Attack Simulation Flow
```
1. Instructor creates educational attack job via Dashboard
2. Spring Boot controller validates and stores job
3. WebSocket notifies connected educational agents
4. Python agent executes SAFE simulation
5. Fake results generated and sent back
6. Educational logs stored and displayed
7. Students review learning outcomes
```

### Real-time Communication Flow
```
Dashboard ←→ WebSocket ←→ Spring Boot ←→ Database
    ↑                                        ↓
    └── Educational Agents (Python) ←────────┘
```

---

## Deployment Architecture

### Docker Compose Services
1. **raf-database**: PostgreSQL with educational schema
2. **raf-controller**: Spring Boot application server
3. **raf-dashboard**: React UI with Nginx
4. **raf-agent-client**: Python educational agents

### Network Configuration
- **raf-network**: Custom bridge network
- **Port Bindings**: All bound to 127.0.0.1 only
- **Volume Mounts**: Educational data persistence

### Health Checks
- Database: PostgreSQL readiness check
- Controller: Spring Boot health actuator
- Dashboard: HTTP response check
- Agents: Educational safety verification

---

## API Architecture

### RESTful Endpoints
- `/auth/*`: Educational user authentication
- `/agents/*`: Educational agent management  
- `/attacks/*`: Safe attack simulation management
- `/logs/*`: Educational logging access
- `/educational/safety`: Safety verification

### WebSocket Communication
- **Endpoint**: `/ws` (localhost only)
- **Authentication**: JWT token required
- **Messages**: Educational simulation commands only
- **Safety**: All real attack vectors neutralized

### API Security
- JWT authentication required
- Rate limiting for educational use
- Input validation and sanitization
- Educational usage tracking
- CORS restricted to localhost

---

## Educational Compliance

### Required Environment Markers
```bash
EDUCATIONAL_FRAMEWORK=RemoteAgentFramework
VM_ISOLATION_REQUIRED=true
LOCALHOST_ONLY=true
SAFE_SIMULATION_ONLY=true
MALICIOUS_CODE_NEUTRALIZED=true
```

### Institutional Requirements
1. **VM Isolation**: Mandatory virtualized environment
2. **Instructor Oversight**: Qualified cybersecurity instructor required
3. **Educational License**: Proper licensing for educational use
4. **Safety Training**: Students must complete safety training
5. **Usage Monitoring**: All activities logged and monitored

### Legal Compliance
- Educational use license only
- No production deployment permitted
- Institutional oversight required
- Safety measures documentation
- Incident reporting procedures

---

## Maintenance and Updates

### Security Updates
- Regular dependency vulnerability scans
- Educational safety verification tests
- Docker image security updates
- Educational compliance reviews

### Educational Enhancements
- New safe simulation scenarios
- Improved educational materials
- Enhanced safety measures
- Better learning analytics

### Version Control
- Git-based version control
- Educational safety pre-commit hooks
- Automated testing pipeline
- Educational compliance verification

---

*This architecture serves educational purposes only and requires proper institutional oversight and VM isolation for safe operation.*