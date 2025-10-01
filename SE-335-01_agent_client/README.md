# Cybersecurity Education Lab - Agent-Based Security Research Platform

## ⚠️ CRITICAL LEGAL AND ETHICAL DISCLAIMER ⚠️

**THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY**

This project has been **COMPLETELY NEUTRALIZED** and converted from malicious code into a safe educational simulation. All dangerous functionality has been removed and replaced with harmless demonstrations.

### Legal Notice
- This software is intended **EXCLUSIVELY** for cybersecurity education and research
- **MUST ONLY** be used in controlled, isolated environments (VMs with no internet access)
- **NEVER** run on production systems or networks you do not own
- Users are **SOLELY RESPONSIBLE** for compliance with all applicable laws
- Unauthorized use may violate computer fraud and abuse laws
- The authors assume **NO LIABILITY** for misuse of this software

### Educational Purpose
This project demonstrates cybersecurity concepts including:
- Attack simulation and detection
- C2 communication patterns (simulated only)
- Data exfiltration prevention techniques
- Security monitoring and logging
- Incident response procedures

## 🔒 Required Safety Environment

### MANDATORY: Isolated VM Setup
**NEVER run on your host machine or real networks**

1. **VM Requirements:**
   - Completely isolated virtual machine
   - **NO internet access** (disconnect network adapter)
   - Snapshot before testing (for easy restore)
   - Dedicated test environment only

2. **Network Isolation:**
   ```bash
   # Verify NO internet connectivity before testing
   ping google.com  # Should fail
   curl -I https://example.com  # Should fail
   ```

3. **Safe Test Data Only:**
   - All simulations use fake/generated data
   - No real user data is accessed
   - Test files are created in `./lab_test_files/` only

## 🎓 Learning Objectives

Students will learn:
1. **Attack Pattern Recognition:** How malware attempts to access browser data
2. **C2 Communication:** Command and control patterns (simulated safely)
3. **Data Exfiltration Methods:** File discovery techniques (demo only)
4. **Defense Strategies:** How to detect and prevent these attacks
5. **Ethical Hacking Principles:** Responsible security research practices

## 🧪 Safe Exercises

### Exercise 1: Cookie Simulation Analysis
```bash
cd SE-335-01_agent_client
python3 -m pytest tests/test_safe_attacks.py::TestSafeAttackSimulations::test_safe_cookie_simulation -v
```

### Exercise 2: File Discovery Simulation
```bash
python3 -m pytest tests/test_safe_attacks.py::TestSafeAttackSimulations::test_safe_file_discovery_simulation -v
```

### Exercise 3: C2 Communication Demo
```bash
python3 -m pytest tests/test_safe_attacks.py::TestSafeAttackSimulations::test_mock_c2_creates_local_files -v
```

### Exercise 4: Security Analysis
1. Examine the simulation output files in `./outbox/`
2. Analyze the fake data patterns
3. Identify detection opportunities
4. Propose countermeasures

## ❌ DO NOT DO - Prohibited Activities

- **NEVER** modify the code to access real browser data
- **NEVER** run outside of isolated VM environment  
- **NEVER** attempt to connect to real C2 servers
- **NEVER** use this code as a base for actual malware
- **NEVER** deploy on networks you don't own and control
- **NEVER** share modified versions that restore malicious functionality

## 🔧 Installation (VM Only)

```bash
# ONLY in isolated VM with NO internet access
git clone [repository-url]
cd SE-335-01_agent_client
python3 -m pip install poetry
poetry install
poetry shell
```

## 🧪 Running Safe Tests

```bash
# Verify safe operation
python3 -m pytest tests/test_safe_attacks.py -v

# Run simulation demo
python3 src/main.py

# Check simulation outputs
ls -la ./lab_test_files/
ls -la ./outbox/
```

## 📊 Expected Safe Outputs

All operations should produce:
- Log files in `./lab_test_files/`
- Simulation data with "SAFE SIMULATION" markers
- Mock payloads in `./outbox/` directory
- No real user data access
- No network connections (except localhost)

## 🔍 Detection Exercise

Students should implement detection for:
1. Unauthorized browser data access attempts
2. Suspicious file system scanning
3. C2 communication patterns
4. Data exfiltration behaviors

## 🤝 Contribution Guidelines

### Acceptable Contributions
- Additional safe simulations
- Enhanced educational content
- Better detection mechanisms
- Documentation improvements
- Security hardening

### Prohibited Contributions
- Any code that accesses real user data
- Actual malicious functionality
- Network exploitation capabilities
- Credential theft mechanisms
- Real attack implementations

## 📚 Educational Resources

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Security Guidelines](https://owasp.org/)
- [Ethical Hacking Principles](https://www.eccouncil.org/ethical-hacking/)
- [Incident Response Procedures](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)

## 🆘 Responsible Disclosure

If you discover any remaining dangerous functionality:
1. **DO NOT EXPLOIT** the vulnerability
2. Immediately report to the project maintainers
3. Provide detailed reproduction steps
4. Suggest safe remediation approaches

## 📞 Support and Questions

For educational support:
- Create GitHub issues for technical questions
- Use discussions for learning assistance
- Contact maintainers for security concerns

---
**Remember: This software is for learning defensive cybersecurity only. Always act ethically and legally.**
