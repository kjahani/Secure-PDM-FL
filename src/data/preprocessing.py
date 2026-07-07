import pandas as pd
from sklearn.preprocessing import MinMaxScaler

SELECTED_SENSORS = [
    "sensor_2",
    "sensor_3",
    "sensor_4",
    "sensor_7",
    "sensor_11",
    "sensor_12",
    "sensor_15",
    "sensor_20",
    "sensor_21"
]


class CMAPSSPreprocessor:

    def __init__(self):

        self.scaler = MinMaxScaler()

    def fit_transform(
        self,
        df: pd.DataFrame
    ):

        df = df.copy()

        df[
            SELECTED_SENSORS
        ] = self.scaler.fit_transform(

            df[
                SELECTED_SENSORS
            ]

        )

        return df

    def transform(
        self,
        df
    ):

        df = df.copy()

        df[
            SELECTED_SENSORS
        ] = self.scaler.transform(

            df[
                SELECTED_SENSORS
            ]

        )

        return df