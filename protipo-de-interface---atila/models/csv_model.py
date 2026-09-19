import os
import pandas as pd

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

class CSVModel:
    def __init__(self, filename, columns):
        self.path = os.path.join(BASE, filename)
        self.columns = columns
        os.makedirs(BASE, exist_ok=True)
        if not os.path.exists(self.path):
            pd.DataFrame(columns=columns).to_csv(self.path, index=False, encoding="utf-8-sig")

    def all(self):
        return pd.read_csv(self.path, dtype=str).fillna("")

    def save(self, df):
        df.to_csv(self.path, index=False, encoding="utf-8-sig")
