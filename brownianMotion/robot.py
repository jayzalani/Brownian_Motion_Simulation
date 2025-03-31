import numpy as np
import random
from typing import Tuple, List

class BrownianRobot:
    """
    A robot that exhibits Brownian motion behavior within a square arena.
    
    The robot moves in straight lines and, upon collision with the arena boundaries,
    rotates for a random duration before continuing in the new direction.
    """
    
    def __init__(self, arena_size: int = 100, robot_radius: int = 2, speed: float = 0.5):
        self.arena_size = arena_size
        self.robot_radius = robot_radius
        self.speed = speed
        
        # Start in the middle of the arena
        self.position = np.array([arena_size/2, arena_size/2])        
        self.direction = 0.0       
        self.path_history = [tuple(self.position)]       
        self.is_rotating = False
        self.rotation_steps_remaining = 0
        self.rotation_speed = np.pi/10  
    
    def check_collision(self) -> Tuple[bool, str]:
        x, y = self.position
        
        if x - self.robot_radius <= 0:
            return True, "left"
        if x + self.robot_radius >= self.arena_size:
            return True, "right"
        if y - self.robot_radius <= 0:
            return True, "bottom"
        if y + self.robot_radius >= self.arena_size:
            return True, "top"
        
        return False, ""
    
    def start_rotation_after_collision(self, boundary: str) -> None:
        self.is_rotating = True
        self.rotation_steps_remaining = random.randint(5, 20)
        if boundary == "left":
            self.rotation_target = np.random.uniform(-np.pi/2, np.pi/2)
        elif boundary == "right":
            self.rotation_target = np.random.uniform(np.pi/2, 3*np.pi/2)
        elif boundary == "bottom":
            self.rotation_target = np.random.uniform(0, np.pi)
        elif boundary == "top":
            self.rotation_target = np.random.uniform(np.pi, 2*np.pi)
    
    def rotate(self) -> None:
        if self.rotation_steps_remaining > 0:
            angle_diff = (self.rotation_target - self.direction + np.pi) % (2 * np.pi) - np.pi
            if abs(angle_diff) < self.rotation_speed:
                self.direction = self.rotation_target
            else:
                rotation_direction = 1 if angle_diff > 0 else -1
                self.direction = (self.direction + rotation_direction * self.rotation_speed) % (2 * np.pi)
            
            self.rotation_steps_remaining -= 1
        else:
            self.is_rotating = False
    
    def move(self) -> None:
        if self.is_rotating:
            self.rotate()

            self.path_history.append(tuple(self.position))
        else:
    
            dx = self.speed * np.cos(self.direction)
            dy = self.speed * np.sin(self.direction)
            
            new_position = self.position + np.array([dx, dy])
            self.position = new_position
            
            has_collided, boundary = self.check_collision()
            
            if has_collided:

                x, y = self.position
                if boundary == "left":
                    x = self.robot_radius
                elif boundary == "right":
                    x = self.arena_size - self.robot_radius
                elif boundary == "bottom":
                    y = self.robot_radius
                elif boundary == "top":
                    y = self.arena_size - self.robot_radius
                
                self.position = np.array([x, y])
                
    
                self.path_history.append(tuple(self.position))
                
    
                self.start_rotation_after_collision(boundary)
            else:

                self.path_history.append(tuple(self.position))
    
    def get_position(self) -> Tuple[float, float]:
        return tuple(self.position)
    
    def get_path_history(self) -> List[Tuple[float, float]]:
        return self.path_history