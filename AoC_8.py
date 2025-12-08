import marimo

__generated_with = "0.18.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from typing import Self
    from math import sqrt
    from itertools import combinations
    return Self, combinations, sqrt


@app.cell
def _(Self, sqrt):
    class Junction:
        """Junction box as a 3D coordinate."""

        def __init__(self, x: int, y: int, z: int) -> None:
            self.x = int(x)
            self.y = int(y)
            self.z = int(z)

        def distance_to(self, other: Self) -> float:
            """Distance to another junction box."""
            return sqrt(
                (other.x - self.x) ** 2 +
                (other.y - self.y) ** 2 +
                (other.z - self.z) ** 2
            )

        def __repr__(self) -> str:
            """Return representation of self."""
            return f"Junction({self.x}, {self.y}, {self.z})"

        def __str__(self) -> str:
            """Return string representation of self."""
            return f"({self.x:3d}, {self.y:3d}, {self.z:3d})"
    return (Junction,)


@app.cell
def _():
    junction_str = """
    162,817,812
    57,618,57
    906,360,560
    592,479,940
    352,342,300
    466,668,158
    542,29,236
    431,825,988
    739,650,466
    52,470,668
    216,146,977
    819,987,18
    117,168,530
    805,96,715
    346,949,466
    970,615,88
    941,993,340
    862,61,35
    984,92,344
    425,690,689
    """
    return (junction_str,)


@app.cell
def _(Junction, junction_str):
    # Parse input into Juntions.
    junctions = []
    for row in junction_str.strip().split():
        x, y, z = row.split(",")
        junctions.append(Junction(x, y, z))
    return (junctions,)


@app.cell
def _(Junction, combinations, junctions):
    # Compute pairwise distances.
    def compute_distances(junctions: list[Junction]) -> list[tuple]:
        """Compute pairwise distances between junctions."""
        distances = []
        for (left, right) in combinations(junctions, 2):
            distance = left.distance_to(right)
            print(f"Distance {left} - {right}: {distance:8.2f}")
            distances.append((distance, left, right))
        return distances

    distances = compute_distances(junctions)
    return (distances,)


@app.function
def create_circuits(distances: list[tuple], connect_max: int) -> list:
    """Create circuits by connecting the shortest distances between junctions."""
    # Keep track of connections and circuits.
    n_connections = 1
    connected = {}
    circuits = []
    
    # Connect junctions with shortest distances into curcuits.
    for distance, left, right in sorted(distances, key=lambda c: c[0]):
        
        # Both left and right are already part of a circuit.abs
        if left in connected and right in connected:
            print(f"Both {left} and {right} already connected, skipping...")
            continue

        print(f"Creating connection: {n_connections}")
        
        # Left is part of an existing circuit.
        if left in connected:
            circuit_idx = connected[left]
            circuits[circuit_idx].add(right)
            connected[right] = circuit_idx
            print(f"Connected {right} to existing circuit {circuit_idx}.")
    
        # Right is part of an existing circuit.
        elif right in connected:
            circuit_idx = connected[right]
            circuits[circuit_idx].add(left)
            connected[left] = circuit_idx
            print(f"Connected {left} to existing circuit {circuit_idx}.")
    
        # Create a new circuit.
        else:
            circuit_idx = len(circuits)
            circuits.append(set((left, right)))
    
            # Store junction <-> circuit connections.
            connected[left] = circuit_idx
            connected[right] = circuit_idx
            print(f"Created circuit {circuit_idx} from {left} and {right}.")
    
        # Stopping at max connections.
        n_connections += 1
        if n_connections > connect_max:
            print(f"Reached maximum number of connections: {connect_max}")
            break

    return circuits


@app.cell
def _(distances):
    # Shortest distances between junctions
    sorted(distances, key=lambda c: c[0])[:10]
    return


@app.cell
def _(distances):
    # Maximum number of connections to make.
    connect_max = 10
    create_circuits(distances, connect_max)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
