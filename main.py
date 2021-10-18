import math


def print_meniu():
    print("1. Citirea unei liste de numere întregi.")
    print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3.Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
    print("4.Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr" 
          " n citit de la tastatură.")
    print("5.Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu"
            "radicalul acestora. În cazul numerelor care nu sunt pătrat perfect," 
            "acestea sunt înlocuite cu o listă"
            "cu numerele pătrat perfect mai mici decât numărul inițial." 
            "Modificările se aplică doar pe numerele pozitive.")
    print("6. iesire")
    print("7. afisarea listei scrise de la tastatura")


def citire_lista(lst):
    n = int(input("dati numarul de elemente"))
    for i in range(n):
        lst.append(int(input("L[" + str(i) + " ] ")))
    return lst


def create_number(lst: list[int]) -> int:
    """
    se va scrie numarul obtinut din concatenarea numerelor pozitive a listei
    :param lst: o lista de nr. intregi
    :return: numarul obtinut din concatenarea numerelor pozitive a listei
    """
    concatenat = ""
    for x in lst:
        if x > 0:
            string_x = str(x)
            concatenat = concatenat + string_x
    concatenat = int(concatenat)
    return concatenat


def test_create_number():
    assert create_number([0, 8, 23, -13, 25]) == 82325
    assert create_number([-13, -6, 9]) == 9
    assert create_number([12, 23, 45]) == 122345


def sum_cel_mai_mare_si_cel_mai_mic_nr(lst: list[int]):
    """
    afla suma dintre cel mai mare numar din lista si cel mai mic nr din lista
    :param lst: o lista de numere intregi
    :return: suma dintre cel mai mare numar din lista si cel mai mic nr din lista
    """
    max_value = max(lst)
    min_value = min(lst)
    suma = max_value + min_value
    return suma


def test_sum_cel_mai_mare_si_cel_mai_mic_nr():
    assert sum_cel_mai_mare_si_cel_mai_mic_nr([-13, 2, 3, 10, 9]) == -3
    assert sum_cel_mai_mare_si_cel_mai_mic_nr([-10, 10, 0]) == 0
    assert sum_cel_mai_mare_si_cel_mai_mic_nr([5, 0, 6, 7, 9]) == 9


def sum_cifre(number: int):
    """
    scrie suma cifrelor unui numar n
    :param number: un numar intreg
    :return: suma cifrelor unui numar n
    """
    suma = 0
    n = number
    while n != 0:
        c = n % 10
        suma = suma + c
        n = n // 10
    return suma


def test_sum_cif():
    assert sum_cifre(18) == 9
    assert sum_cifre(2) == 2
    assert sum_cifre(34) == 7


def afisare_nr_sum_c_is_n(lst: list[int], n: int):
    """
    creeaza o lista noua in care adauga doar numerele care au suma cifrelor mai mare sau egala decat n
    :param lst: o lista de nr intregi
    :param n: un numar intreg
    :return: o lista noua in care adauga doar numerele care au suma cifrelor mai mare sau egala decat n
    """
    new_list = []
    for x in lst:
        if sum_cifre(x) >= n:
            new_list.append(x)
    return new_list


def test_afisare_nr_sum_c_is_n():
    assert afisare_nr_sum_c_is_n([25, 11, 10, 24, 39], 7) == [25, 39]
    assert afisare_nr_sum_c_is_n([12, 23, 3,  2, 1, 10], 3) == [12, 23, 3]
    assert afisare_nr_sum_c_is_n([1, 2, 3, 4], 23) == []


def main():
    new_list = []
    test_create_number()
    test_sum_cel_mai_mare_si_cel_mai_mic_nr()
    test_afisare_nr_sum_c_is_n()
    test_sum_cif()
    while True:
        print_meniu()
        option = input("optiunea dorita este = ")
        if option == '1':
            citire_lista(new_list)
        elif option == '2':
            print(create_number(new_list))
        elif option == '3':
            print(sum_cel_mai_mare_si_cel_mai_mic_nr(new_list))
        elif option == '4':
            n = int(input("numarul citit de la tastatura este = "))
            print(afisare_nr_sum_c_is_n(new_list, n))
        elif option == '5':
            pass
        elif option == '6':
            break
        elif option == '7':
            print(new_list)
        else:
            print("optiune invalida, reincercati!")


main()

