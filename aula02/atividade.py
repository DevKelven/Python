candidatos = ["Candidato 1", "Candidato 2", "Candidato 3"]

faixa_etaria = {"18-25": [0, 0, 0], "26-35": [0, 0, 0], "36-50": [0, 0, 0], "51+": [0, 0, 0]}
genero = {"Masculino": [0, 0, 0], "Feminino": [0, 0, 0], "Outro": [0, 0, 0]}

total_votos = 0

def registrar_voto():
    global total_votos
    
    print("\nVotação para representante de sala")
    print("Escolha um candidato (1, 2 ou 3):")
    voto = int(input("Digite o número do candidato (1, 2 ou 3): ")) - 1
    if voto not in [0, 1, 2]:
        print("Opção inválida. Tente novamente.")
        return False

    faixa = input("Digite sua faixa etária (18-25, 26-35, 36-50, 51+): ")
    if faixa not in faixa_etaria:
        print("Faixa etária inválida. Tente novamente.")
        return False

    genero_input = input("Digite seu gênero (Masculino, Feminino, Outro): ")
    if genero_input not in genero:
        print("Gênero inválido. Tente novamente.")
        return False

    faixa_etaria[faixa][voto] += 1
    genero[genero_input][voto] += 1
    total_votos += 1
    
    return True

def exibir_resultados():
    print("\nResultados da votação:")
    
    for faixa, votos in faixa_etaria.items():
        print(f"\nFaixa Etária {faixa}:")
        for i, candidato in enumerate(candidatos):
            percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
            print(f"  {candidato}: {percentual:.2f}%")
    
    for gen, votos in genero.items():
        print(f"\nGênero {gen}:")
        for i, candidato in enumerate(candidatos):
            percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
            print(f"  {candidato}: {percentual:.2f}%")

def main():
    while True:
        if not registrar_voto():
            continue
        
        cont = input("Deseja registrar outro voto? (sim/não): ").strip().lower()
        if cont != "sim":
            break

    exibir_resultados()

main()
