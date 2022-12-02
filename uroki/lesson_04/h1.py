# Используя input() ввести предложение состоящее из двух слов.
# Создать 2 переменные и в каждую записать по 1 введённому слову используя методы строк.
# Создать новую переменную 3-мя разными способами форматирования (фактически 3 переменные),
# которая бы состояла из введённых слов в обратном порядке, первое слово должно состоять
# только из больших букв, а второе с первой заглавной буквы и остальных маленьких.
# В начале предложения должен быть восклицательный знак, а в конце вопросительный.
#
# Используя только атрибуты функции print() вывести первоначальную строку и получившиеся
# разными способами форматирования через разделитель "<<<>>>", вывод сделать в файл.


text = input("Введите предложени из слов: ")
splitted_text = text.split()
first_word = splitted_text[0].title()
second_word = splitted_text[1].upper()
reverse_text_1 = f"!{second_word} {first_word}?"
reverse_text_2 = "!%s %s?" % (second_word, first_word)
reverse_text_3 = "!{1} {0}?".format(first_word, second_word)
new_file = open("splitted_file.txt", "w")
print(text, reverse_text_1, reverse_text_2, reverse_text_3, sep="<<<>>>", file=new_file)
new_file.close()