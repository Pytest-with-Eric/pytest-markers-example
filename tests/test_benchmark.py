def fetch_large_dataset():
    return list(range(100000))


def test_dataset_performance(benchmark):
    data = benchmark(fetch_large_dataset)
    assert len(data) == 100000
