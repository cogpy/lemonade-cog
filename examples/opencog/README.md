# OpenCog Examples

This directory contains examples demonstrating the OpenCog autonomous multi-agent orchestration workbench for Lemonade.

## Examples

### 1. Basic Orchestration (`basic_orchestration.py`)

Demonstrates the core multi-agent orchestration capabilities:
- Creating and initializing a multi-agent orchestrator
- Starting the orchestrator and enabling cognitive synergy
- Submitting tasks to agents
- Monitoring system status
- Adding custom specialized agents

**Run:**
```bash
python examples/opencog/basic_orchestration.py
```

### 2. Autonomous Workflows (`autonomous_workflows.py`)

Shows the three main autonomous workflows:
- **Self-Healing**: Automatic detection and repair of system issues
- **Maintenance**: Regular system optimization and cleanup
- **Improvement**: Continuous performance enhancement

**Run:**
```bash
python examples/opencog/autonomous_workflows.py
```

### 3. AGI Capabilities (`agi_capabilities.py`)

Demonstrates advanced AGI features:
- **Autognosis**: Self-knowledge and introspection
- **Autogenesis**: Autonomous evolution and self-improvement

**Run:**
```bash
python examples/opencog/agi_capabilities.py
```

## Requirements

All examples require the Lemonade SDK with OpenCog to be installed:

```bash
cd /path/to/lemonade-cog
pip install -e .
```

## Integration with Lemonade

These examples can be integrated with the Lemonade Server to provide autonomous orchestration for LLM inference tasks. See the main OpenCog documentation at `docs/opencog.md` for more details.

## Command Line Interface

You can also use the OpenCog CLI directly:

```bash
# Start multi-agent orchestrator
lemonade-opencog start

# Run self-healing
lemonade-opencog heal

# Run maintenance
lemonade-opencog maintain

# Run improvement
lemonade-opencog improve

# Perform introspection
lemonade-opencog introspect

# Trigger evolution
lemonade-opencog evolve
```

## Learning More

- See `docs/opencog.md` for comprehensive documentation
- Check `test/opencog/` for additional usage patterns
- Visit the Lemonade documentation for integration examples
