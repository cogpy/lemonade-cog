"""
Tests for OpenCog Multi-Agent Orchestrator
"""

import pytest
import asyncio
from lemonade.opencog.orchestrator import MultiAgentOrchestrator
from lemonade.opencog.agent import CognitiveAgent


@pytest.mark.asyncio
async def test_orchestrator_initialization():
    """Test orchestrator initialization"""
    orchestrator = MultiAgentOrchestrator(config={"num_agents": 2})
    await orchestrator.initialize()
    
    assert len(orchestrator.agents) == 2
    assert not orchestrator.running


@pytest.mark.asyncio
async def test_orchestrator_add_agent():
    """Test adding an agent to orchestrator"""
    orchestrator = MultiAgentOrchestrator()
    await orchestrator.initialize()
    
    initial_count = len(orchestrator.agents)
    
    new_agent = CognitiveAgent(agent_id="new_agent")
    await orchestrator.add_agent(new_agent)
    
    assert len(orchestrator.agents) == initial_count + 1
    assert "new_agent" in orchestrator.agents


@pytest.mark.asyncio
async def test_orchestrator_remove_agent():
    """Test removing an agent from orchestrator"""
    orchestrator = MultiAgentOrchestrator()
    await orchestrator.initialize()
    
    agent_id = list(orchestrator.agents.keys())[0]
    await orchestrator.remove_agent(agent_id)
    
    assert agent_id not in orchestrator.agents


@pytest.mark.asyncio
async def test_orchestrator_submit_task():
    """Test submitting task to orchestrator"""
    orchestrator = MultiAgentOrchestrator()
    await orchestrator.initialize()
    
    task = {"type": "inference", "prompt": "test"}
    await orchestrator.submit_task(task)
    
    assert orchestrator.task_queue.qsize() == 1


@pytest.mark.asyncio
async def test_orchestrator_start_stop():
    """Test starting and stopping orchestrator"""
    orchestrator = MultiAgentOrchestrator()
    await orchestrator.initialize()
    
    await orchestrator.start()
    assert orchestrator.running
    
    await orchestrator.stop()
    assert not orchestrator.running


@pytest.mark.asyncio
async def test_orchestrator_cognitive_synergy():
    """Test cognitive synergy between agents"""
    orchestrator = MultiAgentOrchestrator(config={"num_agents": 2})
    await orchestrator.initialize()
    
    # Add knowledge to one agent
    agent_id = list(orchestrator.agents.keys())[0]
    orchestrator.agents[agent_id].knowledge_base["test_knowledge"] = "value"
    
    # Enable cognitive synergy
    await orchestrator.enable_cognitive_synergy()
    
    # All agents should now have the knowledge
    for agent in orchestrator.agents.values():
        assert "test_knowledge" in agent.knowledge_base


@pytest.mark.asyncio
async def test_orchestrator_get_system_status():
    """Test getting system status"""
    orchestrator = MultiAgentOrchestrator(config={"num_agents": 2})
    await orchestrator.initialize()
    
    status = await orchestrator.get_system_status()
    
    assert "orchestrator_running" in status
    assert status["num_agents"] == 2
    assert "agents" in status
    assert len(status["agents"]) == 2
