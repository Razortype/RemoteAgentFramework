# Contributing to Cybersecurity Education Lab

## 🔒 Security-First Contribution Policy

This project is an **educational cybersecurity simulation** with strict safety requirements. All dangerous functionality has been neutralized and replaced with safe demonstrations.

### ⚠️ Critical Rules for Contributors

1. **NO MALICIOUS CODE**: Contributions that restore dangerous functionality will be rejected
2. **EDUCATIONAL ONLY**: All code must serve legitimate educational purposes
3. **SAFETY VERIFICATION**: All PRs require security review before merge
4. **LEGAL COMPLIANCE**: Contributors must comply with all applicable laws

## 🎯 Acceptable Contribution Types

### ✅ Welcome Contributions
- **Safe Simulations**: Additional educational demonstrations using fake data
- **Detection Tools**: Code that identifies attack patterns
- **Educational Content**: Documentation, tutorials, learning exercises
- **Security Hardening**: Improvements to prevent misuse
- **Test Coverage**: Unit tests verifying safe operation
- **Defense Mechanisms**: Code demonstrating protection techniques

### ❌ Prohibited Contributions
- Real browser cookie extraction
- Actual file system exploitation
- Live C2 communication capabilities
- Credential theft mechanisms
- Network exploitation tools
- Encryption bypass techniques
- Authentication circumvention
- Data exfiltration implementations

## 📋 Contribution Process

### 1. Pre-Contribution Checklist
- [ ] Contribution serves legitimate educational purpose
- [ ] No real user data is accessed
- [ ] All functionality is clearly marked as simulation
- [ ] Code includes appropriate safety checks
- [ ] Documentation explains educational value

### 2. Development Guidelines

#### Code Safety Requirements
```python
# ✅ GOOD: Safe simulation
def generate_fake_browser_session():
    return [{
        'name': 'sim_session',
        'value': f'sim_{uuid.uuid4().hex}',
        'domain': 'example-lab.com'
    }]

# ❌ BAD: Real data access (will be rejected)
def extract_real_cookies():
    return browser_cookie3.chrome()  # NEVER DO THIS
```

#### Required Safety Markers
All simulation code must include:
```python
# SAFE SIMULATION: Description of educational purpose
# EDUCATIONAL: What students learn from this
# WARNING: Clarification that this is not real
```

#### Mandatory Safety Checks
```python
def safe_file_operation(file_path):
    # Safety check: only allow test directories
    if not file_path.startswith("./lab_test_files/"):
        raise SecurityError("Attempted access outside safe test area")
    # ... safe operation only
```

### 3. Pull Request Requirements

#### PR Template
```markdown
## Educational Purpose
Describe what cybersecurity concept this teaches

## Safety Verification
- [ ] No real user data accessed
- [ ] Only localhost connections used
- [ ] All outputs clearly marked as simulation
- [ ] Includes safety checks to prevent misuse
- [ ] Added appropriate tests

## Testing
- [ ] All tests pass in isolated VM
- [ ] No network connections required
- [ ] Simulation produces expected safe outputs

## Documentation
- [ ] Added or updated educational documentation
- [ ] Included example usage
- [ ] Described learning objectives
```

#### Required Reviews
- **Security Review**: All PRs require security team approval
- **Educational Review**: Content must serve clear learning objectives
- **Legal Review**: For any significant changes to licensing or usage

### 4. Testing Standards

#### Safe Testing Environment
- **VM Only**: All testing must occur in isolated virtual machines
- **No Internet**: Test environment must have no network access
- **Safe Data**: Only test/fake data may be used
- **Cleanup**: Tests must clean up all generated files

#### Required Test Categories
```python
class TestSafety(unittest.TestCase):
    def test_no_real_data_access(self):
        """Verify no real user data is accessed"""
        
    def test_localhost_only_connections(self):
        """Verify only localhost connections are made"""
        
    def test_simulation_markers_present(self):
        """Verify all outputs marked as simulation"""
```

## 🔍 Code Review Process

### Security Review Checklist
- [ ] No access to real browser data
- [ ] No network connections outside localhost
- [ ] All file operations limited to test directories
- [ ] Appropriate safety checks implemented
- [ ] Clear simulation markers present
- [ ] Educational value clearly documented

### Automatic Security Scans
All PRs are automatically scanned for:
- Hardcoded secrets or credentials
- Dangerous library imports
- Real data access patterns
- Network communication code
- File system manipulation outside test areas

## 🚫 Reporting Security Issues

### If You Find Dangerous Code
1. **DO NOT** create a public issue
2. **DO NOT** attempt to exploit the vulnerability
3. Email security@[project-domain] immediately
4. Provide detailed steps to reproduce
5. Suggest safe remediation approach

### Responsible Disclosure Timeline
- **Day 0**: Report received, acknowledgment sent
- **Day 1-7**: Initial assessment and triage
- **Day 7-30**: Development of fix and testing
- **Day 30**: Public disclosure (if appropriate)

## 📚 Educational Standards

### Learning Objective Requirements
All contributions must clearly state:
- What cybersecurity concept is demonstrated
- What students will learn
- How this relates to real-world security
- What defensive measures are appropriate

### Documentation Standards
- Clear explanations suitable for students
- Step-by-step instructions for safe usage
- Warnings about prohibited activities
- References to relevant security frameworks

## 🏆 Recognition

### Contributor Types
- **Safety Champions**: Contributors who improve security safeguards
- **Education Leaders**: Contributors who enhance learning content
- **Detection Experts**: Contributors who build defense mechanisms

### Hall of Fame
We recognize contributors who:
- Identify and fix security issues
- Create outstanding educational content
- Develop innovative safe simulations
- Improve project safety standards

## 📞 Getting Help

### Contact Methods
- **General Questions**: GitHub Discussions
- **Security Concerns**: security@[project-domain]
- **Educational Support**: education@[project-domain]
- **Technical Issues**: GitHub Issues

### Community Guidelines
- Be respectful and professional
- Focus on educational value
- Prioritize safety above all else
- Share knowledge responsibly

---

**Remember**: This project exists to teach defensive cybersecurity. Help us maintain the highest standards of safety and educational value.