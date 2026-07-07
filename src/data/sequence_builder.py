import numpy as np

def build_sequences(
        features,
        targets,
        seq_length=30
):

    X = []
    y = []

    for i in range(
        len(features)
        -
        seq_length
    ):

        X.append(

            features[
                i:i+seq_length
            ]

        )

        y.append(

            targets[
                i+seq_length
            ]

        )

    return (
        np.array(X),
        np.array(y)
    )