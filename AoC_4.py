import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    diagram = """
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    """
    return (diagram,)


@app.cell
def _(diagram):
    # Convert to numerical matrix.
    matrix = [
        list(1 if pos == "@" else 0 for pos in row)
        for row in diagram.split()
    ]
    matrix[0]
    return (matrix,)


@app.function
def get_adjacent(pos_x, pos_y, matrix):
    """Return a list of adjacent values."""
    # Matrix dimensions
    width = len(matrix[0])
    height = len(matrix)

    # Get 8 adjacent positions.
    adjacent = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # Skip self.
            if dx == 0 and dy == 0:
                continue
            
            x = pos_x + dx
            y = pos_y + dy

            # Handle out of matrix bounds.
            if x < 0 or x >= width or y < 0 or y >= height:
                adjacent.append(0)

            else:
                adjacent. append(matrix[y][x])
    
    return adjacent


@app.cell
def _(matrix):
    # Compute number of reachable squares.
    reachable = []
    for y in range(len(matrix)):
        # Initialize the row.
        reachable.append([])
    
        for x in range(len(matrix[y])):
            # Not a roll of paper.
            if matrix[y][x] == 0:
                print(f"row: {y}, position {x}: no roll")
                reachable[y].append(0)
                continue
        
            # Get adjacent values.
            adjacent = get_adjacent(x, y, matrix)
            print(f"row: {y}, position {x}: {sum(adjacent)} adjacent")
        
            # Check reachability.
            if sum(adjacent) < 4:
                reachable[y].append(1)
            else:
                reachable[y].append(0)
    return (reachable,)


@app.cell
def _(matrix, reachable):
    # Check output.
    output_str = ""
    for row_idx, row in enumerate(reachable):
        for pos_idx, pos in enumerate(row):
            if pos == 1:
                output_str += "X"
            elif matrix[row_idx][pos_idx] == 1:
                output_str += "@"
            else:
                output_str += "."
        output_str += "\n"

    print(output_str)
    return


@app.cell
def _(reachable):
    # Compute total reachable squares.
    sum([
      sum(row) for row in reachable  
    ])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
