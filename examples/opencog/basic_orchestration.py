"""
OpenCog Multi-Agent Orchestration Example

This example demonstrates how to use OpenCog's autonomous multi-agent
orchestration system for LLM operations.
"""

import asyncio
from lemonade.opencog import MultiAgentOrchestrator, CognitiveAgent


async def main():
    print("=== OpenCog Multi-Agent Orchestration Example ===\n")
    
    # Create orchestrator with configuration
    print("1. Creating Multi-Agent Orchestrator...")
    orchestrator = MultiAgentOrchestrator(
        config={
            "num_agents": 3,
            "model_config": {
                "backend": "oga-cpu",
            }
        }
    )
    
    # Initialize the orchestrator
    print("2. Initializing orchestrator...")
    await orchestrator.initialize()
    print(f"   Created {len(orchestrator.agents)} cognitive agents\n")
    
    # Start the orchestrator
    print("3. Starting orchestrator...")
    await orchestrator.start()
    
    # Enable cognitive synergy
    print("4. Enabling cognitive synergy between agents...")
    await orchestrator.enable_cognitive_synergy()
    print("   Cognitive synergy enabled\n")
    
    # Submit some tasks
    print("5. Submitting tasks to agents...")
    tasks = [
        {"type": "inference", "prompt": "What is the capital of France?"},
        {"type": "monitor", "system": "health_check"},
        {"type": "optimize", "target": "performance"},
    ]
    
    for i, task in enumerate(tasks):
        await orchestrator.submit_task(task)
        print(f"   Task {i+1} submitted: {task['type']}")
    
    # Wait a bit for tasks to process
    await asyncio.sleep(2)
    
    # Get system status
    print("\n6. Getting system status...")
    status = await orchestrator.get_system_status()
    print(f"   Orchestrator running: {status['orchestrator_running']}")
    print(f"   Number of agents: {status['num_agents']}")
    print(f"   Pending tasks: {status['pending_tasks']}")
    
    # Show agent details
    print("\n7. Agent Details:")
    for agent_info in status['agents']:
        print(f"   - {agent_info['agent_id']}")
        print(f"     State: {agent_info['state']}")
        print(f"     Capabilities: {', '.join(agent_info['capabilities'])}")
        print(f"     Experience count: {agent_info['experience_count']}")
    
    # Add a custom agent
    print("\n8. Adding a custom specialized agent...")
    custom_agent = CognitiveAgent(
        agent_id="specialist_agent",
        model_config={"backend": "llamacpp", "model": "custom"},
        capabilities=["inference", "reasoning", "code_generation"],
    )
    await orchestrator.add_agent(custom_agent)
    print("   Custom agent added\n")
    
    # Stop the orchestrator
    print("9. Stopping orchestrator...")
    await orchestrator.stop()
    print("   Orchestrator stopped\n")
    
    print("=== Example Complete ===")


if __name__ == "__main__":
    asyncio.run(main())
