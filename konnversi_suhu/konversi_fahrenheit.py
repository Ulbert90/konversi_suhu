#konversi fahrenheit ke celcius/reamur/kelvin

#konversi fahrenheit ke satuan lain

print("\nPROGRAM KONVRSI TEMPERATUR\n")

fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
print("suhu dalam fahrenheit", fahrenheit, "fahrenheit")


#fahrenheit -> celcius
celcius = ((5/9) * (fahrenheit + 32))
print("=> suhu dalam celcius adalah", celcius,"Celcius")

#fahrenheit -> reamur
reamur = ((4/9) * (fahrenheit - 32))
print("=> suhu dalam reamur adalah", reamur,"Reamur")

#fahrenheit -> kelvin
kelvin = ((5/9) * (fahrenheit - 32) + 273)
print("=> suhu dalam kelvin adalah", kelvin,"Kelvin")