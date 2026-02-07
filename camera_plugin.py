import requests
import json
from datetime import datetime

class HGAuraCameraPlugin:
def init(self, node_id, camera_config):
self.node_id = node_id
self.camera_config = camera_config
self.s4t_backend_url = "https://s4t-cloud.example.com/api"
text

def register_camera(self):
    """Register camera as virtual node in Stack4Things"""
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
    
    response = requests.post(
        f"{self.s4t_backend_url}/nodes/register",
        json=registration_payload,
        headers={'Authorization': f'Bearer {self.get_token()}'}
    )
    
    if response.status_code == 201:
        print(f"Camera {self.node_id} registered successfully")
        return response.json()['node_uuid']
    else:
        print(f"Registration failed: {response.text}")
        return None
