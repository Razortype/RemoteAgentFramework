import os
import time
import json
import platform
import uuid
from datetime import datetime, timedelta

# SAFE SIMULATION: Removed real browser cookie extraction libraries
# import browser_cookie3  # REMOVED - was used for actual cookie theft
# import sqlite3  # REMOVED - was used to access browser databases
# from cryptography import *  # REMOVED - was used to decrypt stolen cookies

from module.attacker_module.attacks.base_attack import Attack

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module.attacker_module.attack_executor import AttackExecutor
    from module.message_handler.messages.payloads.attack_payload import AttackPayload

class CookieAttack(Attack):
    
    def __init__(self, executor: "AttackExecutor", attack_payload: "AttackPayload") -> None:
        super().__init__(executor, attack_payload)

        self.important_cookie_names = {
            'sessionid',  # Generic session identifier
            'userid',  # Generic user identifier
            'username',  # User's name
            'csrftoken',  # Cross-Site Request Forgery prevention token
            'auth_token',  # Authentication token
            'access_token',  # Access token for OAuth 2.0
            'refresh_token',  # Refresh token for OAuth 2.0
            'sid',  # Session ID
            'connect.sid',  # Session ID used by some frameworks
            'JSESSIONID',  # Java J2EE session identifier
            'ASP.NET_SessionId',  # ASP.NET session identifier
            '__cfduid',  # Cloudflare service token
            '_ga',  # Google Analytics
            '_gid',  # Google Analytics
            '_gat',  # Google Analytics
        }

    def job(self):
        # SAFE SIMULATION: Replaced malicious cookie extraction with educational simulation
        self.info("Cookie Discovery Simulation initiating...")
        self.info("EDUCATIONAL PURPOSE: This demonstrates how malware might attempt cookie access")
        self.info("WARNING: This simulation uses fake data only - no real cookies are accessed")
        
        # Generate fake browser data for educational purposes
        fake_cookies = self._generate_fake_browser_session()
        
        self.info("Simulated browser detection complete")
        for cookie in fake_cookies:
            if cookie['name'] in self.important_cookie_names:
                self.log_data(f"SIMULATION: Cookie [Name]: {cookie['name']} [Value]: {cookie['value']}")
            else:
                self.info(f"SIMULATION: Cookie [Name]: {cookie['name']} [Value]: {cookie['value']}")

        self.info("Cookie discovery simulation completed safely.")
        self.info("REMINDER: This was a simulation - no real data was accessed")

    def _generate_fake_browser_session(self):
        """
        SAFE SIMULATION: Generates fake cookie data for educational demonstration
        This replaces the dangerous real cookie extraction functionality
        """
        # Generate deterministic fake cookies for educational purposes
        fake_cookies = [
            {
                'name': 'sessionid',
                'value': f'sim_{uuid.uuid4().hex[:16]}',
                'domain': 'example-lab.com',
                'path': '/'
            },
            {
                'name': 'csrftoken', 
                'value': f'sim_csrf_{uuid.uuid4().hex[:24]}',
                'domain': 'example-lab.com',
                'path': '/'
            },
            {
                'name': '_ga',
                'value': f'GA1.1.{int(time.time())}.{uuid.uuid4().hex[:8]}',
                'domain': '.example-lab.com',
                'path': '/'
            },
            {
                'name': 'auth_token',
                'value': f'sim_auth_{uuid.uuid4().hex[:32]}',
                'domain': 'secure.example-lab.com',
                'path': '/admin'
            }
        ]
        
        self.info(f"Generated {len(fake_cookies)} simulated cookies for educational demonstration")
        return fake_cookies

    # SAFE SIMULATION: Removed dangerous browser detection and cookie extraction methods
    # The following methods have been removed as they implemented real malware functionality:
    # - _detect_browser() - scanned for real browser installations
    # - _extract_chrome_cookies() - accessed real Chrome cookie database
    # - _extract_firefox_cookies() - accessed real Firefox cookie database
    # - _get_chrome_secret() - extracted real Chrome encryption keys
    # - _decrypt_cookie_value() - decrypted real stolen cookies
    # - _fetch_cookies_from_sqlite() - accessed real browser SQLite databases
    
    def _create_safe_test_environment(self):
        """
        SAFE SIMULATION: Creates a test environment for educational purposes
        This replaces dangerous file system access with controlled test data
        """
        test_dir = "./lab_test_files/browser_simulation"
        os.makedirs(test_dir, exist_ok=True)
        
        # Create sample files for educational demonstration
        with open(f"{test_dir}/sample_cookies.json", "w") as f:
            json.dump({
                "notice": "This is simulated data for educational purposes only",
                "cookies": self._generate_fake_browser_session()
            }, f, indent=2)
        
        self.info(f"Created safe test environment at: {test_dir}")
        return test_dir


class FileFolderDiscoveryAttack(Attack):
    
    def __init__(self, executor: "AttackExecutor", attack_payload: "AttackPayload") -> None:
        super().__init__(executor, attack_payload)

    def job(self):
        # SAFE SIMULATION: Replaced malicious file discovery with educational simulation
        self.info("File Discovery Simulation initiating...")
        self.info("EDUCATIONAL PURPOSE: This demonstrates how malware might scan for files")
        self.info("WARNING: This simulation only accesses test files - no real user data")
        
        # Only work with safe test directory
        test_directories = self._create_safe_test_directories()
        
        for directory in test_directories:
            self._simulate_file_discovery(directory)
        
        self.info("File discovery simulation completed safely.")
        self.info("REMINDER: This was a simulation - no real user files were accessed")

    def _create_safe_test_directories(self):
        """
        SAFE SIMULATION: Creates controlled test directories instead of accessing real user folders
        """
        base_test_dir = "./lab_test_files/file_discovery_simulation"
        test_dirs = [
            f"{base_test_dir}/test_documents",
            f"{base_test_dir}/test_downloads", 
            f"{base_test_dir}/test_pictures"
        ]
        
        for dir_path in test_dirs:
            os.makedirs(dir_path, exist_ok=True)
            
            # Create safe sample files for educational demonstration
            sample_files = [
                "sample_document.txt",
                "test_report.pdf", 
                "demo_spreadsheet.xlsx",
                "example_image.jpg"
            ]
            
            for filename in sample_files:
                file_path = os.path.join(dir_path, filename)
                with open(file_path, "w") as f:
                    f.write(f"SIMULATION FILE - Created for educational purposes only.\n")
                    f.write(f"This demonstrates file discovery concepts safely.\n")
                    f.write(f"Created: {datetime.now().isoformat()}\n")
        
        self.info(f"Created {len(test_dirs)} safe test directories with sample files")
        return test_dirs

    def _simulate_file_discovery(self, directory):
        """
        SAFE SIMULATION: Only scans test directories, never real user data
        """
        self.info(f"SIMULATION: Scanning test directory: {directory}")
        
        if not directory.startswith("./lab_test_files/"):
            self.error("SAFETY CHECK: Attempted to scan non-test directory - blocked!")
            return
        
        try:
            for root, dirs, files in os.walk(directory):
                for name in files:
                    file_path = os.path.join(root, name)
                    if self._is_simulation_target_file(file_path):
                        self._log_simulation_file_info(file_path)
        except Exception as e:
            self.error(f"Error scanning test directory: {directory} - {e}")

    def _is_simulation_target_file(self, file_path):
        """
        SAFE SIMULATION: Determines if a test file should be flagged for demonstration
        """
        target_extensions = {'.txt', '.pdf', '.xlsx', '.jpg', '.png', '.doc', '.docx'}
        _, ext = os.path.splitext(file_path)
        return ext.lower() in target_extensions

    def _log_simulation_file_info(self, file_path):
        """
        SAFE SIMULATION: Logs test file information for educational purposes
        """
        file_info = f"SIMULATION: Found test file: {file_path}"
        self.log_data(file_info)
        self.debug(f"Educational demo - logged: {file_info}")