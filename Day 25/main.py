import csv
import pandas


data = pandas.read_csv("squirell_data.csv")
#how many of each color:

color_cin = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(color_cin)
color_gray = len(data[data["Primary Fur Color"] == "Gray"])
color_black = len(data[data["Primary Fur Color"] == "Black"])

thisdict= {
  "Fur Color": ["Cinnamon", "Gray", "Black"],
  "Count": [color_cin, color_gray, color_black]
  
}
df = pandas.DataFrame(thisdict)
df.to_csv("squirell_dict.csv", index=False)