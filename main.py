from get_request import get_request
from matplotlib import pyplot as plt

# url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99"
# url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=7e0ff61e94ceb5aebb213f9782798eae"
lat = 44.34
lon = 10.99
start = 1369728000
end = 1369789200
# url = "https://history.openweathermap.org/data/2.5/history/city?lat=44.34&lon=10.99&type=hour&start=1369728000&end=" \
#       "1369789200"
url = "https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99"

data = get_request(url)
temperature = []
for i in range(len(data)):
    temperature.append(data[i]['main']['temp'])

print(temperature)

plt.plot(temperature)
plt.ylabel("[K]")
plt.title("Temperature")
# plt.legend()
plt.tight_layout()
plt.savefig("plot.png", dpi=1200)
