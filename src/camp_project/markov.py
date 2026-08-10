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