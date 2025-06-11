#!/usr/bin/env python3
# Created by: Hiab G
# Created on: June 9


import math


# function to calculate distance using distance formula
def calculate_distance(x1, y1, x2, y2):

    # Distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance


def main():
    try:
        # Getting user input for the 4 points
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        # checks if the given points are the same
        if x1 != x2 or y1 != y2:
            # checks if the given points are equal to 0
            if x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
                distance = calculate_distance(x1, y1, x2, y2)
                print(f"Distance: {calculate_distance(x1, y1, x2, y2)}")
            else:
                print("All points are at origin.")
        else:
            print("There's no distance between given points.")

    except Exception:
        print("Invalid input! Please enter numbers.")


if __name__ == "__main__":
    main()
