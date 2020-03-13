def PenentuNilai(nilai):
	if(nilai<= 100 and nilai >= 80):
		print("Maka anda mendapat A ")
	elif (nilai <80 and nilai >=70):
		print("Maka anda mendapat B")
	elif(nilai <70 and nilai >=60):
		print("Maka anda mendapat C")
	elif(nilai < 60 and nilai >=40):
		print("Maka anda mendapat D")
	elif(nilai <40 and nilai >=0):
		print("Maka anda mendapat E")
	else:
		print("Format yang anda masukan salah")
		
bilangan = int(input("Masukan Nilai : "))
print ("Jika nilai anda ",bilangan)  
PenentuNilai(bilangan)



