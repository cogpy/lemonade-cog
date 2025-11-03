"""
OpenCog Autonomous Multi-Agent Orchestration Workbench

This module implements OpenCog as an autonomous multi-agent orchestration system
for Lemonade configurations with LLM models, servers, SDK, API, CLI, etc.
It enables AGI cognitive synergy with self-healing maintenance, repair and
improvement workflows toward true autognosis and autogenesis.
"""

from lemonade.opencog.agent import CognitiveAgent
from lemonade.opencog.orchestrator import MultiAgentOrchestrator
from lemonade.opencog.workflows import (
    SelfHealingWorkflow,
    MaintenanceWorkflow,
    ImprovementWorkflow,
)
from lemonade.opencog.autognosis import AutognosisEngine
from lemonade.opencog.autogenesis import AutogenesisEngine

__all__ = [
    "CognitiveAgent",
    "MultiAgentOrchestrator",
    "SelfHealingWorkflow",
    "MaintenanceWorkflow",
    "ImprovementWorkflow",
    "AutognosisEngine",
    "AutogenesisEngine",
]
