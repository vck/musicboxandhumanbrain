import pandas
import matplotlib.pyplot as plt
data_exception = [43.0, 53.0]
new_data = []
source_url = "http://pastebin.com/raw.php?i=y16ecx3v"

def getData(url):
    if url:
        return pandas.read_csv(url, header=None).values
    else:
        pass

def dataFilter(data):
    for d in data:
        if d not in data_exception:
            new_data.append(d)
    return new_data

# next up
# bring the data to the visualization sequence

plt.plot(dataFilter(getData(source_url)))
plt.show()

