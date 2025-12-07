import random

def simula_dado(n_lancamentos):
    contagens = {face: 0 for face in range(1, 7)}
    for _ in range(n_lancamentos):
        face = random.randint(1, 6)
        contagens[face] += 1
    return contagens

if __name__ == "__main__":
    n = 10_000  # número de lançamentos
    resultado = simula_dado(n)
    print(f"Lançando um dado {n} vezes (Monte Carlo simples):")
    for face, qtd in sorted(resultado.items()):
        print(f"Face {face}: {qtd} vezes ({qtd/n:.2%})")