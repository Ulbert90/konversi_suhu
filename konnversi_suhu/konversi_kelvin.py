#konversi suhu kelvin ke celcius/reamur/fahrenheit

#konversi kelvin ke satuan lain

print("\nPROGRAM KONVRSI TEMPERATUR\n")

kelvin = float(input("masukan suhu dalam kelvin : "))
print("suhu dalam kelvin", kelvin, "Kelvin")

#kelvin -> celcius
celcius =  + 273
print("=> suhu dalam kelvin adalah", celcius, "Celcius")

#kelvin -> reamur
reamur =  ((4/5) * (kelvin - 273))
print("=> suhu dalam ramur adalah", reamur, "Reamur")

#kelvin -> fahrenheit
fahrenheit = ((9/5) * (kelvin - 273) + 32)
print("=> suhu dalam fahrenheit adalah", fahrenheit,"Fahrenheit")
