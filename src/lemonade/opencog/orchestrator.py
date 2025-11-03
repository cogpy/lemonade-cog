"""
Multi-Agent Orchestrator for OpenCog workbench.

This module coordinates multiple cognitive agents to work together
in achieving autonomous LLM orchestration goals.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any
from lemonade.opencog.agent import CognitiveAgent


class MultiAgentOrchestrator:
    """
    Orchestrates multiple cognitive agents for autonomous operations.

    The orchestrator manages:
    - Agent lifecycle (creation, monitoring, shutdown)
    - Task distribution and load balancing
    - Inter-agent communication
    - System-wide coordination
    - Cognitive synergy between agents
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the multi-agent orchestrator.

        Args:
            config: Configuration dictionary for the orchestrator
        """
        self.config = config or {}
        self.agents: Dict[str, CognitiveAgent] = {}
        self.task_queue: asyncio.Queue = asyncio.Queue()
        self.running = False
        self.logger = logging.getLogger("opencog.orchestrator")

    async def initialize(self):
        """Initialize the orchestrator and create initial agents"""
        self.logger.info("Initializing Multi-Agent Orchestrator")

        # Create default agent pool
        num_agents = self.config.get("num_agents", 3)
        for i in range(num_agents):
            agent = CognitiveAgent(
                agent_id=f"agent_{i}",
                model_config=self.config.get("model_config", {}),
                capabilities=["inference", "monitoring", "optimization"],
            )
            await agent.initialize()
            self.agents[agent.agent_id] = agent

        self.logger.info(f"Created {len(self.agents)} cognitive agents")

    async def add_agent(self, agent: CognitiveAgent):
        """Add a new agent to the orchestrator"""
        await agent.initialize()
        self.agents[agent.agent_id] = agent
        self.logger.info(f"Added agent {agent.agent_id}")

    async def remove_agent(self, agent_id: str):
        """Remove an agent from the orchestrator"""
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            await agent.shutdown()
            del self.agents[agent_id]
            self.logger.info(f"Removed agent {agent_id}")

    async def submit_task(self, task: Dict[str, Any]):
        """
        Submit a task to the orchestrator for execution.

        Args:
            task: Task specification dictionary
        """
        await self.task_queue.put(task)
        self.logger.debug(f"Task submitted: {task.get('type', 'unknown')}")

    async def _select_agent_for_task(
        self, task: Dict[str, Any]
    ) -> Optional[CognitiveAgent]:
        """
        Select the most appropriate agent for a given task.

        Args:
            task: Task to be executed

        Returns:
            Selected agent or None if no suitable agent found
        """
        task_type = task.get("type")

        # Simple selection: find agent with matching capability and in ACTIVE state
        for agent in self.agents.values():
            if task_type in agent.capabilities and agent.state.value == "active":
                return agent

        # Fallback: return any active agent
        for agent in self.agents.values():
            if agent.state.value == "active":
                return agent

        return None

    async def _process_tasks(self):
        """Process tasks from the queue"""
        while self.running:
            try:
                # Get task with timeout
                task = await asyncio.wait_for(self.task_queue.get(), timeout=1.0)

                # Select agent for task
                agent = await self._select_agent_for_task(task)

                if agent:
                    # Execute task
                    result = await agent.execute_task(task)
                    self.logger.debug(f"Task completed by {agent.agent_id}: {result}")
                else:
                    self.logger.warning(f"No suitable agent found for task: {task}")

            except asyncio.TimeoutError:
                # No tasks in queue, continue
                continue
            except Exception as e:
                self.logger.error(f"Error processing task: {e}")

    async def start(self):
        """Start the orchestrator and begin processing tasks"""
        self.logger.info("Starting Multi-Agent Orchestrator")
        self.running = True

        # Start background task processor
        asyncio.create_task(self._process_tasks())

    async def stop(self):
        """Stop the orchestrator and shutdown all agents"""
        self.logger.info("Stopping Multi-Agent Orchestrator")
        self.running = False

        # Shutdown all agents
        for agent in self.agents.values():
            await agent.shutdown()

    async def enable_cognitive_synergy(self):
        """
        Enable cognitive synergy between agents for AGI operations.

        Cognitive synergy allows agents to:
        - Share knowledge and experiences
        - Collaborate on complex tasks
        - Collectively learn and improve
        """
        self.logger.info("Enabling cognitive synergy")

        # Share knowledge bases between agents
        combined_knowledge = {}
        for agent in self.agents.values():
            combined_knowledge.update(agent.knowledge_base)

        # Distribute combined knowledge to all agents
        for agent in self.agents.values():
            agent.knowledge_base.update(combined_knowledge)

    async def get_system_status(self) -> Dict[str, Any]:
        """
        Get current status of the orchestrator and all agents.

        Returns:
            System status dictionary
        """
        return {
            "orchestrator_running": self.running,
            "num_agents": len(self.agents),
            "agents": [
                {
                    "agent_id": agent.agent_id,
                    "state": agent.state.value,
                    "capabilities": agent.capabilities,
                    "experience_count": len(agent.experience_log),
                }
                for agent in self.agents.values()
            ],
            "pending_tasks": self.task_queue.qsize(),
        }
