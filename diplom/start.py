from date_base import DataBasa

def main():
    data = DataBasa
    call_function = {1: data.input_data, 2: data.find, 3: data.get_from_file,
                     4: data.get_intu_file, 5: data.export_in_json}

    while True:
        print("1. Ввести новую запись")
        print("2. Поиск в БД")
        print("3. Загрузить данные в БД из файла")
        print("4. Сохранить данные из БД в файл")
        print("5. Экспортировать данные в json формат")
        print('-' * 50)
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if not choice.isdigit() or int(choice) > 5:
            print("Не корректный ввод")
            continue
        elif int(choice) == 0:
            break


        call_function[int(choice)](int(choice))



if __name__ == "__main__":
    main()
