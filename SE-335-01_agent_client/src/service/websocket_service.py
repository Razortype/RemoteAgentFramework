import websocket
import threading
import time
import json
import os

from module.message_handler.message_factory import MessageFactory

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.app import App

class WebSocketClientSevice:
    def __init__(self, app: "App", url: str, path: str):
        
        self.app = app
        # SAFE SIMULATION: Force localhost-only connections for educational use
        if not url.startswith(("ws://localhost", "ws://127.0.0.1", "wss://localhost", "wss://127.0.0.1")):
            self.app._log_service.warn("SAFETY: Non-localhost connection blocked. Using localhost for simulation.")
            url = "ws://localhost:8080"
        
        self.url = url
        self.path = path
        self.connection_url = self.url + self.path

        self.ws = None
        self.thread = None
        self.is_connected = False
        self._setup_safe_simulation()

    def _setup_safe_simulation(self):
        """
        SAFE SIMULATION: Creates local simulation environment instead of real C2 communication
        """
        self.simulation_dir = "./lab_test_files/websocket_simulation"
        os.makedirs(self.simulation_dir, exist_ok=True)
        
        # Create safe message outbox for demonstration
        self.outbox_file = f"{self.simulation_dir}/message_outbox.json"
        with open(self.outbox_file, "w") as f:
            json.dump({
                "notice": "This is a safe simulation for educational purposes",
                "messages": []
            }, f, indent=2)

    def connect(self):
        # SAFE SIMULATION: Replace real WebSocket with local simulation
        self.app._log_service.info("SIMULATION: WebSocket connection initiated (localhost-only)")
        self.app._log_service.info("EDUCATIONAL: This demonstrates C2 communication concepts safely")
        
        # Simulate connection without real network activity
        self._simulate_connection()

    def _simulate_connection(self):
        """
        SAFE SIMULATION: Simulates WebSocket connection without real network communication
        """
        try:
            self.is_connected = True
            self.app._log_service.info("SIMULATION: WebSocket connected to localhost simulation")
            
            # Start simulation thread
            self.thread = threading.Thread(target=self._run_simulation)
            self.thread.daemon = True
            self.thread.start()
            
        except Exception as e:
            self.app._log_service.error(f"Simulation connection error: {e}")
            self.is_connected = False

    def _run_simulation(self):
        """
        SAFE SIMULATION: Runs educational demonstration instead of real malicious communication
        """
        simulation_count = 0
        while self.is_connected and simulation_count < 5:  # Limit simulation
            try:
                # Simulate receiving safe demo messages
                demo_message = {
                    "type": "demo_command",
                    "payload": f"Educational simulation message #{simulation_count}",
                    "timestamp": time.time(),
                    "notice": "This is a safe simulation for learning purposes"
                }
                
                self._handle_simulation_message(json.dumps(demo_message))
                time.sleep(10)  # Wait between simulation messages
                simulation_count += 1
                
            except Exception as e:
                self.app._log_service.error(f"Simulation error: {e}")
                break
        
        self.app._log_service.info("SIMULATION: Educational demonstration completed")

    def _handle_simulation_message(self, message_data):
        """
        SAFE SIMULATION: Handles demo messages safely without real malicious actions
        """
        try:
            message = json.loads(message_data)
            self.app._log_service.info(f"SIMULATION: Received demo message: {message.get('type', 'unknown')}")
            
            # Log to safe simulation file instead of real C2 communication
            self._log_to_simulation_outbox(message)
            
        except Exception as e:
            self.app._log_service.error(f"Simulation message handling error: {e}")

    def _log_to_simulation_outbox(self, message):
        """
        SAFE SIMULATION: Logs messages to local file instead of sending to real C2 server
        """
        try:
            with open(self.outbox_file, "r") as f:
                data = json.load(f)
            
            data["messages"].append({
                "timestamp": time.time(),
                "message": message,
                "note": "Safe simulation - no real data transmitted"
            })
            
            with open(self.outbox_file, "w") as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            self.app._log_service.error(f"Simulation logging error: {e}")

    def disconnect(self):
        # SAFE SIMULATION: Clean disconnect from simulation
        if not self.is_connected:
            self.app._log_service.info("SIMULATION: Not connected to simulation server")
            return
        
        self.is_connected = False
        if self.thread:
            self.thread.join()
            self.thread = None
        
        self.app._log_service.info("SIMULATION: Disconnected from localhost simulation")
        self.is_connected = False

    # SAFE SIMULATION: Replaced dangerous WebSocket callbacks with safe educational stubs
    
    def send_message(self, message):
        """
        SAFE SIMULATION: Logs messages locally instead of sending to real C2 server
        """
        if not self.is_connected:
            self.app._log_service.warn("SIMULATION: Not connected to simulation server")
            return

        # SAFE: Log to local file instead of real network transmission
        self.app._log_service.info("SIMULATION: Message queued for local demonstration")
        self._log_to_simulation_outbox({
            "direction": "outbound",
            "message": message,
            "timestamp": time.time(),
            "note": "Simulated outbound message - no real transmission"
        })
        
    def mock_c2_send(self, payload):
        """
        SAFE SIMULATION: Replacement for dangerous C2 communication
        Writes payload to local JSON file for educational inspection
        """
        outbox_dir = "./outbox"
        os.makedirs(outbox_dir, exist_ok=True)
        
        timestamp = int(time.time())
        filename = f"{outbox_dir}/mock_payload_{timestamp}.json"
        
        safe_payload = {
            "notice": "EDUCATIONAL SIMULATION - No real data transmitted",
            "timestamp": time.time(),
            "original_payload": payload,
            "safety_note": "This demonstrates C2 communication concepts safely"
        }
        
        with open(filename, "w") as f:
            json.dump(safe_payload, f, indent=2)
            
        self.app._log_service.info(f"SIMULATION: Mock C2 payload saved to {filename}")
        return filename