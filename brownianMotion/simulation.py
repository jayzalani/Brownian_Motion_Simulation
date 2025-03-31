import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .robot import BrownianRobot

class BrownianSimulation:    
    def __init__(self, num_steps: int = 1000, arena_size: int = 100, 
                 robot_radius: int = 2, speed: float = 0.8):
        self.num_steps = num_steps
        self.robot = BrownianRobot(arena_size, robot_radius, speed)
        self.fig, self.ax = None, None
        self.robot_marker, self.path_line = None, None
    
    def setup_visualization(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # Setup for animation
        self.robot_marker, = self.ax.plot([], [], 'ro', markersize=self.robot.robot_radius*2)
        self.path_line, = self.ax.plot([], [], 'b-', linewidth=1.0, alpha=0.8)
    
    def init_animation(self):
        self.ax.set_xlim(0, self.robot.arena_size)
        self.ax.set_ylim(0, self.robot.arena_size)
        self.ax.set_title('Brownian Motion Robot Simulation')
        self.ax.set_xlabel('X position')
        self.ax.set_ylabel('Y position')
        self.ax.grid(True, linestyle='--', alpha=0.7)
        
        # Draw arena boundaries
        self.ax.plot([0, 0], [0, self.robot.arena_size], 'k-', linewidth=2)
        self.ax.plot([0, self.robot.arena_size], [0, 0], 'k-', linewidth=2)
        self.ax.plot([self.robot.arena_size, self.robot.arena_size], 
                    [0, self.robot.arena_size], 'k-', linewidth=2)
        self.ax.plot([0, self.robot.arena_size], 
                    [self.robot.arena_size, self.robot.arena_size], 'k-', linewidth=2)
        
        return self.robot_marker, self.path_line
    
    def update_animation(self, frame):
        """Update the animation for each frame"""
        # Move the robot
        self.robot.move()
        
        # Update the plot
        x_data, y_data = zip(*self.robot.path_history)
        self.path_line.set_data(x_data, y_data)
        self.robot_marker.set_data([self.robot.position[0]], [self.robot.position[1]])
        
        return self.robot_marker, self.path_line
    
    def run(self, visualize: bool = True, save_animation: bool = False, 
            filename: str = 'brownian_motion.gif', fps: int = 30):
        if visualize:
            self.setup_visualization()
            ani = animation.FuncAnimation(
                self.fig, self.update_animation, frames=self.num_steps,
                init_func=self.init_animation, blit=True, interval=1000/fps
            )
            
            if save_animation:
                # Save as gif
                ani.save(filename, writer='pillow', fps=fps)
                print(f"Animation saved as {filename}")
            
            plt.show()
        else:
            # Run simulation without visualization
            for _ in range(self.num_steps):
                self.robot.move()
        
        return self.robot.get_path_history()