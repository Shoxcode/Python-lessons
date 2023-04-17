#yosh = int(input("Yoshingizni kiriting "))
#if yosh <=4:
 #   price = 0
#elif yosh <=12:
 #   price = 5
#elif yosh <=18:
 #   price = 8
#else:
 #   price = 10

#print(f"Sizga kirish {price} so'm")

#kun = input("Bugungi kunni kiriting>>")
#if kun.lower() == "yakshanba" or kun.lower() == "shanba":
 #   print("Bugun dam olish kuni")
#else:
    #print("Bugun ish kuni")
#kun = input("Bugungi kunni kiriting>>")
#harorat = float(input("Havo haroratini kiriting>>"))

#if kun.lower() == "yakshanba" and harorat >= 30:
 #   print("Cho'milgani ketdik")
#elif kun.lower() == "yakshanba" and harorat < 30:
    #print("Bugun cho'milishga bora olmaymiz")

menu = ["ovqat", "somsa", "pomidor", "norin"]
buyurtmalar = ["somsa", "pomido", "norin"]
for taom in buyurtmalar:

 if taom in menu:
    print(f"Bizda {taom} bor")
 else:
    print(f"Kechirasiz bizda {taom} yo'q")
