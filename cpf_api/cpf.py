from random import randint as rand

class CPF:
    def __init__(self):
        self.estados = {
            0: ["RS"],
            1: ["DF", "GO", "MS", "MT", "TO"],
            2: ["AC", "AM", "AP", "PA", "RO", "RR"],
            3: ["CE", "MA", "PI"],
            4: ["AL", "PB", "PE", "RN"],
            5: ["BA", "SE"],
            6: ["MG"],
            7: ["ES", "RJ"],
            8: ["SP"],
            9: ["PR", "SC"]
        }

    
    def validar_cpf(self, cpf):
        str_cpf = cpf
        cpf = [int(x) for x in cpf if x.isnumeric()]

        cpf_invalido_mensagem = {
                    "estado":False,
                    "mensagem":f"o cpf '{str_cpf}' não passou na validação",
                    0: str_cpf,
                    1: str_cpf
                }
        
        if any([len(cpf) != 11, all(x == cpf[0] for x in cpf)]):
            return cpf_invalido_mensagem
        
        for y in [10, 11]:
            if cpf[y - 1] != sum([cpf[y - x] * x for x in range(y, 1, -1)]) * 10 % 11 % 10:
                return cpf_invalido_mensagem
            
        return {
            "estado":True,
            "mensagem":f"o cpf '{str_cpf}' passou na validação",
            0: str_cpf,
            1: self.formatar_cpf(str_cpf)
        }
    
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
            1: self.formatar_cpf(cpf),
            2: estado
        }

    def formatar_cpf(self, cpf):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'