print('Напишите строку из нескольких слов разделенных пробелами')
text = (input())
text = text.split(' ')
for ind, el in enumerate(text):
 print(ind+1, el[0:10])
#Каждый любит программирование на пайтон
