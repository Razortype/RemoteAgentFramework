#!/bin/bash

# RemoteAgentFramework - Simple Publication Test
# Educational cybersecurity simulation framework

echo "🎓 RemoteAgentFramework Publication Test"
echo "========================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASS=0
FAIL=0

check() {
    local test_name="$1"
    local test_cmd="$2"
    
    echo -n "Testing $test_name... "
    
    if eval "$test_cmd" >/dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}"
        PASS=$((PASS + 1))
    else
        echo -e "${RED}❌ FAIL${NC}"
        FAIL=$((FAIL + 1))
    fi
}

echo "🔍 Essential Files"
check "README.md" "[ -f README.md ] && [ $(wc -l < README.md) -gt 300 ]"
check "LICENSE" "[ -f LICENSE ] && grep -q 'Educational' LICENSE"
check "Docker setup" "[ -f docker-compose.yml ] && docker-compose config >/dev/null 2>&1"
check "Documentation" "[ -f ARCHITECTURE.md ] && [ -f DEPLOYMENT.md ] && [ -f INSTRUCTOR_GUIDE.md ]"

echo ""
echo "🔒 Educational Safety"
check "Educational disclaimers" "grep -q 'EDUCATIONAL USE ONLY' README.md"
check "VM isolation requirements" "grep -q 'VM.*isolation' README.md || grep -q 'VM.*isolation' DEPLOYMENT.md"
check "Instructor supervision" "grep -q 'instructor.*supervision' INSTRUCTOR_GUIDE.md"
check "Localhost-only network" "grep -q '127.0.0.1' docker-compose.yml"

echo ""
echo "🛡️ Security & Dependencies"
check "Safe dependencies" "! grep -q 'browser-cookie3' SE-335-01_agent_client/pyproject.toml"
check "Educational data generation" "grep -q 'faker' SE-335-01_agent_client/pyproject.toml"
check "Component structure" "[ -d SE-335-01_agent_client ] && [ -d SE-335-01_agent-controller-service ] && [ -d SE-335-01_agent_controller_dashboard ]"

echo ""
echo "📊 Results"
echo "=========="
TOTAL=$((PASS + FAIL))
RATE=$(( (PASS * 100) / TOTAL ))

echo "Passed: $PASS"
echo "Failed: $FAIL"
echo "Success Rate: ${RATE}%"
echo ""

if [ $FAIL -eq 0 ] && [ $RATE -ge 90 ]; then
    echo -e "${GREEN}✅ READY FOR PUBLICATION!${NC}"
    echo ""
    echo "Your RemoteAgentFramework is ready to share with:"
    echo "  • Educational institutions"
    echo "  • Qualified cybersecurity instructors"
    echo "  • VM-isolated environments"
    echo ""
    echo "🔒 Remember: VM isolation and instructor supervision are mandatory!"
elif [ $RATE -ge 70 ]; then
    echo -e "${YELLOW}⚠️  MOSTLY READY - REVIEW FAILED ITEMS${NC}"
    echo "Address the failed tests, then you're good to go!"
else
    echo -e "${RED}❌ NOT READY - NEEDS WORK${NC}"
    echo "Please fix the failed tests before sharing."
fi

echo ""
echo "📖 For sharing guidance, see INSTRUCTOR_GUIDE.md"
echo "🚀 For setup instructions, see DEPLOYMENT.md"
echo "🔒 For detailed safety verification, run: ./verify-educational-safety.sh"

exit $FAIL