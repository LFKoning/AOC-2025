import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    # Invalid IDs

    return


@app.cell
def _():
    id_str = """
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124
    """
    return (id_str,)


@app.cell
def _(id_str):
    id_ranges = id_str.strip().split(",")
    id_ranges
    return (id_ranges,)


@app.cell
def _(id_ranges):
    invalid = []
    for id_range in id_ranges:
        # Split string to get low and high boundaries.
        low, high = id_range.split("-")
        numbers = range(int(low), int(high) + 1)

        # Loop over the number range.
        for number in numbers:
            # Split the string in two halves.
            number_str = str(number)
            mid = len(number_str) // 2
            left = number_str[:mid]
            right = number_str[mid:]
        
            # Check for repitition; invalid if repeated.
            if left == right:
                invalid.append(number)

    # All invalid IDs.
    invalid
    return (invalid,)


@app.cell
def _(invalid):
    # Sum of the invalid IDs.
    sum(invalid)
    return


if __name__ == "__main__":
    app.run()
