GARIIIII = open('gbp.txt', 'r', encoding='utf-8')
rate = float(GARIIIII.read())
GARIIIII.close()

amount = float(input('Ievadiet kaut ko'))
new_amount = amount * rate

print(f'{amount} Euro = {new_amount} gbp')