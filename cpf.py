from random import randint as rand

class CPF:
    def __init__(self):
        self.tabela = {
            'AC': 2,
            'AL': 4,
            'AP': 2,
            'AM': 2,
            'BA': 5,
            'CE': 3,
            'DF': 0,
            'ES': 7,
            'GO': 1,
            'MA': 3,
            'MT': 1,
            'MS': 1,
            'MG': 6,
            'PA': 2,
            'PB': 4,
            'PR': 9,
            'PE': 4,
            'PI': 3,
            'RJ': 7,
            'RN': 4,
            'RS': 0,
            'RO': 2,
            'RR': 2,
            'SC': 9,
            'SP': 8,
            'SE': 5,
            'TO': 1
        }
    def cpf_validator(self, cpf):
        cpf = [int(x) for x in cpf if x.isnumeric()]
        if True in [len(cpf) != 11, cpf == cpf[::-1]]:
            return False
        for y in [10, 11]:
            if cpf[y - 1] != sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10:
                return False
        return True

    def cpf_generator(self, estado = False):
        while True:
            cpf = [rand(0, 9) for x in range(9)]
            if estado in self.tabela:
                cpf[8] = self.tabela[estado]
            if cpf != cpf[::-1]:
                break
        for y in [10, 11]:
            cpf.append(sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10)
        cpf = ''.join([str(x) for x in cpf])
        return cpf

    def cpf_formatter(self, cpf):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
