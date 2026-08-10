import random


def simulate(P: list[list[float]], T: int, seed: int = 0) -> list[int]:
    """Simulate T steps of a Markov chain with matrix P.

    Definition:
        Starts at state 0 and uses the probabilities in P to randomly decide which state to move to next.

    Inputs:
        P: A matrix containing the probabilities of moving from each state to every other state.
        T: The number of states to include in the simulation.
        seed: Used to make the random results the same each time.

    Outputs:
        A list showing the states visited during the simulation.
    """
    for row in P:
        if abs(sum(row) - 1.0) > 1e-9:
            raise ValueError("Each row of P must add to 1.")

    rand = random.Random(seed)
    state = 0
    out = [state]

    for _ in range(T - 1):
        r = rand.random()
        probabilities = P[state]
        cumulative = 0.0

        for next_state in range(len(probabilities)):
            p = probabilities[next_state]
            cumulative += p

            if r < cumulative:
                state = next_state
                break

        out.append(state)

    return out

def empirical_frequency(path: list[int]) -> dict[int, float]:
    """Figure out how often each state appears in a path.

    Definition:
        Counts how many times each state appears in the path and divided each count by the number of states.

    Input:
        path: A list of states from the simulated Markov chain.

    Output:
        A dictionary showing the frequency of each state.
    """

    count = {}

    for state in path:
        if state in count:
            count[state] += 1
        else:
            count[state] = 1

    n = len(path)

    frequencies = {}

    for state, number in count.items():
        frequencies[state] = number / n

    return frequencies

def stationary_distribution(P: list[list[float]]) -> dict[int, float]:
    """Calculate the stationary distribution of a Markov chain.

    Definition:
        Calculates the probability of being in each state in the long run.

    Inputs:
        P: A matrix of the probabilities of moving from each state to the other states.

    Outputs:
        A dictionary showing the long run probability of each state.
    """
    p01 = P[0][1]
    p10 = P[1][0]

    prob0 = p10 / (p01 + p10)
    prob1 = p01 / (p01 + p10)

    return {0: prob0, 1: prob1}