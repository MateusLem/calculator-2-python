from math import log


class Operacoes:
    def __init__(self) -> None:
        pass

    @staticmethod
    def insert_value() -> float:
        '''Retorna o valor informado pelo usuário.'''
        while True:
            try:
                return float(input('\nInforme um número: '))
            except ValueError:
                print("Por favor, insira um número válido.")

    @staticmethod
    def soma(number1: float, number2: float) -> float:
        '''Retorna a adição de dois números.'''
        return number1 + number2

    @staticmethod
    def subt(number1: float, number2: float) -> float:
        '''Retorna a subtração entre dois números.'''
        return number1 - number2

    @staticmethod
    def mult(number1: float, number2: float) -> float:
        '''Retorna a multiplicação de dois números.
        Há arredondamento para 3 casas decimais.'''
        return round(number1 * number2, 3)

    @staticmethod
    def divd(number1: float, number2: float) -> float:
        '''Retorna a divisão entre dois números.
        Há arredondamento para 3 casas decimais.'''
        while number2 == 0:
            print('\nBase inválida. O valor deve ser um número diferente de 0')
            number2 = Operacoes.insert_value()
        return round(number1 / number2, 3)

    @staticmethod
    def expo(number1: float, number2: float) -> float:
        '''Retorna a exponenciação entre dois números.
        Há arredondamento para 3 casas decimais.'''
        return round(number1 ** number2, 3)

    @staticmethod
    def raiz(number1: float, number2: float) -> float:
        '''Retorna a radiciação entre dois números.
        Há arredondamento para 3 casas decimais.'''
        return round(number1 ** (1 / number2), 3)

    @staticmethod
    def trocar_base() -> bool:
        '''Verifica se o usuário deseja trocar a base da equação logarítma.'''
        r = int(input('\nDeseja trocar a base?\n(Lembrando, que a base é o primeiro número que você escreveu'
                      ' ou o resultado da última operação)\n\n1- Sim\n2- Não\n\n'))
        if r == 1:
            return True

    def valid_base(self, number1: float) -> float:
        '''Verifica se a base do logarítimo é válida (positiva e diferente de 1).'''
        while number1 <= 0 or number1 == 1:
            print('\nBase inválida. O valor deve ser um número positivo e diferente de 1')
            number1 = self.insert_value()
        return number1

    def valid_logaritmando(self, number2: float) -> float:
        '''Verifica se o logaritmando é válido (positivo).'''
        while number2 < 0:
            print('\nLogaritmando inválido. O valor deve ser um número positivo')
            number2 = self.insert_value()
        return number2

    def logf(self, number1: float, number2: float) -> float:
        '''Retorna logarítmo entre dois números.'''
        if self.trocar_base():
            number1 = self.insert_value()

        number1 = self.valid_base(number1)
        number2 = self.valid_logaritmando(number2)
        return round(log(number2, number1), 3)


class Menus(Operacoes):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def input_operacao() -> int:
        '''Retorna o número da operação escolhida pelo usuário.'''
        return int(input(
            "\nInforme a operação:\n1- Soma\n2- Subtração\n3- Multiplicação"
            "\n4- Divisão\n5- Exponenciação\n6- Radiciação\n7- Logarítmo\n\n"
        ))

    @staticmethod
    def select_continuar() -> int:
        '''Retorna a seleção de continuar do usuário.'''
        return int(input("Deseja continuar?\n1- Sim\n2- Não\n\n"))

    @staticmethod
    def no_dot(number: str) -> str:
        '''Verifica se o número possui vírgula. Em caso segativo, adiciona '.0' ao final do número.'''
        if '.' not in number:
            number += '.0'
        return number

    @staticmethod
    def define_expoent(number: str) -> str | None:
        '''Verifica se há necessidade de apresentar notação científica.
        Caso o número seja negativo, o expoente será reduzido para refletir um resultado mais legível.
        Caso o expoente seja menor que 10, um '0' será adicionado por motivos estéticos.
        Caso não haja necessidade de notação, o retorno é None'''
        if len(number) >= 8:
            dot_index = number.index('.')
            expoent = dot_index - 1

            if '-' in number:
                expoent -= 1

            if expoent < 10:
                expoent = f'0{expoent}'

            return str(expoent)
        return None

    def select_operacao(self):
        '''Retorna a operação escolhida pelo usuário.'''
        operations = {
            1: self.soma,
            2: self.subt,
            3: self.mult,
            4: self.divd,
            5: self.expo,
            6: self.raiz,
            7: self.logf
        }
        resp = self.input_operacao()
        return operations.get(resp)

    def valid_operation(self) -> float | None:
        '''Verifica se a operação escolhida é valida.
        Retorna quando houver valor.'''
        operation_func = self.select_operacao()

        while not operation_func:
            print('\nOperação Inválida')
            operation_func = self.select_operacao()

        return operation_func

    def show_result(self, number: float) -> None:
        '''Exibe o resultado da operação.'''
        str_number = self.no_dot(str(number))
        expoent = self.define_expoent(str_number)

        if expoent:
            print(f'\nResultado: {number/(10**int(expoent))}e{expoent}\n')
        else:
            print(f'\nResultado: {number}\n')

    def operation(self, number1: float | None) -> float | None:
        '''Executa a operação selecionada pelo usuário.
        Caso o primeiro valor seja None, haverá a requisição de um valor ao usuário.'''
        operation_func = self.valid_operation()

        if number1 is None:
            number1 = self.insert_value()
        print(f'Primeiro número: {number1}')

        number2 = self.insert_value()
        print(f'Segundo número: {number2}')

        try:
            result = operation_func(number1, number2)
            self.show_result(result)
            return result
        except ValueError as e:
            print(e)

    def continuar(self, result: float) -> None:
        '''
        Verifica se o usuário deseja continuar.
        Positivo: Chama a função 'Menus.main()', tendo o resultado como parâmetro.
        Negativo: Encerra o programa.
        '''
        if self.select_continuar() == 1:
            self.main(result)

    def main(self, result: float | None = None) -> None:
        '''
        Função dividida em duas etapas.
        1-> Executa a função 'Menus.operation()', tendo como parâmetros
        o resultado anterior, caso haja, e o input de um valor pelo usuário.
        2-> Verifica se há um resultado válido.
        '''
        result = self.operation(result)
        if result is not None:
            self.continuar(result)


Menus().main()
