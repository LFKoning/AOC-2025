import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    joltage_input = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    return (joltage_input,)


@app.cell
def _(joltage_input):
    banks = joltage_input.split()
    banks
    return (banks,)


@app.cell
def _(banks):
    all_maxed = []

    for bank in banks:
        # Find the first highest digit and its index.
        max = 0
        max_idx = 0
        for idx, number in enumerate(bank[:-1]):
            number = int(number)
            if number > max:
                max = number
                max_idx = idx

        # Store first digit.
        maxed = 10 * max
    
        # Find second highest digit.
        max = 0
        for number in bank[max_idx + 1:]:
            number = int(number)
            if number > max:
                max = number

        # Store maxed digits.
        maxed += max
        all_maxed.append(maxed)

    # Print maxed out banks
    all_maxed
    return (all_maxed,)


@app.cell
def _(all_maxed):
    # Maxed out joltage
    sum(all_maxed)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
