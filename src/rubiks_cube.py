# rubiks_cube.py

import pycuber as pc
import random

class RubiksCube:
    def __init__(self):
        # Initialize the cube in a solved state using pycuber
        self.cube = pc.Cube()

    def apply_move(self, move):
        # Apply a move to the cube
        try:
            self.cube(sequence=move)
        except Exception as e:
            print(f"Invalid move: {e}")

    def is_solved(self):
        # Check if the cube is solved
        return self.cube.is_solved()

    def scramble(self, moves=20):
        # Scramble the cube with a sequence of random moves
        move_list = ['U', 'D', 'L', 'R', 'F', 'B', 'U\'', 'D\'', 'L\'', 'R\'', 'F\'', 'B\'']
        scramble_moves = random.choices(move_list, k=moves)
        for move in scramble_moves:
            self.apply_move(move)

    def get_state(self):
        # Get the current state of the cube
        return str(self.cube)

    def display(self):
        # Display the cube's state in a readable format
        print(self.cube)

# Example usage:
if __name__ == "__main__":
    cube = RubiksCube()
    print("Initial Cube State:")
    cube.display()

    print("\nScrambling Cube...")
    cube.scramble()
    cube.display()

    print("\nIs the cube solved?", cube.is_solved())

''