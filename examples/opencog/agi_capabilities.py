"""
OpenCog AGI Capabilities Example

This example demonstrates the autognosis (self-knowledge) and autogenesis
(self-improvement) capabilities for achieving AGI cognitive synergy.
"""

import asyncio
from lemonade.opencog.autognosis import AutognosisEngine
from lemonade.opencog.autogenesis import AutogenesisEngine


async def demonstrate_autognosis():
    """Demonstrate autognosis (self-knowledge) capabilities"""
    print("=== Autognosis (Self-Knowledge) ===\n")
    
    engine = AutognosisEngine()
    
    # System state for introspection
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
    
    # Perform introspection
    print("1. Performing system introspection...")
    result = await engine.introspect(system_state)
    
    print(f"\nCapabilities discovered:")
    for cap in result['capabilities']:
        print(f"  - {cap}")
    
    print(f"\nLimitations identified:")
    if result['limitations']:
        for lim in result['limitations']:
            print(f"  - {lim}")
    else:
        print("  - None")
    
    print(f"\nPerformance metrics:")
    for key, value in result['performance'].items():
        print(f"  - {key}: {value}")
    
    # Assess readiness for a task
    print("\n2. Assessing readiness for inference task...")
    task = {
        "type": "inference",
        "required_capabilities": ["llm_inference", "multi_agent_coordination"],
    }
    
    readiness = await engine.assess_readiness(task)
    print(f"Ready: {readiness['ready']}")
    
    if not readiness['ready']:
        print(f"Missing capabilities: {readiness['missing_capabilities']}")
    
    # Get accumulated self-knowledge
    print("\n3. Retrieving accumulated self-knowledge...")
    knowledge = await engine.get_self_knowledge()
    print(f"Performance history entries: {len(knowledge['performance_history'])}")


async def demonstrate_autogenesis():
    """Demonstrate autogenesis (self-improvement) capabilities"""
    print("\n\n=== Autogenesis (Self-Improvement) ===\n")
    
    engine = AutogenesisEngine()
    
    # Current system state
    current_state = {
        "latency": 150,
        "capabilities": ["llm_inference", "multi_agent_coordination"],
        "requested_features": ["advanced_reasoning", "code_generation"],
        "feedback": [
            {"type": "performance", "message": "Response time could be better"},
            {"type": "feature_request", "message": "Need code generation"},
        ],
    }
    
    # First evolution
    print("1. Triggering first evolution cycle...")
    result = await engine.evolve(current_state)
    
    print(f"Status: {result['status']}")
    print(f"Evolution generation: {result['evolution_generation']}")
    print(f"\nImprovements applied:")
    for improvement in result['improvements']:
        print(f"  - {improvement['strategy']}: {improvement['status']}")
    
    # Second evolution
    print("\n2. Triggering second evolution cycle...")
    result = await engine.evolve(current_state)
    print(f"Evolution generation: {result['evolution_generation']}")
    
    # Measure growth
    print("\n3. Measuring system growth over time...")
    growth = await engine.measure_growth()
    
    print(f"Total evolution generations: {growth['evolution_generations']}")
    print(f"Total improvements made: {growth['total_improvements']}")
    print(f"Active improvement strategies: {len(growth['active_strategies'])}")
    
    # Show evolution history
    print("\n4. Evolution history:")
    history = await engine.get_evolution_history()
    for i, record in enumerate(history):
        print(f"  Generation {i+1}:")
        print(f"    Timestamp: {record['timestamp']}")
        print(f"    Strategies applied: {record['strategies_applied']}")


async def main():
    print("=== OpenCog AGI Capabilities Example ===\n")
    
    await demonstrate_autognosis()
    await demonstrate_autogenesis()
    
    print("\n\n=== Example Complete ===")


if __name__ == "__main__":
    asyncio.run(main())
