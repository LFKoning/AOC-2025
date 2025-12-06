import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    sheet = """
    123 328  51 64 
     45 64  387 23 
      6 98  215 314
    *   +   *   + 
    """
    return (sheet,)


@app.cell
def _():
    # Make some classes to handle operations.
    class Operator:
        """Base class for share functionality."""

        def __init__(self):
            self._values = []

        @classmethod
        def create(cls, operator_str):
            if operator_str == "+":
                return AddOperator()
            elif operator_str == "*":
                return MultOperator()
            else:
                raise ValueError(f"Invalid operator: {operator_str}")

        def add(self, value):
            try:
                self._values.append(int(value))
            except (ValueError, TypeError):
                raise ValueError(f"Could not convert value to integer: {value}")

        def __repr__(self):
            return f"{self.__class__.__name__}()"


    class AddOperator(Operator):
        """Addition operator."""

        @property
        def result(self):
            return sum(self._values)


    class MultOperator(Operator):
        """Multiplication operator"""

        @property
        def result(self):
            result = 1
            for value in self._values:
                result *= value
            return result
    return (Operator,)


@app.cell
def _(sheet):
    # Preprocess the input.
    # Note: assuming the input is always a square matrix
    # with operators on the last line...
    lines = sheet.strip().split("\n")
    return (lines,)


@app.cell
def _(Operator, lines):
    # Create Operators.
    operators = []
    for op in lines[-1].split():
        operators.append(Operator.create(op))
    operators
    return (operators,)


@app.cell
def _(lines, operators):
    # Process the values.
    for line in lines[:-1]:
        for idx, value in enumerate(line.split()):
            operators[idx].add(value)
    return


@app.cell
def _(operators):
    # Compute results.
    [op.result for op in operators]
    return


@app.cell
def _(operators):
    # Compute sum of the results.
    sum([op.result for op in operators])
    return


if __name__ == "__main__":
    app.run()
