import json

INPUT_FILE = "input.csv"
# в pycharm решение с файлом "input.csv" не прошло - не видит файл; 
# возможно там опечатка и правильно называть файл "output.csv" - оставил оба варианта имени
# INPUT_FILE = "output.csv"

def csv_to_list_dict(filename):
    data = []
    result = []
    with open(filename) as csv_file:
        for line in csv_file:
            data.append(line.split(','))

        for i in range(1, len(data)):
            row = {}
            for j in range(len(data[0])):
                row[data[0][j]] = data[i][j].rstrip('\n')

            result.append(row)

    return result

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
