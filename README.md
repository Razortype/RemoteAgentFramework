# RemoteAgentFramework

## 🎓 Educational Cybersecurity Research Platform

**RemoteAgentFramework** is a **completely neutralized** educational cybersecurity simulation platform designed for academic research and security awareness training. This project demonstrates attack vectors and command & control patterns in a **safe, controlled environment**.

## ⚠️ CRITICAL LEGAL AND ETHICAL DISCLAIMER ⚠️

### 🚨 EDUCATIONAL USE ONLY 🚨

**THIS SOFTWARE HAS BEEN COMPLETELY NEUTRALIZED AND IS FOR EDUCATIONAL PURPOSES ONLY**

- **ALL MALICIOUS FUNCTIONALITY HAS BEEN REMOVED** and replaced with safe simulations
- **MUST ONLY** be used in isolated virtual machines with **NO INTERNET ACCESS**
- **NEVER** run on production systems or networks you do not own
- Users are **SOLELY RESPONSIBLE** for compliance with all applicable laws
- Unauthorized use may violate computer fraud and abuse laws
- The authors assume **NO LIABILITY** for misuse of this software

### Legal Requirements
- ✅ Use only for legitimate cybersecurity education and research
- ✅ Obtain explicit permission before using on any system
- ✅ Comply with all local, state, and federal laws
- ✅ Use only in controlled, isolated environments
- ✅ Report any discovered vulnerabilities responsibly

## 🏗️ Project Architecture

RemoteAgentFramework consists of three main components:

### 1. Agent Client (`SE-335-01_agent_client/`)
**Python-based educational simulation client**
- **Safe cookie discovery simulation** (no real browser data accessed)
- **File discovery demonstration** (limited to test files only)
- **Mock data exfiltration** (writes to local files, no network transmission)
- **Educational logging and monitoring**

```
SE-335-01_agent_client/
├── src/
│   ├── core/                    # Core application logic
│   ├── module/
│   │   ├── attacker_module/     # SAFE attack simulations
│   │   ├── message_handler/     # Communication protocols
│   │   └── attack_logging_module/  # Educational logging
│   └── service/                 # Network and connection services
├── tests/                       # Safety verification tests
├── README.md                    # Component documentation
└── requirements.txt             # Dependencies
```

### 2. Controller Service (`SE-335-01_agent-controller-service/`)
**Spring Boot-based command & control simulation**
- **Localhost-only WebSocket server** for educational demonstrations
- **Safe attack job management** with synthetic data
- **Educational logging and audit trails**
- **Role-based access control for training scenarios**

```
SE-335-01_agent-controller-service/
├── src/main/java/com/razortype/cyberproject/
│   ├── api/                     # REST API controllers
│   ├── service/                 # Business logic
│   ├── entity/                  # Data models
│   ├── config/                  # Security configuration
│   └── auth/                    # Authentication logic
├── src/test/                    # Unit and integration tests
└── pom.xml                      # Maven dependencies
```

### 3. Dashboard (`SE-335-01_agent_controller_dashboard/`)
**React-based monitoring interface**
- **Safe visualization** of simulated attack data
- **Educational dashboards** for training scenarios
- **Synthetic data displays** for learning purposes
- **Secure authentication** for controlled access

```
SE-335-01_agent_controller_dashboard/
├── src/
│   ├── components/              # React components
│   ├── views/                   # Application pages
│   ├── services/                # API communication
│   └── context/                 # State management
├── public/                      # Static assets
└── package.json                 # Dependencies
```

## 🎯 Learning Objectives

Students and researchers will learn:

### 🔍 Attack Pattern Recognition
- How malware attempts to access browser credentials
- File system enumeration techniques
- Command & control communication patterns
- Data exfiltration methodologies

### 🛡️ Defense Strategies
- Detection mechanisms for suspicious activities
- Monitoring and logging best practices
- Incident response procedures
- Network security implementations

### 📚 Cybersecurity Principles
- Ethical hacking methodologies
- Responsible disclosure practices
- Security architecture design
- Risk assessment techniques

## 🔒 Required Safety Environment

### MANDATORY: Isolated VM Setup
**NEVER run on your host machine or real networks**

#### 1. Virtual Machine Requirements
```bash
# Recommended VM specifications
- OS: Ubuntu 20.04 LTS or similar
- RAM: 4GB minimum
- Storage: 20GB minimum  
- Network: COMPLETELY ISOLATED (no internet access)
- Snapshots: Create before testing for easy restore
```

#### 2. Network Isolation Verification
```bash
# VERIFY NO INTERNET ACCESS before running
ping google.com                    # Should FAIL
curl -I https://example.com        # Should FAIL
nslookup google.com               # Should FAIL

# Only localhost should work
ping localhost                     # Should succeed
curl http://localhost:8080        # Should work for local services
```

#### 3. Safe Directory Structure
```bash
# All simulations work only in these safe directories
mkdir -p ./lab_test_files/
mkdir -p ./outbox/
mkdir -p ./simulation_data/

# Verify permissions
chmod 755 ./lab_test_files/
ls -la ./lab_test_files/          # Should show safe test directory
```

## 🚀 Installation and Setup

### Prerequisites
- **Java 17+** (for Spring Boot controller)
- **Python 3.10+** (for agent client)
- **Node.js 18+** (for React dashboard)
- **Docker** (optional, for containerized deployment)

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/razortype/RemoteAgentFramework.git
cd RemoteAgentFramework

# Verify you're in an isolated VM with no internet
ping google.com  # This should FAIL

# If internet is accessible, STOP and fix network isolation first
```

### 2. Agent Client Setup
```bash
cd SE-335-01_agent_client

# Install Python dependencies
python3 -m pip install poetry
poetry install
poetry shell

# Run safety verification tests
python -m pytest tests/test_security_compliance.py -v

# All tests MUST pass before proceeding
```

### 3. Controller Service Setup
```bash
cd ../SE-335-01_agent-controller-service

# Build with Maven
./mvnw clean install

# Run tests to verify safety
./mvnw test

# Start localhost-only server
./mvnw spring-boot:run
```

### 4. Dashboard Setup
```bash
cd ../SE-335-01_agent_controller_dashboard

# Install dependencies
npm install

# Run security audit
npm audit

# Start development server (localhost only)
npm run dev
```

## 🧪 Safe Usage Examples

### Example 1: Cookie Discovery Simulation
```bash
cd SE-335-01_agent_client
python src/main.py

# Expected safe output:
# "SIMULATION: Cookie discovery simulation initiated"
# "WARNING: This simulation uses fake data only"
# "SIMULATION: Generated 4 simulated cookies for educational demonstration"
```

### Example 2: File Discovery Demo
```bash
# Check simulation outputs
ls -la ./lab_test_files/file_discovery_simulation/
cat ./lab_test_files/file_discovery_simulation/test_documents/sample_document.txt

# Should show clearly marked simulation files only
```

### Example 3: C2 Communication Demonstration
```bash
# Check mock C2 outputs
ls -la ./outbox/
cat ./outbox/mock_payload_*.json

# Should show educational simulation data with safety markers
```

## 🧪 Educational Exercises

### Exercise 1: Attack Pattern Analysis
1. Run the safe simulations
2. Analyze the generated log files
3. Identify potential detection points
4. Design countermeasures

### Exercise 2: Defense Implementation
1. Review the simulation code
2. Implement additional safety checks
3. Create detection algorithms
4. Test defensive measures

### Exercise 3: Incident Response
1. Simulate detection of the "attack"
2. Practice incident response procedures
3. Document findings and recommendations
4. Present remediation strategies

## ❌ PROHIBITED ACTIVITIES

### 🚫 DO NOT DO - Will Result in Legal Issues
- **NEVER** modify code to access real browser data
- **NEVER** run outside of isolated VM environment
- **NEVER** attempt to connect to real C2 servers
- **NEVER** use as basis for actual malware development
- **NEVER** deploy on networks you don't own and control
- **NEVER** share versions that restore malicious functionality
- **NEVER** use for unauthorized system access
- **NEVER** bypass the safety mechanisms

## 🔍 Detection Opportunities

Students should implement detection for:

### Network-Based Detection
- Unusual WebSocket connections
- C2 communication patterns
- Data exfiltration attempts
- Suspicious outbound traffic

### Host-Based Detection
- Browser data access attempts
- Unusual file system activity
- Process monitoring
- Registry/configuration changes

### Behavioral Analysis
- Unusual user activity patterns
- Privilege escalation attempts
- Lateral movement indicators
- Data staging activities

## 🧪 Quick Testing

### Check if Ready for Publication
```bash
# Simple publication readiness test (5 minutes)
./simple-publication-test.sh

# Expected result: ✅ READY FOR PUBLICATION!
```

### Detailed Safety Verification
```bash
# Educational safety verification
./verify-educational-safety.sh
```

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for detailed testing instructions.

## 🧪 Running Tests

### Safety Verification Tests
```bash
# Run critical safety tests (MUST all pass)
cd SE-335-01_agent_client
python -m pytest tests/test_security_compliance.py -v

# Run functional simulation tests
python -m pytest tests/test_safe_attacks.py -v
```

### Controller Service Tests
```bash
cd SE-335-01_agent-controller-service
./mvnw test
```

### Dashboard Tests
```bash
cd SE-335-01_agent_controller_dashboard
npm test
```

## 📊 Expected Safe Outputs

All operations should produce:

### ✅ Safe Simulation Indicators
- Log entries marked with "SAFE SIMULATION"
- Fake data clearly labeled as "sim_" or "test_"
- Files only in `./lab_test_files/` directories
- Network connections only to localhost
- Clear educational warnings in all outputs

### ✅ Security Compliance
- No real user data accessed
- No external network connections
- No real browser databases opened
- No actual credential theft
- No unauthorized file access

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

### Quick Guidelines
- All contributions must serve educational purposes
- No code that accesses real user data
- All simulations must be clearly marked as safe
- Security review required for all changes
- Legal compliance verification needed

## 📚 Educational Resources

### Cybersecurity Frameworks
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [OWASP Security Guidelines](https://owasp.org/)

### Learning Materials
- [Ethical Hacking Principles](https://www.eccouncil.org/ethical-hacking/)
- [Incident Response Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
- [Security Architecture Design](https://www.nist.gov/publications)

### Academic Resources
- Course materials and lab exercises
- Research paper templates
- Assessment criteria and rubrics

## 🆘 Responsible Disclosure

### If You Discover Security Issues
1. **DO NOT EXPLOIT** any vulnerabilities found
2. **DO NOT** create public issues for security problems
3. **IMMEDIATELY** contact the security team
4. Provide detailed reproduction steps
5. Suggest safe remediation approaches

### Contact Information
- **Security Issues**: security@[institution].edu
- **Educational Support**: education@[institution].edu
- **General Questions**: Use GitHub Discussions

## 📞 Support

### Getting Help
- **GitHub Issues**: Technical problems and bugs
- **GitHub Discussions**: Educational questions and support
- **Documentation**: Check component READMEs for detailed info
- **Security Concerns**: Contact security team directly

### Community Guidelines
- Be respectful and professional
- Focus on educational value
- Prioritize safety above all else
- Share knowledge responsibly
- Follow ethical guidelines

## 📄 License

This project is licensed under the Educational Use Only License - see the [LICENSE](LICENSE) file for details.

### Key License Points
- **Educational use only** - no commercial use
- **VM isolation required** - no production use
- **Legal compliance mandatory** - follow all applicable laws
- **Safety restrictions** - maintain all security safeguards
- **Institutional oversight** - requires academic supervision

## 🏆 Acknowledgments

- Educational cybersecurity community
- Security researchers who promote ethical practices
- Academic institutions supporting cybersecurity education
- Contributors who maintain safety standards

## 📈 Project Status

### Current Version: 1.0.0-SAFE
- ✅ All malicious functionality neutralized
- ✅ Safe simulations implemented
- ✅ Educational documentation complete
- ✅ Security tests passing
- ⚠️  Legal review pending
- ⚠️  Institutional approval pending

### Roadmap
- [ ] Additional attack pattern simulations
- [ ] Enhanced detection mechanisms
- [ ] Expanded educational content
- [ ] Virtual lab environment integration
- [ ] Instructor training materials

---

**⚠️ REMEMBER: This is educational software for learning defensive cybersecurity. Always act ethically, legally, and responsibly. When in doubt, ask for guidance from qualified professionals.**

**🔒 SAFETY FIRST: If you're unsure about any aspect of this software, consult with cybersecurity professionals and legal experts before proceeding.**