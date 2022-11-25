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