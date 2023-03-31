sentense = input('Введите предложение: ')

sentense = sentense[: sentense.find('h') :] + sentense[sentense.rfind('h') + 1:]

print(sentense)