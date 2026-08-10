from camp_project.markov import simulate, empirical_frequency


def test_simulate_degenerate():
    P = [[1.0, 0.0], [0.0, 1.0]]

    path = simulate(P, 5)

    assert path == [0, 0, 0, 0, 0]

def test_empirical_frequency():
    path = [0, 0, 0, 1]

    frequencies = empirical_frequency(path)

    assert frequencies == {0: 0.75, 1: 0.25}