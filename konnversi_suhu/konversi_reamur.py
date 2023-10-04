#konversi suhu ramur ke celcius/fahrenheit/kelvin

#konversi reamur ke satuan lain

print("\nPROGRAM KONVRSI TEMPERATUR\n")

reamur = float(input("masukan suhu dalam reamur : "))
print("suhu dalam reamur", reamur, "Reamur")

#reamur -> celcius
kelvin = ((5/4) * reamur)
print("=> suhu dalam kelvin adalah", kelvin,"Kelvin")

#reamur -> fahrenheit
celcius = ((9/4 * reamur + 32))
print("=> suhu dalam celcius adalah", celcius,"Celcius")

#reamur -> kelvin
kelvin = ((5/4) * reamur + 273)
print("=> suhu dalam kelvin adalah", kelvin,"Kelvin")
