content = input('Ko vēlies rakstīt?')
amount = int(input('Cik vēlies rakstīt?'))

NewFile = open('Fails_tears.txt', 'w', encoding='utf-8')

for i in range(amount):
    NewFile.write(content + '\n')

NewFile.close()