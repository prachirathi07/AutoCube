# test_rubiks_cube.py

import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rubiks_cube import RubiksCube

def main():
    cube = RubiksCube()
    print("Initial Solved State:")
    cube.display()

    cube.scramble(moves=10)
    print("\nScrambled State:")
    cube.display()

    print("\nIs Solved?", cube.is_solved())

    # Attempt to solve (using the library's solve method if available)
    # For now, we'll assume it's unsolved
    # Implement solving logic or use the library's solver if available

if __name__ == "__main__":
    main()
