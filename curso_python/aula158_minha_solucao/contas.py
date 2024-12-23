import abc
from dataclasses import dataclass, field


@dataclass
class Conta(abc.ABC):
    agencia: int
    conta: int
    saldo: float = field(default=0)

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('--')


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo


@dataclass
class ContaCorrente(Conta):
    limite: float = field(default=0)

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é -R${self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    print(cp1)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # cp1.sacar(1)
    # cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    print(cc1)
    # cc1.sacar(1)
    # cc1.depositar(1)
    # cc1.sacar(1)
    # cc1.sacar(98)
    # cc1.sacar(1)
    # cc1.sacar(1)
    print('##')
