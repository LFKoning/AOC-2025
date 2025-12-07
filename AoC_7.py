import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    manifold = """
    .......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    """
    return (manifold,)


@app.cell
def _(manifold):
    start_x = start_y = 0
    manifold_mtx = []

    # Process the input for starting and splitter positions.
    for y, row in enumerate(manifold.split()):
        manifold_mtx.append([])
        for x, char in enumerate(row):
            if char == "S":
                start_x = x
                start_y = y
            elif char == "^":
                manifold_mtx[y].append(1)
            else:
                manifold_mtx[y].append(0)

    # Store matrix dimension
    manifold_rows = len(manifold_mtx)
    return manifold_mtx, manifold_rows, start_x, start_y


@app.cell
def _(manifold_mtx, manifold_rows):
    # Keep track of duplicates.
    splitters = set()
    duplicates = set()

    def trace_beam(start_x: int, start_y: int) -> None:
        """Trace a single beam until it hits a splitter or max row."""
        print(f"Tracing beam from: {start_x}, {start_y}")
        for y in range(start_y, manifold_rows):
            if manifold_mtx[y][start_x]:
                # Note: splitter can be hit by multiple unique beams.
                splitters.add((start_x, y))
                print(f"Encountered splitter at: {start_x}, {y}")

                # Trace child beams, skipping duplicates.
                # Should check bounds here??
                if (start_x - 1, y) not in duplicates:
                    duplicates.add((start_x - 1, y))
                    trace_beam(start_x - 1, y)

                if (start_x + 1, y) not in duplicates:
                    duplicates.add((start_x + 1, y))
                    trace_beam(start_x + 1, y)

                # Stop the beam.
                return

        # Beam reached end without getting split.
        print(f"Beam ended at: {start_x}, {y}")
    return splitters, trace_beam


@app.cell
def _(start_x, start_y, trace_beam):
    trace_beam(start_x, start_y)
    return


@app.cell
def _(splitters):
    # Print the locations of the splitters hit by a beam.
    print(sorted(splitters, key=lambda loc: loc[1]))
    return


@app.cell
def _(splitters):
    print("Number of splits: ", len(splitters))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
