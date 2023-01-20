import sys


def delete(lista, word):
    plik = read_file(lista)
    plik = plik.replace(word, '')
    save_to_file(lista, plik)

def contains(lista, word):
    if word in read_file(lista):
        print(word + " zawiera sie w "+ lista)
    else:
        print(word + " nie zawiera sie w " + lista)

def add (lista, word):
    reszta = read_file(lista)
    reszta += word
    reszta += "\n"
    save_to_file(lista, reszta)

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)


def run_program(name, params):
    print(params)
    if params[0] == 'push':
        pass

def main():
    if sys.argv[1] == 'contains':
        contains('lista.txt',sys.argv[2])
    if sys.argv[1] == 'add':
        add('lista.txt',sys.argv[2])
    if sys.argv[1] == 'delete':
        delete('lista.txt',sys.argv[2])


if __name__ == '__main__':
    args = sys.argv
    run_program('PyCharm', sys.argv[1:])
    main()