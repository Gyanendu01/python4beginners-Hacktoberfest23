print("\tWelcome To The Temperature Conversion App")

#Input Data
while True:
    tmp_faren = float(input("\n\tWhat is the temperature in degrees Farhnheit? "))
    if tmp_faren > 0:
        break

#Logic for Conversion
tmp_kelvin =  (tmp_faren - 32) * (5 / 9) + 273.15
tmp_kelvin = round(tmp_kelvin , 4)
tmp_celcius = (tmp_faren - 32) * 5/9
tmp_celcius = round(tmp_celcius, 4)
data = dict()

#Storing Elements in Dict
data["Degrees Farenheit"] = tmp_faren
data["Degrees Celsius"] = tmp_celcius
data["Degrees Kelvin"] = tmp_kelvin

#Display Elements
for i,j in data.items():
    print("\n\t{}                   {}".format(i,j))
