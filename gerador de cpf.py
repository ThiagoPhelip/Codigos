import random

def gera_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    # Aplica o algoritmo de validação do CPF
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)
    
    return ''.join(map(str, cpf))

# Exemplo de uso
print(gera_cpf())
