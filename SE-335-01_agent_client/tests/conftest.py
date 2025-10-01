"""
Test configuration for RemoteAgentFramework Python client.
Educational cybersecurity simulation framework - VM isolation required.
"""

import pytest
import os
import tempfile
from unittest.mock import Mock, patch


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def mock_config():
    """Mock configuration for testing."""
    return {
        'websocket': {
            'host': 'localhost',
            'port': 8080,
            'ssl': False
        },
        'educational': {
            'framework': 'RemoteAgentFramework',
            'version': '1.0.0',
            'safety_verified': True,
            'vm_isolation_required': True
        },
        'logging': {
            'level': 'DEBUG',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    }


@pytest.fixture
def mock_websocket():
    """Mock WebSocket connection for testing."""
    with patch('websocket.WebSocketApp') as mock_ws:
        mock_instance = Mock()
        mock_ws.return_value = mock_instance
        yield mock_instance


@pytest.fixture
def educational_safety_check():
    """Verify educational safety measures are in place."""
    # Check that this is running in an educational context
    educational_markers = [
        'EDUCATIONAL',
        'FRAMEWORK',
        'VM_ISOLATION',
        'LOCALHOST'
    ]
    
    # This should be run in a controlled environment
    assert any(marker in os.environ.get('CI', '') or 
              marker in os.environ.get('EDUCATIONAL_FRAMEWORK', '') 
              for marker in educational_markers), \
           "Educational safety markers not found in environment"
    
    yield True


@pytest.fixture(scope="session", autouse=True)
def setup_educational_environment():
    """Setup educational environment variables for testing."""
    os.environ['EDUCATIONAL_FRAMEWORK'] = 'RemoteAgentFramework'
    os.environ['VM_ISOLATION_REQUIRED'] = 'true'
    os.environ['LOCALHOST_ONLY'] = 'true'
    os.environ['SAFETY_VERIFIED'] = 'true'
    
    yield
    
    # Cleanup after tests
    for key in ['EDUCATIONAL_FRAMEWORK', 'VM_ISOLATION_REQUIRED', 
                'LOCALHOST_ONLY', 'SAFETY_VERIFIED']:
        os.environ.pop(key, None)