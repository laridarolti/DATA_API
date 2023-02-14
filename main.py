from get_request import get_request
from matplotlib import pyplot as plt
from json_to_df import json_to_df


url = "https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99"

lat = 44.34
lon = 10.99
start = 1369728000
end = 1369789200


data = get_request(url)
df = json_to_df(data)
plt.plot(df)
plt.ylabel("[K]")
plt.title("Temperature")
plt.tight_layout()
plt.savefig("plot.png", dpi=1200)
