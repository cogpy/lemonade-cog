"""
OpenCog Autonomous Workflows Example

This example demonstrates the self-healing, maintenance, and improvement
workflows for autonomous system management.
"""

import asyncio
from lemonade.opencog.workflows import (
    SelfHealingWorkflow,
    MaintenanceWorkflow,
    ImprovementWorkflow,
)


async def demonstrate_self_healing():
    """Demonstrate self-healing workflow"""
    print("=== Self-Healing Workflow ===")
    
    workflow = SelfHealingWorkflow()
    
    # Scenario 1: Healthy system
    print("\nScenario 1: Healthy System")
    healthy_context = {
        "agents": [
            {"agent_id": "agent_0", "state": "active"},
            {"agent_id": "agent_1", "state": "active"},
        ],
        "memory_usage": 60,
    }
    
    result = await workflow.execute(healthy_context)
    print(f"Status: {result['status']}")
    print(f"Issues found: {result['issues_found']}")
    
    # Scenario 2: System with issues
    print("\nScenario 2: System with Issues")
    unhealthy_context = {
        "agents": [
            {"agent_id": "agent_0", "state": "active"},
            {"agent_id": "agent_1", "state": "error"},
        ],
        "memory_usage": 95,
    }
    
    result = await workflow.execute(unhealthy_context)
    print(f"Status: {result['status']}")
    print(f"Issues found: {result['issues_found']}")
    print(f"Repairs applied: {result['repairs_applied']}")
    
    for repair in result['repairs']:
        print(f"  - Repair action: {repair['action']} - {repair['status']}")


async def demonstrate_maintenance():
    """Demonstrate maintenance workflow"""
    print("\n\n=== Maintenance Workflow ===\n")
    
    workflow = MaintenanceWorkflow()
    
    context = {
        "uptime_days": 30,
        "cache_size_mb": 500,
    }
    
    result = await workflow.execute(context)
    print(f"Status: {result['status']}")
    print(f"Tasks completed: {result['tasks_completed']}")
    
    for task in result['details']:
        print(f"  - {task['task']}: {task['status']}")


async def demonstrate_improvement():
    """Demonstrate improvement workflow"""
    print("\n\n=== Improvement Workflow ===\n")
    
    workflow = ImprovementWorkflow()
    
    context = {
        "throughput": 100,
        "latency": 150,  # High latency triggers improvement
        "accuracy": 0.95,
    }
    
    result = await workflow.execute(context)
    print(f"Status: {result['status']}")
    print(f"Opportunities found: {result['opportunities_found']}")
    print(f"Improvements made: {result['improvements_made']}")
    
    for improvement in result['improvements']:
        print(f"  - {improvement['opportunity']['type']}: {improvement['status']}")


async def main():
    print("=== OpenCog Autonomous Workflows Example ===\n")
    
    await demonstrate_self_healing()
    await demonstrate_maintenance()
    await demonstrate_improvement()
    
    print("\n\n=== Example Complete ===")


if __name__ == "__main__":
    asyncio.run(main())
