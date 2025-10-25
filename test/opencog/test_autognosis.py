"""
Tests for OpenCog Autognosis Engine
"""

import pytest
import asyncio
from lemonade.opencog.autognosis import AutognosisEngine


@pytest.mark.asyncio
async def test_autognosis_introspect():
    """Test autognosis introspection capability"""
    engine = AutognosisEngine()
    
    system_state = {
        "agents": [
            {"agent_id": "agent_0", "state": "active"},
            {"agent_id": "agent_1", "state": "active"},
        ],
        "memory_available": 8000,
        "gpu_available": True,
        "avg_response_time": 50,
        "requests_per_second": 100,
        "error_rate": 0.01,
        "cpu_usage": 60,
    }
    
    result = await engine.introspect(system_state)
    
    assert "capabilities" in result
    assert "limitations" in result
    assert "performance" in result
    assert "llm_inference" in result["capabilities"]
    assert "multi_agent_coordination" in result["capabilities"]


@pytest.mark.asyncio
async def test_autognosis_identify_limitations():
    """Test autognosis limitation identification"""
    engine = AutognosisEngine()
    
    system_state = {
        "agents": [{"agent_id": "agent_0"}],
        "memory_available": 500,  # Low memory
        "gpu_available": False,  # No GPU
    }
    
    result = await engine.introspect(system_state)
    
    assert "limited_memory" in result["limitations"]
    assert "no_gpu_acceleration" in result["limitations"]


@pytest.mark.asyncio
async def test_autognosis_get_self_knowledge():
    """Test retrieving accumulated self-knowledge"""
    engine = AutognosisEngine()
    
    system_state = {
        "agents": [{"agent_id": "agent_0", "state": "active"}],
        "memory_available": 8000,
        "gpu_available": True,
    }
    
    await engine.introspect(system_state)
    
    knowledge = await engine.get_self_knowledge()
    
    assert "capabilities" in knowledge
    assert "limitations" in knowledge
    assert "performance_history" in knowledge
    assert len(knowledge["performance_history"]) > 0


@pytest.mark.asyncio
async def test_autognosis_assess_readiness():
    """Test task readiness assessment"""
    engine = AutognosisEngine()
    
    # Build self-knowledge first
    system_state = {
        "agents": [{"agent_id": "agent_0", "state": "active"}],
        "memory_available": 8000,
        "gpu_available": True,
    }
    await engine.introspect(system_state)
    
    # Assess readiness for a task
    task = {
        "type": "inference",
        "required_capabilities": ["llm_inference"],
    }
    
    readiness = await engine.assess_readiness(task)
    
    assert readiness["ready"] is True
    assert len(readiness["missing_capabilities"]) == 0


@pytest.mark.asyncio
async def test_autognosis_assess_readiness_missing_capability():
    """Test readiness assessment with missing capabilities"""
    engine = AutognosisEngine()
    
    system_state = {
        "agents": [],  # No agents, limited capabilities
    }
    await engine.introspect(system_state)
    
    task = {
        "type": "inference",
        "required_capabilities": ["advanced_reasoning"],
    }
    
    readiness = await engine.assess_readiness(task)
    
    assert readiness["ready"] is False
    assert "advanced_reasoning" in readiness["missing_capabilities"]
