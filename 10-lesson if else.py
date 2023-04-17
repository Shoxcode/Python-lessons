games = ["csgo", "dota 2", "apex legends", "the last of us"]

for game in games:
    if game == "csgo" or game == "apex legends":
        print(game.upper())
    else:
        print(game.title())

#ism = input("Ismingizni kiriting ")
#if ism.lower() != "ali":
    #print(f"Uzur {ism.title()} biz Alini kutayapmiz!")
#else:
 #   print("Salom Ali)")
#answer = input("6 * 9 = ")
#if answer != "54":
 #   print("Javob Xato")
#else:
 #   print("Javobingiz to'g'ri")

yosh = int(input("Yoshingiz nechchida? "))

if yosh >= 18:
    print("Hush kelibsiz!")
else:
    print("Kirish mumkin emas")