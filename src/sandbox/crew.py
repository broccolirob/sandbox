from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Sandbox():
    """Sandbox crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    
    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            verbose=True
        )
    
    @task
    def project_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_planner_task'],
            output_file='project_plan.md'
        )
    
    @task
    def project_scoping_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_scoping_task'],
            output_file='project_scoping.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Sandbox crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
