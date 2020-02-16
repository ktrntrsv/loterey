import string

alphabet = string.ascii_uppercase


def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    counter = 1
    for i in list(gen_series(series)):
        for j in list(gen_number(length)):
            if counter <= count:
                yield '{} {}'.format(j, i)
                counter += 1
            else: raise StopIteration

def gen_series(series):
    """
    генератор серий лотерейных билетов, входные параметры: series -  - номер серии,
    выход - строка, состоящая из двух заглавных букв латинского алфавита
    """
    series = series.upper()
    while series != 'ZZ':
        yield series
        if series[1] == 'Z':
            series = alphabet[alphabet.find(series[0])+1] + 'A'
        else:
            series = series[0] + alphabet[alphabet.find(series[1])+1]
    yield "ZZ"


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов, входные параметры: необязательный
    аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    count = 1
    yield '{0:0>{len}}'.format(count, len = length)
    while count < int('9'*length):
        count += 1
        yield '{0:0>{len}}'.format(count, len = length)
