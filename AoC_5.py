import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    data = """
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
    """
    return (data,)


@app.cell
def _(data):
    def parse_range(range_str):
        """Parse range string into low, high tuple."""
        low, high = range_str.split("-")
        return int(low), int(high)


    # Process the data into ranges and items.
    ranges = []
    items = []
    for record in data.strip().split():
        if "-" in record:
            ranges.append(parse_range(record))
        else:
            items.append(int(record))
    return items, ranges


@app.cell
def _(ranges):
    # Make sure ranges are sorted by their lower bound.
    sranges = sorted(ranges)
    return (sranges,)


@app.cell
def _(items, sranges):
    # Check items fall in a freshness range.
    fresh = []
    for item in items:
        print(f"Processing item: {item}")
        for (low, high) in sranges:
            # Item won't be in higher ranges
            if item < low:
                break

            # Falls in range, thus fresh.
            if item >= low and item <= high:
                print(f"Item falls in range: {low} - {high}")
                fresh.append(item)
                # One range is sufficient.
                break
    return (fresh,)


@app.cell
def _(fresh):
    # Print fresh items.
    fresh
    return


@app.cell
def _(fresh):
    print(f"Number of fresh items: {len(fresh)}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
