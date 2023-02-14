import pandas as pd


def json_to_df(data):
    temperature = []
    df = pd.DataFrame()
    for i in range(len(data)):
        temperature.append(data[i]['main']['temp'])

    df["temperature"] = temperature
    return df
