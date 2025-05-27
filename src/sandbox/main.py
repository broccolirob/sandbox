#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from sandbox.crew import Sandbox

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'project_description': 'Our company wants to launch a new weekly blog series focused on "Sustainable Living Practices for Urban Dwellers". The goal is to increase website engagement and position our brand as a thought leader in sustainability. The target audience is young professionals living in cities. We need to plan the first month of content (4 blog posts), including research, writing, and a promotional strategy. The desired tone is informative, actionable, and inspiring. We have a team that includes research capabilities and content writing capabilities. The deadline for having the first month\'s plan (including topics for 4 posts and a promotional outline) is in 2 weeks.',
    }
    
    try:
        Sandbox().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'project_description': 'Our company wants to launch a new weekly blog series focused on "Sustainable Living Practices for Urban Dwellers". The goal is to increase website engagement and position our brand as a thought leader in sustainability. The target audience is young professionals living in cities. We need to plan the first month of content (4 blog posts), including research, writing, and a promotional strategy. The desired tone is informative, actionable, and inspiring. We have a team that includes research capabilities and content writing capabilities. The deadline for having the first month\'s plan (including topics for 4 posts and a promotional outline) is in 2 weeks.',
    }
    try:
        Sandbox().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Sandbox().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'project_description': 'Our company wants to launch a new weekly blog series focused on "Sustainable Living Practices for Urban Dwellers". The goal is to increase website engagement and position our brand as a thought leader in sustainability. The target audience is young professionals living in cities. We need to plan the first month of content (4 blog posts), including research, writing, and a promotional strategy. The desired tone is informative, actionable, and inspiring. We have a team that includes research capabilities and content writing capabilities. The deadline for having the first month\'s plan (including topics for 4 posts and a promotional outline) is in 2 weeks.',
    }
    
    try:
        Sandbox().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
