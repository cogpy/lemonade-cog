# OpenCog Autonomous Multi-Agent Orchestration Workbench

## Overview

OpenCog is an autonomous multi-agent orchestration system integrated into Lemonade that enables AGI cognitive synergy with self-healing maintenance, repair, and improvement workflows toward true autognosis (self-knowledge) and autogenesis (self-improvement).

## Features

### Multi-Agent Orchestration
- **Cognitive Agents**: Autonomous agents that can execute tasks, learn from experiences, and communicate with each other
- **Load Balancing**: Intelligent task distribution across agents
- **Cognitive Synergy**: Agents share knowledge and collaborate for enhanced performance

### Autonomous Workflows
- **Self-Healing**: Automatic detection and repair of system issues
- **Maintenance**: Scheduled optimization and resource cleanup
- **Improvement**: Continuous performance enhancement

### AGI Capabilities
- **Autognosis**: Self-knowledge and introspection capabilities
- **Autogenesis**: Autonomous evolution and self-improvement
- **Adaptive Learning**: Learn from experiences and feedback

## Installation

OpenCog is included with the Lemonade SDK. Install it using:

```bash
pip install -e .
```

## Quick Start

### Using the CLI

Start the multi-agent orchestrator:

```bash
lemonade-opencog start
```

Run self-healing workflow:

```bash
lemonade-opencog heal
```

Run maintenance workflow:

```bash
lemonade-opencog maintain
```

Run improvement workflow:

```bash
lemonade-opencog improve
```

Perform system introspection (autognosis):

```bash
lemonade-opencog introspect
```

Trigger autonomous evolution (autogenesis):

```bash
lemonade-opencog evolve
```

### Using the Python API

```python
import asyncio
from lemonade.opencog import MultiAgentOrchestrator

async def main():
    # Create and initialize orchestrator
    orchestrator = MultiAgentOrchestrator(config={
        "num_agents": 3,
        "model_config": {"backend": "oga-hybrid"}
    })
    await orchestrator.initialize()
    
    # Start orchestrator
    await orchestrator.start()
    
    # Enable cognitive synergy
    await orchestrator.enable_cognitive_synergy()
    
    # Submit a task
    await orchestrator.submit_task({
        "type": "inference",
        "prompt": "What is the meaning of life?"
    })
    
    # Get system status
    status = await orchestrator.get_system_status()
    print(f"System status: {status}")
    
    # Stop orchestrator
    await orchestrator.stop()

asyncio.run(main())
```

### Integration with Lemonade Server

```python
import asyncio
from lemonade.opencog.integration import OpenCogLemonadeIntegration

async def main():
    # Create integration
    integration = OpenCogLemonadeIntegration(
        lemonade_config={"port": 8000},
        opencog_config={"num_agents": 5}
    )
    
    # Initialize and start
    await integration.initialize()
    await integration.start()
    
    # Submit inference task through OpenCog
    result = await integration.submit_inference_task({
        "id": "task_1",
        "prompt": "Explain quantum computing",
        "model": "Llama-3.2-1B-Instruct"
    })
    
    # Get cognitive insights
    insights = await integration.get_cognitive_insights()
    print(f"Self-knowledge: {insights['self_knowledge']}")
    print(f"Growth metrics: {insights['growth_metrics']}")
    
    # Stop integration
    await integration.stop()

asyncio.run(main())
```

## Architecture

### Components

1. **Cognitive Agent** (`lemonade.opencog.agent`): Individual autonomous agent
2. **Multi-Agent Orchestrator** (`lemonade.opencog.orchestrator`): Coordinates multiple agents
3. **Workflows** (`lemonade.opencog.workflows`): Autonomous operation workflows
4. **Autognosis Engine** (`lemonade.opencog.autognosis`): Self-knowledge system
5. **Autogenesis Engine** (`lemonade.opencog.autogenesis`): Self-improvement system
6. **Integration Layer** (`lemonade.opencog.integration`): Lemonade integration

### Agent States

- `IDLE`: Agent is not active
- `ACTIVE`: Agent is ready to execute tasks
- `LEARNING`: Agent is processing experiences
- `HEALING`: Agent is performing self-repair
- `MAINTAINING`: Agent is running maintenance
- `IMPROVING`: Agent is optimizing performance

## Workflows

### Self-Healing Workflow

Automatically detects and repairs system issues:

```python
from lemonade.opencog.workflows import SelfHealingWorkflow

async def run_healing():
    workflow = SelfHealingWorkflow()
    
    context = {
        "agents": [...],  # Current agents
        "memory_usage": 85,
    }
    
    result = await workflow.execute(context)
    print(f"Issues found: {result['issues_found']}")
    print(f"Repairs applied: {result['repairs_applied']}")
```

### Maintenance Workflow

Performs regular system maintenance:

```python
from lemonade.opencog.workflows import MaintenanceWorkflow

async def run_maintenance():
    workflow = MaintenanceWorkflow()
    result = await workflow.execute({})
    print(f"Maintenance tasks completed: {result['tasks_completed']}")
```

### Improvement Workflow

Continuously improves system performance:

```python
from lemonade.opencog.workflows import ImprovementWorkflow

async def run_improvement():
    workflow = ImprovementWorkflow()
    
    context = {
        "throughput": 100,
        "latency": 150,
        "accuracy": 0.95,
    }
    
    result = await workflow.execute(context)
    print(f"Improvements made: {result['improvements_made']}")
```

## AGI Capabilities

### Autognosis (Self-Knowledge)

The autognosis engine provides self-awareness:

```python
from lemonade.opencog.autognosis import AutognosisEngine

async def introspect_system():
    engine = AutognosisEngine()
    
    system_state = {
        "agents": [...],
        "memory_available": 8000,
        "gpu_available": True,
        # ... other metrics
    }
    
    # Perform introspection
    insights = await engine.introspect(system_state)
    
    print(f"Capabilities: {insights['capabilities']}")
    print(f"Limitations: {insights['limitations']}")
    print(f"Performance: {insights['performance']}")
    
    # Assess readiness for a task
    task = {"type": "inference", "required_capabilities": ["llm_inference"]}
    readiness = await engine.assess_readiness(task)
    print(f"Ready: {readiness['ready']}")
```

### Autogenesis (Self-Improvement)

The autogenesis engine enables autonomous evolution:

```python
from lemonade.opencog.autogenesis import AutogenesisEngine

async def evolve_system():
    engine = AutogenesisEngine()
    
    current_state = {
        "latency": 150,
        "capabilities": ["basic_inference"],
        "requested_features": ["advanced_reasoning"],
        "feedback": [...],
    }
    
    # Trigger evolution
    result = await engine.evolve(current_state)
    
    print(f"Evolution generation: {result['evolution_generation']}")
    print(f"Improvements: {result['improvements']}")
    
    # Measure growth over time
    growth = await engine.measure_growth()
    print(f"Total improvements: {growth['total_improvements']}")
```

## Configuration

OpenCog can be configured through the orchestrator config:

```python
config = {
    "num_agents": 5,  # Number of cognitive agents
    "model_config": {
        "backend": "oga-hybrid",
        "model": "Llama-3.2-1B-Instruct"
    }
}

orchestrator = MultiAgentOrchestrator(config)
```

## Testing

Run OpenCog tests:

```bash
pytest test/opencog/
```

Run specific test files:

```bash
pytest test/opencog/test_agent.py
pytest test/opencog/test_orchestrator.py
pytest test/opencog/test_workflows.py
pytest test/opencog/test_autognosis.py
pytest test/opencog/test_autogenesis.py
pytest test/opencog/test_integration.py
```

## Best Practices

1. **Enable Cognitive Synergy**: Always enable cognitive synergy for multi-agent collaboration
2. **Monitor System Status**: Regularly check system status to ensure healthy operation
3. **Run Workflows Periodically**: Schedule self-healing and maintenance workflows
4. **Track Evolution**: Monitor autogenesis metrics to measure system improvement
5. **Assess Readiness**: Use autognosis to assess readiness before complex tasks

## Troubleshooting

### Agents not starting

Check that agents are properly initialized:
```python
await orchestrator.initialize()
```

### High memory usage

Run maintenance workflow to clean up resources:
```bash
lemonade-opencog maintain
```

### Performance degradation

Trigger improvement workflow:
```bash
lemonade-opencog improve
```

## Contributing

Contributions to OpenCog are welcome! Please see the main Lemonade contributing guide.

## License

OpenCog is part of the Lemonade SDK and is licensed under Apache 2.0.
