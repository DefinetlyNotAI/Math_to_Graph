import argparse
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
import numpy as np

def main():
    # Define the argument parser
    parser = argparse.ArgumentParser(description='Plot mathematical functions.')

    # Add arguments
    parser.add_argument('--formula1', type=str, help='Mathematical formula to plot')
    parser.add_argument('--formula2', type=str, help='Mathematical formula to plot')
    parser.add_argument('--formula3', type=str, help='Mathematical formula to plot')
    parser.add_argument('--formula4', type=str, help='Mathematical formula to plot')

    # Parse arguments
    args = parser.parse_args()

    # Ensure at least one formula is provided
    if not any([args.formula1, args.formula2, args.formula3, args.formula4]):
        print("Please provide at least one formula.")
        return

    # Prepare data for plotting
    x = symbols('x')
    plots = []

    # Process each formula
    for i, formula_str in enumerate(['formula1', 'formula2', 'formula3', 'formula4'], start=1):
        if getattr(args, f'formula{i}') is not None:
            # Directly use the formula string passed as an argument
            formula = sympify(getattr(args, f'formula{i}').replace('x', 'x'))

            # Create a lambda function for plotting
            y = lambdify(x, formula, "numpy")(np.arange(-10, 11))
            plots.append((f"Formula {i}", y))

    # Plotting
    fig, ax = plt.subplots()
    for label, y in plots:
        ax.plot(np.arange(-10, 11), y, label=label)  # Ensure x values are plotted

    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
