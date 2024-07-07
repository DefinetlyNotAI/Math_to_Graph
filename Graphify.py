#!/usr/bin/env python

import argparse
from sympy import symbols, lambdify, evalf
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Initialize the parser
    parser = argparse.ArgumentParser(description="Plot mathematical functions.")

    # Add the arguments
    parser.add_argument('--formula1', type=str, help='Formula for the first function.')
    parser.add_argument('--formula2', type=str, help='Formula for the second function.')
    parser.add_argument('--formula3', type=str, help='Formula for the third function.')
    parser.add_argument('--formula4', type=str, help='Formula for the fourth function.')

    # Parse the arguments
    args = parser.parse_args()

    # Check if any formula is provided
    formulas = [args.formula1, args.formula2, args.formula3, args.formula4]
    valid_formulas = [formula for formula in formulas if formula]  # Remove empty strings

    # Define the variable(s)
    variables = 'x'
    if 'r' in valid_formulas[0]:
        variables += ', r'

    # Convert string formulas to lambda functions
    functions = {}
    for i, formula in enumerate(valid_formulas):
        # Extract the equation part after "f(x) = "
        equation_part = formula.split('=')[1].strip()
        # Use SymPy to evaluate the equation symbolically
        expr = eval(equation_part.replace('**', '^'), {variables: symbols(variables)})
        # Convert the expression to a lambda function
        func = lambdify(variables, expr, "numpy")
        functions[f"func{i + 1}"] = func

    # Generate x values
    x_values = np.linspace(-10, 10, 400)

    # Plot each function
    fig, ax = plt.subplots()
    colors = ['red', 'green', 'blue', 'orange']
    for i, (func_name, func) in enumerate(functions.items()):
        y_values = func(x_values)
        ax.plot(x_values, y_values, color=colors[i], label=f"{func_name}")

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Graphs of Functions')
    ax.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
