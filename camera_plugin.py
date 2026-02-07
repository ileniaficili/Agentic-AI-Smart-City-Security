import requests
import json
import uuid

class HGAuraCameraPlugin:
    """
    Simulates the Stack4Things plugin running on the camera node (e.g., Raspberry Pi + OAK-D).
    Handles registration and capability advertisement.
    """
    def __init__(self, node_id, camera_config):
        self.node_id = node_id
        self.camera_config = camera_config
        # In a real scenario, this points to the S4T Cloud
        self.s4t_backend_url = "http://localhost:8000/api" 
        self.token = "dummy_token_xyz"

    def get_token(self):
        return self.token

    def register_camera(self):
        """Register camera as virtual node in Stack4Things"""
        print(f"[Plugin] Attempting to register camera {self.node_id}...")
        
        registration_payload = {
            "node_id": self.node_id,
            "type": "camera",
            "capabilities": {
                "streaming": True,
                "ptz_control": self.camera_config.get('ptz', False),
                "ai_processing": True,
                "power_mode": "adaptive"
            },
            "location": self.camera_config['location'],
            "metadata": self.camera_config.get('metadata', {}),
            "hardware_profile": "oak_d_pro"
        }
        
        try:
            # We mock the request for the PoC
            # response = requests.post(...) 
            print(f"[Plugin] Payload sent: {json.dumps(registration_payload, indent=2)}")
            
            # Simulate success
            fake_uuid = str(uuid.uuid4())
            print(f"[Plugin] Camera {self.node_id} registered successfully. UUID: {fake_uuid}")
            return fake_uuid
            
        except Exception as e:
            print(f"Registration failed: {e}")
            return None

# Example Usage
if __name__ == "__main__":
    config = {
        "location": "Pace del Mela - Industrial Gate",
        "ptz": False,
        "metadata": {"fw_version": "1.2.0"}
    }
    plugin = HGAuraCameraPlugin("CAM_NODE_01", config)
    plugin.register_camera()
