"""
SAFE SIMULATION TESTS
Educational tests demonstrating cybersecurity concepts safely
"""

import unittest
import os
import json
import tempfile
import shutil
from unittest.mock import Mock, patch

# Test the safe simulation functionality
class TestSafeAttackSimulations(unittest.TestCase):
    
    def setUp(self):
        """Set up safe test environment"""
        self.test_dir = tempfile.mkdtemp(prefix="safe_test_")
        self.addCleanup(shutil.rmtree, self.test_dir)
        
    def test_safe_cookie_simulation(self):
        """Test that cookie simulation generates fake data only"""
        from module.attacker_module.attacks.custom_attack import CookieAttack
        
        # Mock executor and payload
        mock_executor = Mock()
        mock_payload = Mock()
        
        attack = CookieAttack(mock_executor, mock_payload)
        fake_cookies = attack._generate_fake_browser_session()
        
        # Verify all cookies are clearly simulated
        self.assertIsInstance(fake_cookies, list)
        self.assertTrue(len(fake_cookies) > 0)
        
        for cookie in fake_cookies:
            self.assertIn('sim_', cookie['value'])  # All values should be prefixed with sim_
            self.assertEqual(cookie['domain'], 'example-lab.com')  # Safe test domain
            
    def test_safe_file_discovery_simulation(self):
        """Test that file discovery only accesses test directories"""
        from module.attacker_module.attacks.custom_attack import FileFolderDiscoveryAttack
        
        # Mock executor and payload  
        mock_executor = Mock()
        mock_payload = Mock()
        
        attack = FileFolderDiscoveryAttack(mock_executor, mock_payload)
        test_dirs = attack._create_safe_test_directories()
        
        # Verify only safe test directories are created
        for test_dir in test_dirs:
            self.assertTrue(test_dir.startswith("./lab_test_files/"))
            self.assertTrue(os.path.exists(test_dir))
            
    def test_websocket_localhost_only(self):
        """Test that WebSocket service only allows localhost connections"""
        from service.websocket_service import WebSocketClientSevice
        
        mock_app = Mock()
        mock_app._log_service = Mock()
        
        # Test external URL gets blocked
        service = WebSocketClientSevice(mock_app, "ws://malicious-server.com", "/evil")
        self.assertTrue(service.url.startswith("ws://localhost"))
        
    def test_mock_c2_creates_local_files(self):
        """Test that C2 communication creates local files instead of network transmission"""
        from service.websocket_service import WebSocketClientSevice
        
        mock_app = Mock()
        mock_app._log_service = Mock()
        
        service = WebSocketClientSevice(mock_app, "ws://localhost:8080", "/test")
        service.setup_safe_simulation()
        
        # Test mock C2 send
        test_payload = {"test": "data"}
        filename = service.mock_c2_send(test_payload)
        
        self.assertTrue(os.path.exists(filename))
        
        with open(filename, 'r') as f:
            data = json.load(f)
            
        self.assertIn("EDUCATIONAL SIMULATION", data["notice"])
        self.assertEqual(data["original_payload"], test_payload)

    def test_no_real_browser_access(self):
        """Test that no real browser files are accessed"""
        from module.attacker_module.attacks.custom_attack import CookieAttack
        
        mock_executor = Mock()
        mock_payload = Mock()
        
        attack = CookieAttack(mock_executor, mock_payload)
        
        # Verify dangerous methods have been removed/disabled
        self.assertFalse(hasattr(attack, '_extract_chrome_cookies'))
        self.assertFalse(hasattr(attack, '_extract_firefox_cookies'))
        self.assertFalse(hasattr(attack, '_get_chrome_secret'))

if __name__ == '__main__':
    print("Running safe simulation tests...")
    print("These tests verify that malicious functionality has been neutralized")
    unittest.main()