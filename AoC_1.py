import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    rotations = (
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    )
    return (rotations,)


@app.cell
def _():
    def rotate(rotation: str, start: int) -> int:
        """Perform a single rotation."""
        if rotation.startswith("L"):
            print("Rotating: LEFT")
            mult = -1
        elif rotation.startswith("R"):
            print("Rotating: RIGHT")
            mult = 1
        else:
            raise ValueError(f"Invalid rotation direction: {rotation[0]}")

        try:
            distance = mult * int(rotation[1:])
            print(f"Rotating distance: {distance}")
        except (ValueError, TypeError):
            raise ValueError(f"Invalid rotation distance: {rotation[1:]}")

    
        current = start + distance 
        if current < 0:
            current = 100 + current
        elif current > 99:
            current = current - 100

        print(f"New postion: {current}")
        return current


    def rotate_all(rotations: list[str], position: int = 50) -> int:
        """Perform a series of rotations."""
        positions = []
        for rotation in rotations:
            position = rotate(rotation, position)
            positions.append(position)
        return position, len([_ for _ in positions if _ == 0])
    return (rotate_all,)


@app.cell
def _(rotate_all, rotations):
    rotate_all(rotations, 50)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
