"""Data handler module for loading and processing data."""

from typing import Optional, List, Union

import os
import numpy as np
import pandas as pd
#from openbb import obb
from qlib.data import D
import qlib
qlib.init()

class DataHandler:
    """Data handler class for loading and processing data."""

    def __init__(
        self,
        symbol,#: Union[str, List[str]],
        fields,#: Union[str, List[str]],
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        region: str = "cn",
        freq: str = "day",
        base_path: str = '/Users/zhangqunying/.qlib/qlib_data'
    ):
        """Initialize the data handler.
        :param region: cn, us
        :param freq: day, 1min
        """
        self.symbol = symbol if isinstance(symbol, list) else [symbol]
        self.start_time = start_time
        self.end_time = end_time
        self.region = region
        self.freq = freq
        self.fields = fields if isinstance(fields, list) else [fields]
        if freq == 'day':
            dir_name = f'{region}_data'
        else:
            dir_name = f'{region}_data_{freq}'
        self.base_path = os.path.join(base_path, dir_name,'features')
        self.calendar_path = os.path.join(base_path, dir_name, 'calendars', f'{freq}.txt')

    def read_calendar(self):
        # with open(self.calendar_path, 'r') as file:
        #     timestamps = [line.strip() for line in file]
        # start_idx = timestamps.index(self.start_time) if self.start_time in timestamps else None
        # end_idx = timestamps.index(self.end_time) if self.end_time in timestamps else None
        # return timestamps[start_idx:end_idx + 1], start_idx, end_idx
        return D.calendar(start_time=self.start_time, end_time=self.end_time, freq=self.freq)


    def load_data(self):

        return D.features(
            self.symbol,
            self.fields,
            start_time=self.start_time,
            end_time=self.end_time,
        )


# # Example usage:
# loader = DataHandler(symbol=["sh600008", "sh600009"], fields=["close", "high"], freq="1min", region="cn")
# df = loader.load_data()
# print(df.head())


    def load_data_from_csv(self, file_path) -> pd.DataFrame:
        """Load data from CSV file."""
        return pd.read_csv(file_path, index_col="date", parse_dates=True)
