def PenentuNilai(nilai):
...     if(nilai<=100 and nilai >=80):
...             print("Nilai A")
...     elif(nilai<80 and nilai >=70):
...             print("Nilai B")
...     elif(nilai<70 and nilai >=60):
...             print("Nilai C")
...     elif(nilai <60 and nilai >=40):
...             print("Nilai D")
...     elif(nilai <40 and nilai >=0):
...             print("Nilai E")
...     else:
...             print("Format yang anda masukan salah ")
...
>>> PenentuNilai(200)
Format yang anda masukan salah
>>> PenentuNilai(100)
Nilai A
>>> PenentuNilai(80)
Nilai A
>>> PenentuNilai(79)
Nilai B
>>> PenentuNilai(70)
Nilai B
>>> PenentuNilai(68)
Nilai C
>>> PenentuNilai(60)
Nilai C
>>> PenentuNilai(59)
Nilai D
>>> PenentuNilai(40)
Nilai D
>>> PenentuNilai(38)
Nilai E
>>> PenentuNilai(-90)
Format yang anda masukan salah
>>>