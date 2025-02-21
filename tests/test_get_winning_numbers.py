from src.mega_sorteio import get_winning_numbers


def test_get_winning_numbers(monkeypatch):
    def mock_sample(range1, range2):
        return [10, 2, 35, 4, 7, 6]

    monkeypatch.setattr("random.sample", mock_sample)
    assert get_winning_numbers() == [2, 4, 6, 7, 10, 35]
