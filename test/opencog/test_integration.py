"""
Tests for OpenCog Integration with Lemonade
"""

import pytest
import asyncio
from lemonade.opencog.integration import OpenCogLemonadeIntegration


@pytest.mark.asyncio
async def test_integration_initialization():
    """Test integration initialization"""
    integration = OpenCogLemonadeIntegration()
    await integration.initialize()

    assert integration.orchestrator is not None
    assert integration.autognosis is not None
    assert integration.autogenesis is not None
    assert len(integration.orchestrator.agents) > 0


@pytest.mark.asyncio
async def test_integration_backend_agents():
    """Test that backend-specific agents are created"""
    integration = OpenCogLemonadeIntegration()
    await integration.initialize()

    # Should have agents for different backends
    agent_ids = list(integration.orchestrator.agents.keys())

    assert any("oga-cpu" in agent_id for agent_id in agent_ids)
    assert any("llamacpp" in agent_id for agent_id in agent_ids)


@pytest.mark.asyncio
async def test_integration_submit_task():
    """Test submitting an inference task"""
    integration = OpenCogLemonadeIntegration()
    await integration.initialize()

    task = {
        "id": "test_task",
        "prompt": "test prompt",
    }

    result = await integration.submit_inference_task(task)

    assert result["status"] == "submitted"
    assert result["task_id"] == "test_task"


@pytest.mark.asyncio
async def test_integration_get_cognitive_insights():
    """Test getting cognitive insights"""
    integration = OpenCogLemonadeIntegration()
    await integration.initialize()

    insights = await integration.get_cognitive_insights()

    assert "self_knowledge" in insights
    assert "growth_metrics" in insights


@pytest.mark.asyncio
async def test_integration_start_stop():
    """Test starting and stopping integration"""
    integration = OpenCogLemonadeIntegration()
    await integration.initialize()

    await integration.start()
    assert integration.running

    await integration.stop()
    assert not integration.running
