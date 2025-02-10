#






dunyo_davlatlari = {
    'AQSH':'bishkek',
    'Italiya':'Dushanbe',
    'Malayziya':'kuala-lumpur',
    'Uzbekiston':'Moskva',
    'Qozoqiston':'Nursulton',
    'Rossiya':'Sungapur',
    'Singapur':'Toshkent',
    'Tojikiston':'Washington'

}
for davlat in sorted(dunyo_davlatlari):
    print(davlat)

for poytaxt in sorted(dunyo_davlatlari.values()):
    print(poytaxt)








#
dunyo_davlatlari = {
    'AQSH':'bishkek',
    'Italiya':'Dushanbe',
    'Malayziya':'kuala-lumpur',
    'Uzbekiston':'Moskva',
    'Qozoqiston':'Nursulton',
    'Rossiya':'Sungapur',
    'Singapur':'Toshkent',
    'Tojikiston':'Washington'

}
davlat = input("istagan davlatingizni kiriting: ")
if davlat.title() in dunyo_davlatlari:
    print(f"{davlat}ning poytaxti {dunyo_davlatlari[davlat]}.")
else:
    print("kechirasiz bunday davlat yoq")



oqatlar = {
    'osh':20000,
    'non':4000,
    'somso':10000,
    'shoshlik':30000
}

buyurtma = ['osh','non','manti']
for oqat in oqatlar:
    if oqat in buyurtma:
        print(f"{oqat.title()}{oqatlar[oqat]} som")

for taom in buyurtma:
    if taom not in oqatlar:
        print(f"kechirasiz bizda  {taom} yoq")

#

