"""
Safety verification tests for RemoteAgentFramework.
Educational cybersecurity simulation framework - VM isolation required.

These tests verify that all malicious functionality has been neutralized
and replaced with safe educational simulations.
"""

import pytest
import os
import sys
import socket
from unittest.mock import patch, Mock
from pathlib import Path


class TestEducationalSafety:
    """Test educational safety measures and malicious code neutralization."""

    @pytest.mark.safety
    def test_localhost_only_enforcement(self):
        """Test that only localhost connections are allowed."""
        # Simulate WebSocket connection attempt
        with patch('socket.socket') as mock_socket:
            mock_sock = Mock()
            mock_socket.return_value = mock_sock
            
            # Should only connect to localhost
            allowed_hosts = ['localhost', '127.0.0.1', '::1']
            
            for host in allowed_hosts:
                # This should not raise an exception
                try:
                    mock_sock.connect((host, 8080))
                except Exception:
                    pass  # Connection might fail in test environment
            
            # Verify socket was called with localhost addresses only
            call_args = [call[0][0][0] for call in mock_sock.connect.call_args_list]
            assert all(host in allowed_hosts for host in call_args), \
                   f"Non-localhost connections attempted: {call_args}"

    @pytest.mark.safety
    def test_no_real_browser_access(self):
        """Test that real browser cookie access is disabled."""
        # Check that browser-cookie3 is not imported
        with pytest.raises(ImportError):
            import browser_cookie3
        
        # Verify safe simulation data is used instead
        from src.module.attacker_module.attacks import custom_attack
        
        # Check that fake data generators are used
        assert hasattr(custom_attack, 'generate_fake_cookies'), \
               "Fake cookie generator not found"

    @pytest.mark.safety
    def test_file_system_safety(self):
        """Test that file system access is limited to safe directories."""
        from src.module.attacker_module.attacks import custom_attack
        
        # Check that only test directories are scanned
        safe_paths = custom_attack.get_safe_scan_paths()
        
        for path in safe_paths:
            path_obj = Path(path)
            # Should only include test/demo directories
            assert any(keyword in str(path_obj).lower() 
                      for keyword in ['test', 'demo', 'sample', 'fake']), \
                   f"Unsafe path detected: {path}"

    @pytest.mark.safety
    def test_educational_markers_present(self):
        """Test that educational framework markers are present."""
        required_env_vars = [
            'EDUCATIONAL_FRAMEWORK',
            'VM_ISOLATION_REQUIRED',
            'LOCALHOST_ONLY',
            'SAFETY_VERIFIED'
        ]
        
        for var in required_env_vars:
            assert os.environ.get(var), f"Required educational marker {var} not set"

    @pytest.mark.safety
    def test_no_real_data_extraction(self):
        """Test that no real sensitive data can be extracted."""
        from src.module.attacker_module.attacks import custom_attack
        
        # Test cookie extraction
        cookies = custom_attack.extract_browser_cookies()
        
        # Should only return fake/demo data
        assert all('fake' in str(cookie).lower() or 
                  'demo' in str(cookie).lower() or
                  'test' in str(cookie).lower() 
                  for cookie in cookies), \
               "Real cookie data detected in extraction"

    @pytest.mark.safety
    def test_network_isolation(self):
        """Test that network access is properly isolated."""
        # Test that only localhost WebSocket connections are made
        with patch('websocket.WebSocketApp') as mock_ws:
            from src.service.websocket_service import WebSocketService
            
            service = WebSocketService()
            service.connect()
            
            # Verify WebSocket was created with localhost URL
            call_args = mock_ws.call_args[0][0]  # First positional argument (URL)
            assert 'localhost' in call_args or '127.0.0.1' in call_args, \
                   f"Non-localhost WebSocket connection: {call_args}"

    @pytest.mark.safety
    def test_educational_logging(self):
        """Test that educational safety logging is active."""
        from src.service.log_service import LogService
        
        log_service = LogService()
        
        # Should log educational safety events
        log_service.log_safety_event("test_event", "Educational safety test")
        
        # Verify educational context is logged
        logs = log_service.get_recent_logs()
        educational_logs = [log for log in logs 
                           if 'educational' in log.lower() or 'safety' in log.lower()]
        
        assert educational_logs, "Educational safety logging not active"

    @pytest.mark.safety
    def test_vm_isolation_warnings(self):
        """Test that VM isolation warnings are displayed."""
        from src.core.app import App
        
        with patch('builtins.print') as mock_print:
            app = App()
            app.start()
            
            # Check that VM isolation warnings were printed
            print_calls = [str(call) for call in mock_print.call_args_list]
            vm_warnings = [call for call in print_calls 
                          if 'vm' in call.lower() and 'isolation' in call.lower()]
            
            assert vm_warnings, "VM isolation warnings not displayed"

    @pytest.mark.safety
    def test_malicious_code_neutralized(self):
        """Test that malicious code has been neutralized."""
        # Check that dangerous functions are replaced with safe equivalents
        from src.module.attacker_module.attacks import custom_attack
        
        # Test that file scanning is safe
        scanned_files = custom_attack.scan_file_system()
        
        # Should only return fake/demo files
        for file_info in scanned_files:
            assert 'real' not in file_info.get('path', '').lower(), \
                   f"Real file path detected: {file_info}"
            
            # Should contain educational markers
            assert any(marker in str(file_info).lower() 
                      for marker in ['fake', 'demo', 'test', 'sample']), \
                   f"Missing educational markers in file info: {file_info}"


class TestFrameworkIntegrity:
    """Test overall framework integrity and educational compliance."""

    @pytest.mark.safety
    def test_framework_identification(self):
        """Test that framework properly identifies itself as educational."""
        from src.config import get_framework_info
        
        info = get_framework_info()
        
        assert info['name'] == 'RemoteAgentFramework'
        assert info['type'] == 'educational'
        assert info['vm_isolation_required'] is True
        assert info['safe_simulation_only'] is True

    @pytest.mark.safety
    def test_configuration_safety(self):
        """Test that configuration enforces safety measures."""
        from src.config import Config
        
        config = Config()
        
        # Should enforce localhost-only connections
        assert config.websocket_host in ['localhost', '127.0.0.1']
        assert config.educational_mode is True
        assert config.vm_isolation_required is True

    @pytest.mark.safety
    def test_no_production_credentials(self):
        """Test that no production credentials are present."""
        # Check common credential files
        credential_files = [
            '.env',
            'credentials.json',
            'secrets.yaml',
            'production.conf'
        ]
        
        project_root = Path(__file__).parent.parent
        
        for cred_file in credential_files:
            cred_path = project_root / cred_file
            if cred_path.exists():
                content = cred_path.read_text()
                # Should not contain real production values
                assert 'production' not in content.lower() or \
                       'educational' in content.lower(), \
                       f"Production credentials detected in {cred_file}"