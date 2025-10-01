"""
Security Compliance Tests
Verifies that all malicious functionality has been neutralized
"""

import unittest
import os
import sys
import importlib.util
import inspect
import ast
import subprocess

class SecurityComplianceTests(unittest.TestCase):
    """
    Critical tests to verify educational safety compliance
    These tests MUST pass before any publication
    """
    
    def setUp(self):
        self.src_path = "src"
        self.dangerous_patterns = [
            # Real browser access patterns
            "browser_cookie3.chrome()",
            "browser_cookie3.firefox()", 
            ".config/google-chrome",
            "Library/Application Support/Google/Chrome",
            "AppData/Local/Google/Chrome",
            
            # Real file system access
            "os.path.expanduser('~')",
            "home_dir = os.path.expanduser",
            "os.walk(directory)" ,
            
            # Real network communication
            "websocket.WebSocketApp",
            "ws://",
            "wss://",
            
            # Dangerous operations
            "subprocess.call",
            "os.system",
            "eval(",
            "exec(",
        ]
        
    def test_no_dangerous_imports(self):
        """Verify no dangerous libraries are imported"""
        dangerous_imports = [
            "browser_cookie3",
            "sqlite3", 
            "cryptography.hazmat",
            "subprocess",
        ]
        
        violations = []
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        for dangerous_import in dangerous_imports:
                            if f"import {dangerous_import}" in content or f"from {dangerous_import}" in content:
                                # Check if it's commented out as a safe simulation marker
                                if "# SAFE SIMULATION" not in content or "# REMOVED" not in content:
                                    violations.append(f"{filepath}: {dangerous_import}")
        
        self.assertEqual([], violations, f"Dangerous imports found: {violations}")
    
    def test_no_real_browser_access(self):
        """Verify no real browser data access exists"""
        violations = []
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        
                        # Check for browser path access
                        browser_paths = [
                            "Google/Chrome/User Data",
                            "Mozilla/Firefox/Profiles",
                            ".config/google-chrome",
                            ".mozilla/firefox"
                        ]
                        
                        for path in browser_paths:
                            if path in content and "SAFE SIMULATION" not in content:
                                violations.append(f"{filepath}: Real browser path access - {path}")
        
        self.assertEqual([], violations, f"Real browser access found: {violations}")
    
    def test_localhost_only_connections(self):
        """Verify all network connections are localhost-only"""
        violations = []
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        
                        # Look for external URLs
                        if "ws://" in content or "wss://" in content or "http://" in content or "https://" in content:
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if any(protocol in line for protocol in ["ws://", "wss://", "http://", "https://"]):
                                    if not any(host in line for host in ["localhost", "127.0.0.1"]):
                                        if "SAFE SIMULATION" not in line and "example" not in line:
                                            violations.append(f"{filepath}:{i+1}: Non-localhost URL - {line.strip()}")
        
        self.assertEqual([], violations, f"External network access found: {violations}")
    
    def test_safe_simulation_markers(self):
        """Verify all attack files have safety markers"""
        attack_files = []
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if 'attack' in file.lower() and file.endswith('.py'):
                    attack_files.append(os.path.join(root, file))
        
        missing_markers = []
        for filepath in attack_files:
            with open(filepath, 'r') as f:
                content = f.read()
                if "SAFE SIMULATION" not in content:
                    missing_markers.append(filepath)
        
        self.assertEqual([], missing_markers, f"Attack files missing safety markers: {missing_markers}")
    
    def test_no_hardcoded_secrets(self):
        """Verify no hardcoded secrets or credentials"""
        violations = []
        secret_patterns = [
            "password=",
            "secret=", 
            "token=",
            "key=",
            "api_key=",
            "auth_token=",
        ]
        
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            for pattern in secret_patterns:
                                if pattern in line.lower():
                                    # Allow if it's obviously a placeholder or demo
                                    if not any(placeholder in line.lower() for placeholder in 
                                             ["demo", "test", "example", "placeholder", "fake", "sim_"]):
                                        violations.append(f"{filepath}:{i+1}: Potential secret - {line.strip()}")
        
        self.assertEqual([], violations, f"Potential hardcoded secrets found: {violations}")
    
    def test_file_operations_safe(self):
        """Verify file operations only access test directories"""
        violations = []
        for root, dirs, files in os.walk(self.src_path):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        
                        # Check for dangerous file operations
                        if "os.walk(" in content:
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if "os.walk(" in line:
                                    # Should only walk test directories
                                    if "lab_test_files" not in content:
                                        violations.append(f"{filepath}:{i+1}: Unsafe os.walk usage")
        
        self.assertEqual([], violations, f"Unsafe file operations found: {violations}")
    
    def test_simulation_directories_only(self):
        """Verify only safe test directories are used"""
        from module.attacker_module.attacks.custom_attack import FileFolderDiscoveryAttack
        from unittest.mock import Mock
        
        attack = FileFolderDiscoveryAttack(Mock(), Mock())
        test_dirs = attack._create_safe_test_directories()
        
        for directory in test_dirs:
            self.assertTrue(directory.startswith("./lab_test_files/"), 
                          f"Unsafe directory created: {directory}")
    
    def test_websocket_safety(self):
        """Verify WebSocket service safety"""
        from service.websocket_service import WebSocketClientSevice
        from unittest.mock import Mock
        
        mock_app = Mock()
        mock_app._log_service = Mock()
        
        # Test that external URLs are blocked
        service = WebSocketClientSevice(mock_app, "ws://malicious.com", "/evil")
        self.assertTrue(service.url.startswith("ws://localhost"), 
                       "External WebSocket URL not blocked")
    
    def test_cookie_attack_safety(self):
        """Verify cookie attack uses only fake data"""
        from module.attacker_module.attacks.custom_attack import CookieAttack
        from unittest.mock import Mock
        
        attack = CookieAttack(Mock(), Mock())
        fake_cookies = attack._generate_fake_browser_session()
        
        for cookie in fake_cookies:
            self.assertIn('sim_', cookie['value'], "Cookie value not marked as simulation")
            self.assertIn('example-lab.com', cookie['domain'], "Cookie domain not safe test domain")
    
    def test_no_real_execution_methods(self):
        """Verify no dangerous execution methods exist"""
        dangerous_methods = [
            "_extract_chrome_cookies",
            "_extract_firefox_cookies", 
            "_get_chrome_secret",
            "_decrypt_cookie_value",
            "_fetch_cookies_from_sqlite"
        ]
        
        from module.attacker_module.attacks.custom_attack import CookieAttack
        from unittest.mock import Mock
        
        attack = CookieAttack(Mock(), Mock())
        
        missing_methods = []
        for method in dangerous_methods:
            if hasattr(attack, method):
                missing_methods.append(method)
        
        self.assertEqual([], missing_methods, f"Dangerous methods still exist: {missing_methods}")

if __name__ == '__main__':
    print("=" * 60)
    print("SECURITY COMPLIANCE VERIFICATION")
    print("These tests verify that malicious functionality has been neutralized")
    print("ALL TESTS MUST PASS before publication")
    print("=" * 60)
    
    # Run tests with detailed output
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 60)
    print("SECURITY COMPLIANCE CHECK COMPLETE")
    print("If all tests passed, basic safety requirements are met.")
    print("REMINDER: Additional legal and security review still required!")
    print("=" * 60)