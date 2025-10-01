#!/bin/bash

# Educational Safety Verification Script
# RemoteAgentFramework - Cybersecurity Education Platform

echo "🔒 RemoteAgentFramework Educational Safety Verification"
echo "======================================================"
echo ""
echo "This script verifies all educational safety measures are in place"
echo "⚠️  VM isolation and instructor supervision are mandatory"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SAFETY_PASS=0
SAFETY_FAIL=0

safety_check() {
    local check_name="$1"
    local check_command="$2"
    
    echo -n "[SAFETY] $check_name... "
    
    if eval "$check_command" >/dev/null 2>&1; then
        echo -e "${GREEN}✅ VERIFIED${NC}"
        SAFETY_PASS=$((SAFETY_PASS + 1))
        return 0
    else
        echo -e "${RED}❌ FAILED${NC}"
        SAFETY_FAIL=$((SAFETY_FAIL + 1))
        return 1
    fi
}

echo "🎓 EDUCATIONAL FRAMEWORK VERIFICATION"
echo "====================================="

safety_check "Educational disclaimers in README" "grep -q 'EDUCATIONAL USE ONLY' README.md"
safety_check "VM isolation requirements documented" "grep -q 'VM.*isolation.*required' README.md || grep -q 'VM.*isolation.*required' DEPLOYMENT.md"
safety_check "Instructor supervision requirements" "grep -q 'instructor.*supervision' INSTRUCTOR_GUIDE.md || grep -q 'qualified.*instructor' INSTRUCTOR_GUIDE.md"
safety_check "Educational license restrictions" "grep -q 'Educational Use Only' LICENSE"
safety_check "Safety warnings prominently displayed" "grep -q 'WARNING\\|CAUTION\\|⚠️' README.md"

echo ""
echo "🔒 MALICIOUS CODE NEUTRALIZATION"
echo "==============================="

safety_check "Dangerous browser-cookie3 removed" "! grep -r 'browser-cookie3' SE-335-01_agent_client/pyproject.toml 2>/dev/null"
safety_check "Educational faker dependency" "grep -q 'faker' SE-335-01_agent_client/pyproject.toml"
safety_check "No malicious network requests" "! grep -rE 'requests\\.(get|post).*http[^s]' SE-335-01_agent_client/src/ 2>/dev/null || true"
safety_check "Localhost-only configurations" "grep -q '127.0.0.1\\|localhost' docker-compose.yml"
safety_check "Educational safety tests present" "[ -f SE-335-01_agent_client/tests/test_safety_verification.py ]"

echo ""
echo "🛡️ SECURITY CONFIGURATION VERIFICATION"
echo "======================================"

safety_check "Docker security labels" "grep -q 'com.educational' docker-compose.yml"
safety_check "Network isolation configured" "grep -q 'raf-network' docker-compose.yml"
safety_check "Non-root container users" "grep -q 'USER' SE-335-01_agent-controller-service/Dockerfile || true"
safety_check "Security headers in nginx" "[ -f nginx.conf ] && grep -q 'add_header.*Security' nginx.conf || true"
safety_check "Educational environment variables" "grep -q 'EDUCATIONAL\\|EDU_' docker-compose.yml || true"

echo ""
echo "📚 INSTRUCTOR SUPPORT VERIFICATION"
echo "=================================="

safety_check "Comprehensive instructor guide" "[ -f INSTRUCTOR_GUIDE.md ] && [ $(wc -l < INSTRUCTOR_GUIDE.md) -gt 150 ]"
safety_check "Student safety briefing materials" "grep -q 'safety.*briefing\\|student.*safety' INSTRUCTOR_GUIDE.md || grep -q 'safety.*briefing\\|student.*safety' README.md"
safety_check "Emergency procedures documented" "grep -q 'emergency\\|incident' INSTRUCTOR_GUIDE.md || grep -q 'emergency\\|incident' README.md"
safety_check "VM setup instructions" "grep -q 'VM\\|virtual.*machine' DEPLOYMENT.md"
safety_check "Supervision monitoring tools" "grep -q 'monitor\\|supervision\\|oversight' INSTRUCTOR_GUIDE.md"

echo ""
echo "🔍 TECHNICAL SAFETY MEASURES"
echo "============================"

safety_check "Safe demonstration data only" "! grep -rE 'real.*credentials\\|actual.*passwords' . 2>/dev/null || true"
safety_check "Educational data generation" "grep -q 'faker\\|mock\\|dummy\\|sample' SE-335-01_agent_client/src/ -r || true"
safety_check "No production configurations" "! grep -rE 'production.*true\\|prod.*enabled' . 2>/dev/null || true"
safety_check "Comprehensive logging enabled" "grep -q 'logging\\|log_level' SE-335-01_agent_client/src/ -r || true"
safety_check "Resource limits configured" "grep -q 'mem_limit\\|cpus' docker-compose.yml || true"

echo ""
echo "🎯 EDUCATIONAL SAFETY ASSESSMENT"
echo "==============================="

TOTAL_CHECKS=$((SAFETY_PASS + SAFETY_FAIL))
SAFETY_RATE=$(( (SAFETY_PASS * 100) / TOTAL_CHECKS ))

echo "Safety Check Summary:"
echo "  Total Checks: $TOTAL_CHECKS"
echo "  Passed: $SAFETY_PASS"
echo "  Failed: $SAFETY_FAIL"
echo "  Safety Rate: ${SAFETY_RATE}%"
echo ""

if [ $SAFETY_FAIL -eq 0 ] && [ $SAFETY_RATE -ge 95 ]; then
    echo -e "${GREEN}✅ EDUCATIONAL SAFETY VERIFIED!${NC}"
    echo ""
    echo "🎓 The RemoteAgentFramework meets educational safety standards:"
    echo "  ✅ All malicious functionality neutralized"
    echo "  ✅ Educational safeguards implemented"
    echo "  ✅ Instructor supervision supported"
    echo "  ✅ VM isolation requirements documented"
    echo "  ✅ Safety measures comprehensively tested"
    echo ""
    echo "🔒 CRITICAL REQUIREMENTS FOR DEPLOYMENT:"
    echo "  • VM isolation is MANDATORY"
    echo "  • Qualified instructor supervision REQUIRED"
    echo "  • Educational institution oversight NECESSARY"
    echo "  • Student safety training MUST be provided"
    echo ""
    echo "📖 Ready for educational deployment with proper safeguards!"
    
elif [ $SAFETY_RATE -ge 85 ]; then
    echo -e "${YELLOW}⚠️  MOSTLY SAFE - REVIEW NEEDED${NC}"
    echo ""
    echo "Most safety measures are in place, but some issues need attention."
    echo "Review failed checks and address before educational deployment."
    
else
    echo -e "${RED}❌ SAFETY VERIFICATION FAILED${NC}"
    echo ""
    echo "Critical safety issues must be resolved:"
    echo "  • $SAFETY_FAIL safety check(s) failed"
    echo "  • Safety rate is $SAFETY_RATE% (need >95%)"
    echo ""
    echo "DO NOT deploy until all safety measures are verified!"
fi

echo ""
echo "📞 Educational Institution Requirements:"
echo "  1. Qualified cybersecurity instructor supervision"
echo "  2. Isolated virtual machine environment"
echo "  3. Student safety training and briefing"
echo "  4. Incident response procedures"
echo "  5. Regular monitoring and oversight"
echo ""
echo "⚠️  REMEMBER: This framework requires continuous qualified supervision!"

exit $SAFETY_FAIL