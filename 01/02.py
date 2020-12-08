import string

def get_file_content(file_path):
    try:
        with open (file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))


inputstring = get_file_content('input.txt')

let = inputstring.splitlines()

numbers = []
for number in let:
    numbers.append(int(number))


for firstNumber in numbers:
    for secondNumber in numbers:
        if (firstNumber+secondNumber<2020):
            for thirdNumber in numbers:
                if (firstNumber+secondNumber+thirdNumber==2020):
                    print(f'{firstNumber}+{secondNumber}+{thirdNumber}==2020.  {firstNumber}*{secondNumber}*{thirdNumber}={firstNumber*secondNumber*thirdNumber}')
