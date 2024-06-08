"""Main module for running the backtester."""

from backtester.data_handler import DataHandler
from backtester.backtester import Backtester
from backtester.strategies import Strategy


def main():
    """Example usage of the backtester."""
    symbol = "sh600008"
    start_time = "1999-11-26" #"2020-09-14 09:32:00" #"2023-01-01"
    end_time = "2001-12-14" #"2020-09-14 14:32:00" #"2023-12-31"
    freq = "day" #"1min"
    fields = "$close" #["close", "high"]
    region = "cn"
    path = r'/Users/zhangqunying/.qlib/qlib_data'

    data = DataHandler.load_data(symbol, fields, start_time, end_time)

    # Define your strategy, indicators, and signal logic here
    strategy = Strategy(
        indicators={
            "sma_20": lambda row: row["$close"].rolling(window=20).mean(),
            "sma_60": lambda row: row["$close"].rolling(window=60).mean(),
        },
        signal_logic=lambda row: 1 if row["sma_20"] > row["sma_60"] else -1,
    )
    data = strategy.generate_signals(data)

    backtester = Backtester()
    backtester.backtest(data)
    backtester.calculate_performance()


if __name__ == "__main__":
    main()

# import struct
#
# # Define the file path
# file_path = r'/Users/zhangqunying/.qlib/qlib_data/cn_data_day/features/sh600008/close.day.bin'
#
# # Open the file in binary read mode
# with open(file_path, 'rb') as file:
#     # Read the binary data
#     binary_data = file.read()
#
#     # Determine the number of integers (assuming each integer is 4 bytes)
#     num_integers = len(binary_data) // 4
#
#     # Unpack the binary data into a list of integers
#     integers = struct.unpack(f'{num_integers}i', binary_data)
#
#     # Print the list of integers
#     print(integers)



