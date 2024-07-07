import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify, symbols, cos, sin, tan, log


class Grapher:
    try:
        def __init__(self):
            """
            Initializes the Grapher class with a predefined set of mathematical functions.
            These functions are used to map string representations to their corresponding SymPy functions.
            """
            self.function_mapping = {
                "cos": cos,
                "sin": sin,
                "tan": tan,
                "log": log,
            }

        def preprocess_formula(self, formula_str):
            """
            Preprocesses the input formula string by replacing string representations of mathematical functions
            with their corresponding SymPy functions. This step ensures that the formula can be evaluated correctly later.

            Parameters:
            - formula_str: A string representing the mathematical formula to be plotted.

            Returns:
            - processed_formula: The preprocessed formula string ready for evaluation.
            """
            if not isinstance(formula_str, str):
                raise TypeError("The formula must be a string.")

            processed_formula = formula_str
            for func_name, sym_func in self.function_mapping.items():
                if sym_func is not None:
                    processed_formula = processed_formula.replace(func_name, str(sym_func))

            return processed_formula

        @staticmethod
        def construct_expression(processed_formula):
            """
            Constructs the mathematical expression from the preprocessed formula string and prepares it for evaluation.

            Parameters:
            - processed_formula: The preprocessed formula string obtained from the preprocess_formula method.

            Returns:
            - expr: The mathematical expression ready for evaluation.
            - x_sym: The symbolic representation of 'x' used in the expression.
            """
            if not isinstance(processed_formula, str):
                raise TypeError("The processed formula must be a string.")

            x_sym = symbols('x')
            expr_str = processed_formula.replace("x", "x_sym")
            try:
                expr = eval(expr_str)
            except Exception as e:
                raise ValueError(f"Failed to evaluate the expression due to an error: {e}")

            return expr, x_sym

        def generate_plot(self, formula_str, start, end):
            """
            Generates and displays a plot of the given mathematical formula over the specified range.

            Parameters:
            - formula_str: A string representing the mathematical formula to be plotted.
            - start: The starting value of the x-axis range.
            - end: The ending value of the x-axis range.

            Raises:
            - TypeError: If the formula_str is not a string.
            - ValueError: If the start or end values are not numbers.
            """
            if not isinstance(formula_str, str):
                raise TypeError("The formula must be a string.")

            if not (isinstance(start, (int, float)) and isinstance(end, (int, float))):
                raise ValueError("Start and end values must be numbers.")

            processed_formula = self.preprocess_formula(formula_str)
            expr, x_sym = self.construct_expression(processed_formula)
            formula = lambdify(x_sym, expr, 'numpy')

            x = np.linspace(start, end, 400)
            y = formula(x)

            plt.figure(figsize=(10, 6))
            plt.plot(x, y)
            plt.title('Graph of {}'.format(formula_str))
            plt.xlabel('X Value')
            plt.ylabel('Answer')
            plt.grid(True)
            plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


'''
# Example usage
grapher = Grapher()
grapher.generate_plot(FORMULA, START_VALUE, END_VALUE)

Formula must include (x) and nothing else in it, like x + 5.

Formula can support any function from the default python module, as well as cos, tan, sin and log.
Prioritizes BODMAS where brackets come first, etc
'''
