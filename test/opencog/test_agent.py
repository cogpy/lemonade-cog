"""
Tests for OpenCog Cognitive Agent
"""

import pytest
import asyncio
from lemonade.opencog.agent import CognitiveAgent, AgentState


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that an agent can be initialized"""
    agent = CognitiveAgent(
        agent_id="test_agent",
        model_config={"model": "test"},
        capabilities=["inference"],
    )
    
    assert agent.agent_id == "test_agent"
    assert agent.state == AgentState.IDLE
    assert "inference" in agent.capabilities


@pytest.mark.asyncio
async def test_agent_initialize():
    """Test agent initialization process"""
    agent = CognitiveAgent(agent_id="test_agent")
    await agent.initialize()
    
    assert agent.state == AgentState.ACTIVE


@pytest.mark.asyncio
async def test_agent_execute_inference_task():
    """Test agent executing inference task"""
    agent = CognitiveAgent(
        agent_id="test_agent",
        capabilities=["inference"],
    )
    await agent.initialize()
    
    task = {"type": "inference", "prompt": "test"}
    result = await agent.execute_task(task)
    
    assert result["status"] == "completed"
    assert result["task_type"] == "inference"
    assert result["agent_id"] == "test_agent"


@pytest.mark.asyncio
async def test_agent_execute_monitoring_task():
    """Test agent executing monitoring task"""
    agent = CognitiveAgent(
        agent_id="test_agent",
        capabilities=["monitoring"],
    )
    await agent.initialize()
    
    task = {"type": "monitor"}
    result = await agent.execute_task(task)
    
    assert result["status"] == "completed"
    assert result["task_type"] == "monitor"
    assert result["health_status"] == "healthy"


@pytest.mark.asyncio
async def test_agent_execute_optimization_task():
    """Test agent executing optimization task"""
    agent = CognitiveAgent(
        agent_id="test_agent",
        capabilities=["optimization"],
    )
    await agent.initialize()
    
    task = {"type": "optimize"}
    result = await agent.execute_task(task)
    
    assert result["status"] == "completed"
    assert result["task_type"] == "optimize"


@pytest.mark.asyncio
async def test_agent_learn_from_experience():
    """Test agent learning capability"""
    agent = CognitiveAgent(agent_id="test_agent")
    await agent.initialize()
    
    # Execute some tasks to build experience
    await agent.execute_task({"type": "inference"})
    await agent.execute_task({"type": "monitor"})
    
    assert len(agent.experience_log) == 2
    
    # Learn from experience
    await agent.learn_from_experience()
    
    assert agent.state == AgentState.ACTIVE


@pytest.mark.asyncio
async def test_agent_self_heal():
    """Test agent self-healing capability"""
    agent = CognitiveAgent(agent_id="test_agent")
    await agent.initialize()
    
    await agent.self_heal()
    
    assert agent.state == AgentState.ACTIVE


@pytest.mark.asyncio
async def test_agent_shutdown():
    """Test agent shutdown"""
    agent = CognitiveAgent(agent_id="test_agent")
    await agent.initialize()
    
    await agent.shutdown()
    
    assert agent.state == AgentState.IDLE
