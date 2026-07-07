from pathlib import Path
import pandas as pd

NASA_COLUMNS = [
    "unit",
    "cycle",
    "op_setting_1",
    "op_setting_2",
    "op_setting_3",
]

NASA_COLUMNS += [
    f"sensor_{i}"
    for i in range(1,22)
]


class NasaCMAPSSLoader:

    def __init__(
        self,
        dataset_root: str
    ):

        self.dataset_root = Path(
            dataset_root
        )

    def load_train(
        self,
        subset="FD001"
    ):

        file_path = (
            self.dataset_root
            /
            f"train_{subset}.txt"
        )

        return self._load(
            file_path
        )

    def load_test(
        self,
        subset="FD001"
    ):

        file_path = (
            self.dataset_root
            /
            f"test_{subset}.txt"
        )

        return self._load(
            file_path
        )

    def load_rul(
        self,
        subset="FD001"
    ):

        file_path = (
            self.dataset_root
            /
            f"RUL_{subset}.txt"
        )

        return pd.read_csv(
            file_path,
            header=None
        )

    def _load(
        self,
        file_path
    ):

        df = pd.read_csv(
            file_path,
            sep=r"\s+",
            header=None
        )

        df = df.iloc[:, :26]

        df.columns = NASA_COLUMNS

        return df