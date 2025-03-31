from brownianMotion import BrownianSimulation

def run_simulation_demo(steps=1000, save_animation=True):
    
    print("Starting Brownian Motion Simulation...")
    
    # Create and run the simulation
    simulation = BrownianSimulation(
        num_steps=steps,
        arena_size=100,
        robot_radius=2,
        speed=1  
    )
    
    # Runs the simulation with visualization and save the animation
    path = simulation.run(
        visualize=True,
        save_animation=save_animation,
        filename="brownian_motion.gif",
        fps=30
    )
    
    print(f"Simulation completed with {len(path)} steps")
    print(f"Final position: {path[-1]}")

if __name__ == "__main__":
    run_simulation_demo()