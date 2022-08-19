import os
import argparse
import pandas
import pandas as pd


def read_power_csv(path_to_csv: str, mode: int):
    # power_consumption
    if mode == mode:
        df = pd.read_csv(path_to_csv)
    # power_generation
    elif mode == mode:
        df = pd.read_csv(path_to_csv)
    return df


if __name__ == '__main__':
    def main():
        parser = argparse.ArgumentParser()
        # region =====path_csv======
        parser.add_argument('-i', '--power_csv', type=str, required=False, help="path to excel")
        parser.add_argument('mode', type=int, help='dataset mode')
        # endregion ================
        args = parser.parse_args()
        path_to_csv = args.power_csv
        mode = args.mode

        df = read_power_csv(path_to_csv, mode)
        print(df)

    main()
