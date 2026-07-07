from src.data.nasa_loader import (
    NasaCMAPSSLoader
)

def test_fd001():

    loader = NasaCMAPSSLoader(
        "data"
    )

    train_df = loader.load_train(
        "FD001"
    )

    assert (
        train_df.shape[1]
        == 26
    )