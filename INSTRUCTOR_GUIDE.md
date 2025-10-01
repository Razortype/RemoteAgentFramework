# 👨‍🏫 Instructor Guide for RemoteAgentFramework

## 🎓 Educational Cybersecurity Simulation Framework

This guide provides comprehensive instructions for **qualified cybersecurity instructors** to safely deploy and supervise the RemoteAgentFramework in educational environments.

## ⚠️ MANDATORY INSTRUCTOR SUPERVISION REQUIREMENTS

### Critical Safety Responsibilities
- [ ] **Qualified instructor supervision** is required at all times during framework operation
- [ ] **Continuous monitoring** of student activities and system behavior
- [ ] **Immediate intervention** capability to stop any concerning activities
- [ ] **Educational oversight** to ensure proper learning objectives are met
- [ ] **Safety enforcement** of VM isolation and security protocols

### Instructor Qualifications Required
- Professional cybersecurity experience (minimum 2 years)
- Understanding of network security principles
- Experience with virtualization and isolation technologies
- Knowledge of educational safety protocols
- Familiarity with incident response procedures

## 🔒 Pre-Class Safety Checklist

### Mandatory Requirements
- [ ] **Legal approval** obtained from institution
- [ ] **IT security team** notified and approved setup
- [ ] **Isolated lab environment** prepared (no internet access)
- [ ] **Student safety briefing** materials prepared
- [ ] **Emergency procedures** documented
- [ ] **Qualified instructor supervision** confirmed and scheduled

## 🔧 Instructor Setup (30 minutes)

### Step 1: Environment Preparation
```bash
# 1. Verify network isolation
./verify-safety.sh

# 2. Quick setup all components
cd SE-335-01_agent_client && poetry install && cd ..
cd SE-335-01_agent-controller-service && ./mvnw clean install && cd ..
cd SE-335-01_agent_controller_dashboard && npm install && cd ..

# 3. Run safety tests
cd SE-335-01_agent_client
python -m pytest tests/test_security_compliance.py -v
```

### Step 2: Demo Preparation
```bash
# Start services for demonstration
# Terminal 1: Controller Service
cd SE-335-01_agent-controller-service
./mvnw spring-boot:run

# Terminal 2: Dashboard  
cd SE-335-01_agent_controller_dashboard
npm run dev

# Terminal 3: Agent Client
cd SE-335-01_agent_client
python src/main.py
```

## 👨‍🏫 Class Structure (90-minute session)

### Introduction (15 minutes)
1. **Safety briefing** - Emphasize ethical use and legal boundaries
2. **Learning objectives** - What students will accomplish
3. **Environment overview** - Isolated lab setup explanation

### Demonstration (20 minutes)
1. **Show the dashboard** - Navigate through safe simulation interface
2. **Run agent simulation** - Execute safe cookie and file discovery demos
3. **Examine outputs** - Review simulation files and logs
4. **Highlight safety markers** - Point out "SAFE SIMULATION" indicators

### Hands-on Activities (45 minutes)

#### Activity 1: Attack Pattern Recognition (15 min)
```bash
# Students examine simulation outputs
ls -la ./lab_test_files/
cat ./outbox/mock_payload_*.json
```
**Learning Goal**: Understand how malware communicates and exfiltrates data

#### Activity 2: Detection Development (20 min)
```bash
# Students create detection rules
grep "SIMULATION" ./logs/*
python -c "
import json
with open('./outbox/mock_payload_123.json', 'r') as f:
    data = json.load(f)
    print('Detected C2 communication pattern:', data['original_payload'])
"
```
**Learning Goal**: Develop skills in identifying malicious behavior

#### Activity 3: Defense Implementation (10 min)
Review code that implements safety checks:
```python
# Example from websocket_service.py
if not url.startswith(("ws://localhost", "ws://127.0.0.1")):
    self.app._log_service.warn("SAFETY: Non-localhost connection blocked")
    url = "ws://localhost:8080"
```
**Learning Goal**: Understand how to implement security controls

### Wrap-up and Assessment (10 minutes)
1. **Knowledge check** - Quiz on attack patterns observed
2. **Defense discussion** - What countermeasures would students implement?
3. **Ethical reflection** - Discussion on responsible disclosure and legal boundaries

## 📝 Student Assignments

### Assignment 1: Attack Analysis Report
**Objective**: Analyze simulation outputs and identify attack patterns
**Deliverable**: 2-page report documenting observed techniques
**Rubric**: Pattern identification (40%), detection proposals (40%), writing quality (20%)

### Assignment 2: Detection Rule Development
**Objective**: Create detection rules for observed attack patterns
**Deliverable**: Code implementing detection logic with test cases
**Rubric**: Accuracy (50%), completeness (30%), code quality (20%)

### Assignment 3: Defense Strategy Proposal
**Objective**: Design comprehensive defense against demonstrated attacks
**Deliverable**: Defense architecture document with implementation plan
**Rubric**: Technical accuracy (40%), feasibility (30%), presentation (30%)

## 🛡️ Safety Monitoring

### During Class
- [ ] Monitor student activities for safety compliance
- [ ] Ensure no attempts to bypass safety mechanisms
- [ ] Watch for any real browser data access attempts
- [ ] Verify all outputs remain in simulation directories

### Red Flags to Watch For
- Students attempting to modify safety checks
- Requests to "make it work on real data"
- Attempts to access actual browser files
- Questions about bypassing network isolation

### Incident Response
If safety violations occur:
1. **Immediately stop** the problematic activity
2. **Remind students** of legal and ethical boundaries
3. **Document** the incident for institutional records
4. **Contact IT security** if safety mechanisms were bypassed

## 📊 Assessment Rubrics

### Technical Understanding (40%)
- Can identify attack patterns in simulation data
- Understands C2 communication mechanisms
- Recognizes data exfiltration techniques
- Knows common detection approaches

### Safety Awareness (30%)
- Demonstrates understanding of legal boundaries
- Shows awareness of ethical considerations
- Maintains safety protocols throughout activities
- Articulates responsible disclosure principles

### Practical Skills (30%)
- Can implement basic detection rules
- Demonstrates defensive thinking
- Proposes viable countermeasures
- Shows system administration awareness

## 🔄 Troubleshooting Common Issues

### "Students want to test on real data"
**Response**: Explain that real data testing would violate laws and institutional policy. Emphasize that simulation data teaches the same concepts safely.

### "The simulation seems unrealistic"
**Response**: Point out that simplification is intentional for educational purposes. Real malware would be more sophisticated but use similar fundamental techniques.

### "Can we make it more advanced?"
**Response**: Advanced features can be discussed theoretically, but implementation should maintain safety boundaries. Focus on understanding principles rather than capability.

## 📚 Extension Activities

### Advanced Students
- Implement additional safety checks
- Create more sophisticated detection algorithms
- Design incident response procedures
- Research real-world case studies

### Struggling Students
- Focus on pattern recognition exercises
- Provide additional guided walkthroughs
- Offer simplified detection examples
- Pair with stronger students for peer learning

## 📞 Support Resources

### Technical Issues
- GitHub Issues for bug reports
- Documentation in component READMEs
- Community discussions for setup help

### Educational Support
- Instructor community forums
- Additional exercise materials
- Assessment template library

### Emergency Contacts
- **IT Security**: [your-it-security@institution.edu]
- **Legal Compliance**: [legal@institution.edu]
- **Project Maintainer**: [maintainer@institution.edu]

---

**Remember**: This is educational simulation software. Always prioritize safety, legality, and ethical use in all classroom activities.