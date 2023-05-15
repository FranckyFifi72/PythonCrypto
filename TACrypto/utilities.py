from pandas import DataFrame
import pandas as pd
import datetime as datetime


def get_data_frame(data):
    df: DataFrame = pd.DataFrame(data, columns=['Timestamp', "Open", "High", "Low", "Close", "Volume"])
    df["Timestamp"] = df["Timestamp"].apply(lambda x: ms_to_dt_local(x))
    df['Date'] = df["Timestamp"].dt.strftime("%d/%m/%Y")
    df['Time'] = df["Timestamp"].dt.strftime("%H:%M:%S")
    column_names = ["Date", "Time", "Open", "High", "Low", "Close", "Volume"]
    df = df.set_index('Timestamp')
    df = df.reindex(columns=column_names)

    return df


def ms_to_dt_utc(ms: int) -> datetime:
    return datetime.datetime.utcfromtimestamp(ms / 1000)


def ms_to_dt_local(ms: int) -> datetime:
    return datetime.datetime.fromtimestamp(ms / 1000)
