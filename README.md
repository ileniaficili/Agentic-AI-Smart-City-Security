# Agentic-AI-Smart-City-Security
Reference implementation for "HG-AURA: Intelligent Video Surveillance Through Agentic AI". A multi-agent framework leveraging LLMs (Qwen) and VLMs (Gemma) for real-time urban anomaly detection on Edge infrastructure.

# HG-AURA: Intelligent Video Surveillance Through Agentic AI

This repository hosts the source code and architectural framework for HG-AURA, an intelligent video surveillance system described in the book chapter: "Video Surveillance Through Agentic AI: A Case Study for Safer Smart Cities".

HG-AURA represents a shift from passive recording to active understanding. It utilizes Agentic AI—autonomous software entities capable of reasoning and planning—orchestrated via the Stack4Things (S4T) platform to monitor urban environments, detect anomalies, and generate natural language reports in real-time.

## Context & Objectives

Designed for Smart Cities and industrial perimeters, the system addresses:
- Contextual Understanding: Moving beyond simple object detection to interpret behaviors (e.g., "suspicious loitering" vs. "waiting for a bus").
- Edge-Cloud Continuum: processing data locally on heterogeneous hardware (NVIDIA Jetson, Intel NUC) to reduce latency and respect privacy.
- Natural Language Reporting: Generating human-readable alerts using Vision-Language Models (Gemma) and Large Language Models (Qwen).

##  System Architecture

The solution implements a three-tier architecture:
1.  Sensing Layer: OAK-D Pro cameras for depth-aware visual capture.
2.  Edge Intelligence: Planning Agent (Qwen): Formulates contextual queries.
    * Description Agent (Gemma): Generates detailed scene descriptions.
3.  Cloud/Orchestration: Stack4Things middleware for node virtualization and workflow management.
