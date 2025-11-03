"""
Tests for OpenCog Autogenesis Engine
"""

import pytest
import asyncio
from lemonade.opencog.autogenesis import AutogenesisEngine


@pytest.mark.asyncio
async def test_autogenesis_evolve():
    """Test autogenesis evolution process"""
    engine = AutogenesisEngine()

    current_state = {
        "latency": 150,
        "capabilities": ["llm_inference"],
        "requested_features": ["advanced_reasoning"],
        "feedback": [
            {"type": "performance", "message": "Slow response time"},
        ],
    }

    result = await engine.evolve(current_state)

    assert result["status"] == "evolved"
    assert "improvements" in result
    assert result["evolution_generation"] > 0


@pytest.mark.asyncio
async def test_autogenesis_evolution_history():
    """Test that evolution history is recorded"""
    engine = AutogenesisEngine()

    current_state = {
        "latency": 100,
        "capabilities": [],
        "requested_features": [],
        "feedback": [],
    }

    initial_gen = len(engine.evolution_history)

    await engine.evolve(current_state)

    assert len(engine.evolution_history) == initial_gen + 1


@pytest.mark.asyncio
async def test_autogenesis_get_evolution_history():
    """Test retrieving evolution history"""
    engine = AutogenesisEngine()

    current_state = {
        "latency": 100,
        "capabilities": [],
        "requested_features": [],
        "feedback": [],
    }

    await engine.evolve(current_state)

    history = await engine.get_evolution_history()

    assert len(history) > 0
    assert "timestamp" in history[-1]
    assert "improvements" in history[-1]


@pytest.mark.asyncio
async def test_autogenesis_measure_growth():
    """Test measuring system growth"""
    engine = AutogenesisEngine()

    current_state = {
        "latency": 150,
        "capabilities": [],
        "requested_features": ["feature1"],
        "feedback": [{"type": "test"}],
    }

    # Evolve multiple times
    await engine.evolve(current_state)
    await engine.evolve(current_state)

    growth = await engine.measure_growth()

    assert growth["evolution_generations"] >= 2
    assert "total_improvements" in growth
    assert "active_strategies" in growth


@pytest.mark.asyncio
async def test_autogenesis_strategies_applied():
    """Test that improvement strategies are applied"""
    engine = AutogenesisEngine()

    current_state = {
        "latency": 200,  # High latency
        "capabilities": ["basic"],
        "requested_features": ["advanced"],  # Capability gap
        "feedback": [{"type": "feedback"}],
    }

    result = await engine.evolve(current_state)

    # Should have applied multiple strategies
    assert len(result["improvements"]) > 0

    # Check that specific strategies were applied
    strategies_applied = [imp["strategy"] for imp in result["improvements"]]
    assert "optimize_performance" in strategies_applied
    assert "enhance_capabilities" in strategies_applied
