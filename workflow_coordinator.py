import requests
import time
import json

class HGAuraWorkflowCoordinator:
def init(self):
self.qwen_agent_url = "http://edge-cubo:8000/analyze"
self.gemma_agent_url = "http://edge-jetson:8001/describe"
self.elastic_url = "http://elasticsearch:9200"
self.hardware_monitor = HardwarePerformanceMonitor()
text

def process_surveillance_frame(self, frame_data, camera_context):
    """Execute the complete agentic AI pipeline with hardware awareness"""
    start_time = time.time()
    
    if not self.hardware_monitor.check_resource_availability():
        return self.queue_for_later_processing(frame_data, camera_context)
    
    planning_request = {
        "frame": frame_data,
        "camera_id": camera_context['id'],
        "location": camera_context['location'],
        "time": camera_context['timestamp'],
        "processing_mode": self.get_optimal_processing_mode()
    }
    
    planning_response = requests.post(
        self.qwen_agent_url,
        json=planning_request,
        timeout=5
    ).json()
    
    context_query = planning_response['context_queries']
    contextual_data = self.retrieve_context_optimized(context_query)
    
    description_request = {
        "frame": frame_data,
        "initial_analysis": planning_response['analysis'],
        "contextual_data": contextual_data,
        "report_template": "surveillance_observation",
        "hardware_constraints": self.get_hardware_constraints()
    }
    
    observation_report = requests.post(
        self.gemma_agent_url,
        json=description_request,
        timeout=10
    ).json()
    
    alert_decision = self.evaluate_for_alerts(observation_report)
    processing_time = time.time() - start_time
    self.hardware_monitor.record_processing_metrics(processing_time)
    
    return {
        "observation_report": observation_report,
        "alert_decision": alert_decision,
        "processing_time": processing_time,
        "hardware_utilization": self.hardware_monitor.get_current_utilization()
    }
