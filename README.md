# Introduction to AI Projects Overview

This repository contains projects related to the course "Introduction to AI", focusing on various aspects of Artificial Intelligence including path finding, logic planning, and the classical AI problems like eating all the dots in Pacman, localization, mapping, and SLAM.

## Projects Description

### Project 1: PacMan Search

- **Description**: Implement general search algorithms to enable PacMan to navigate through a maze and collect food efficiently.
- **Key Files**:
  - `search.py`: Contains all the search algorithms.
  - `searchAgents.py`: Contains all search-based agents.
- **Technologies Used**: Python, Pygame
- **Some commands to Run**:
  ```bash
  python pacman.py -l tinyMaze -p SearchAgent
  python pacman.py -l mediumMaze -p SearchAgent
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

  ## Project 2: Logic and Classical Planning

### Project 2: Logic

In the "Logic and Classical Planning" project, students delve into the theoretical underpinnings and practical applications of logic in Artificial Intelligence. The focus is on utilizing simple Python functions to generate logical sentences that describe the physics governing the PacMan world, known as "pacphysics." These logical formulations then serve as the basis for solving various planning and inference tasks using SAT solvers like PycoSAT.

### Project Goals

The primary objectives of this project are:

- To understand and apply propositional logic for describing environment states and dynamics.
- To utilize SAT solvers for planning and solving logical inference tasks.
- To explore classical AI planning problems in the context of the PacMan game, involving action sequences for reaching goal locations, eating all the dots, and more complex scenarios like localization, mapping, and SLAM (Simultaneous Localization and Mapping).

### Key Components and Tasks

Students will engage with several key components throughout this project:

1. **Logic Formulation**: Generate logical sentences using the `Expr` class to represent the rules of the PacMan world and the interactions within it.
2. **SAT Solving**: Leverage the PycoSAT solver to find models that satisfy given logical sentences, facilitating the planning and execution of actions within the game environment.
3. **Problem-Specific Implementations**: Create specific logic-based solutions for various tasks such as:
    - Generating action sequences to reach goal locations.
    - Efficiently eating all the dots in the maze.
    - Localization: Inferring PacMan's location based on sensor data.
    - Mapping: Constructing a map of the maze.
    - SLAM: Simultaneously performing localization and mapping.

### Technologies and Tools

- **Python**: The primary programming language used for implementing logic sentences and interacting with the SAT solver.
- **PycoSAT**: A Python library providing a wrapper around the picoSAT library, used for solving SAT problems.
- **AIMA Library**: Utilizes components from the AIMA (Artificial Intelligence: A Modern Approach) codebase to facilitate logic operations and interactions.

### Learning Outcomes

By completing this project, students will gain a deeper understanding of logical representations in AI, the use of SAT solvers for decision-making and problem-solving, and the application of these concepts to classical planning problems within a familiar and engaging game environment.
