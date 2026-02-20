import random

string_list = ["portakal", "gitar", "bilgisayar", "terminal"]
tahmin = random.choice(string_list)
tahmin_karma = list(tahmin)
random.shuffle(tahmin_karma)

print(f"Harfleri karışık verilen kelimeyi tahmin ediniz: {''.join(tahmin_karma)}")

while True:
    user_tahmini = input("Tahmininiz: ")
    if user_tahmini == tahmin:
        print("Doğru!")
        break
    else:
        print("Yanlış, tekrar deneyin")
