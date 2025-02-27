class Estacionamento:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.vagas = []

    def adicionar_carro(self,placa):
        if len(self.vagas) < self.capacidade:
            self.vagas.append(placa)
            print(f'Carro com placa {placa} estacionado com sucesso.')
        else:
            print(f'Estacionamento lotado. Não é possivel estacionar.')

        def __str__(self): # type: ignore
            return print(f'Vagas ocupadas:{len(self.vagas)}){self.capacidade}\nVagas:{','.join(self.vagas)}')


    def main():
        capacidade_estacionamento = 10
        estacionamento =  Estacionamento(capacidade_estacionamento)

        while True:
            print('\n--- Estacionamento ---')
            print(estacionamento)
            opcao = input("\nDigite '1' para estacionar um carro, '0' para sair:")

            if opcao =='1':
                placa = input('Digite a placa do carro:')
                estacionamento.adicionar_carro(placa)
            elif opcao =='0':
                print('Encerramento o programa.')
                break
            else:
                print('Opção inválida. Tente novamente')

        if_name_=='__main__': 
    main()