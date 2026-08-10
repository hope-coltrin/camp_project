from camp_project.markov import simulate


def test_simulate_degenerate():
    P = [[1.0, 0.0], [0.0, 1.0]]

    path = simulate(P, 5)

    assert path == [0, 0, 0, 0, 0]