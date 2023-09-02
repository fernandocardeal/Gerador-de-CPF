from random import randint as rand

class CPF:
    def __init__(self):
        self.estados = {
            0: ["DF", "RS"],
            1: ["GO", "MT", "MS", "TO"],
            2: ["AC", "AP", "AM", "PA", "RO", "RR"],
            3: ["CE", "MA", "PI"],
            4: ["AL", "PB", "PE", "RN"],
            5: ["BA", "SE"],
            6: ["MG"],
            7: ["ES", "RJ"],
            8: ["SP"],
        }

    '''    
    def cpf_validator(self, cpf):
        cpf = [int(x) for x in cpf if x.isnumeric()]
        if True in [len(cpf) != 11, cpf == cpf[::-1]]:
            return False
        for y in [10, 11]:
            if cpf[y - 1] != sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10:
                return False
        return True
    '''
    
    def gerar_cpf(self, estado = None):
        while True:
            cpf = [rand(0, 9) for x in range(9)]
            if estado:
                estado_valido = False
                for reg in self.estados:
                    if estado.upper() in self.estados[reg]:
                        cpf[8], estado_valido = reg, True
                        break
                if not estado_valido:
                    return None
            if not all(x == cpf[0] for x in cpf):
                break
        for y in [10, 11]:
            cpf.append(sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10)
        cpf = ''.join([str(x) for x in cpf])
        return {
            0: cpf,
            1: self.formatar_cpf(cpf)
        }

    def formatar_cpf(self, cpf):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'