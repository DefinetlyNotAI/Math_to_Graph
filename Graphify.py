import argparse
import numpy as np
import matplotlib.pyplot as plt


def parse_arguments():
    parser = argparse.ArgumentParser(description='Plot multiple functions.')
    parser.add_argument('--formula1', type=str, default=None)
    parser.add_argument('--formula2', type=str, default=None)
    parser.add_argument('--formula3', type=str, default=None)
    parser.add_argument('--formula4', type=str, default=None)
    return parser.parse_args()


def plot_functions(formulas):
    # Generate x values
    x_values = np.linspace(-10, 10, 400)

    # Initialize figure and axes
    fig, ax = plt.subplots()

    # Plot each formula
    for i, formula in enumerate(formulas, start=1):
        y_values = eval(formula.replace('x', 'x_values'))
        ax.plot(x_values, y_values, label=f'Formula {i}')

    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graph of Functions')

    # Show legend
    ax.legend()

    # Display the plot
    plt.show()


if __name__ == '__main__':
    args = parse_arguments()

    # Filter out None values
    formulas = [args.formula1, args.formula2, args.formula3, args.formula4]
    formulas = [f for f in formulas if f is not None]

    if formulas:
        plot_functions(formulas)
    else:
        print("Please provide at least one formula.")
