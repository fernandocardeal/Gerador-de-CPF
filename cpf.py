from random import randint as rand

class CPF:
    def cpf_validator(cpf):
        cpf = [int(x) for x in cpf if x.isnumeric()]
        if True in [len(cpf) != 11, cpf == cpf[::-1]]:
            return False
        for y in [10, 11]:
            if cpf[y - 1] != sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10:
                return False
        return True

    def cpf_generator():
        while True:
            cpf = [rand(0, 9) for x in range(9)]
            if cpf != cpf[::-1]:
                break
        for y in [10, 11]:
            cpf.append(sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10)
        cpf = ''.join([str(x) for x in cpf])
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'