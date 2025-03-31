# Brownian Motion Simulation

This project is my submission for the GSoC-2025 JdeRobot Python Challenge. It implements a simulation of Brownian motion behavior for a robot within a square arena.

## Project Overview

In this simulation, a robot exhibits Brownian motion within defined boundaries:
- The robot is represented as a point/circle
- The robot starts in the middle of a square arena, moving straight ahead
- When the robot collides with the arena boundaries, it rotates for a random duration
- After rotation, the robot continues moving forward in the new direction

## Requirements

- Python 3.6 or higher
- NumPy (for mathematical operations)
- Matplotlib (for visualization)

## Installation

Clone this repository and install the package:

```bash
git clone https://github.com/jayzalani/Brownian_Motion_Simulation.git
cd brownianMotion
pip install -e .
```

## Usage

### Running the Example Simulation

The easiest way to run the simulation is to use the provided example script:

```bash
python -m brownianMotion.example
```

This will:
- Start the simulation with default parameters
- Display the visualization in a new window
- Save an animation of the simulation as "brownian_motion.gif"

## Project Structure

- `brownianMotion/` - Main package directory
  - `__init__.py` - Package initialization
  - `robot.py` - BrownianRobot class implementation
  - `simulation.py` - Simulation environment
  - `example.py` - Example application
- `setup.py` - Package setup file

## Demonstration

The following GIF shows the robot's movement pattern:![brownian_motion](https://github.com/user-attachments/assets/53f8eeaa-f804-48b4-9890-63aaa5d5c09b)

### If this does not load then go to exampleOutput which contains a one more example gif of this simulation 


## Features

- **Random Rotation Duration**: After colliding with a boundary, the robot rotates for a randomized number of steps before continuing
- **Direction Control**: The robot always turns away from the boundary it collided with
- **Visualization**: Real-time visualization of the robot's movement
- **Animation Export**: Capability to export the simulation as GIF animations

## GSoC-2025 JdeRobot Challenge Implementation Notes

This project fulfills the requirements of the GSoC-2025 JdeRobot Python Challenge by:

1. Implementing Brownian motion behavior in a robot
2. Using only Python standard library, NumPy, and Matplotlib
3. Structuring the code as a Python module
4. Providing a sample application
5. Generating visualization media (GIFs)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
