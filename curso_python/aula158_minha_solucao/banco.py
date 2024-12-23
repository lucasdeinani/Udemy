from dataclasses import dataclass, field
import contas
import pessoas


@dataclass
class Banco:
    lista_agencias: list[int] = field(default_factory=list)
    lista_clientes: list[pessoas.Cliente] = field(default_factory=list)
    lista_contas: list[contas.Conta] = field(default_factory=list)

    def _checa_agencia(self, agencia: contas.Conta) -> bool:
        if agencia.agencia in self.lista_agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente: pessoas.Cliente) -> bool:
        if cliente in self.lista_clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta: contas.Conta) -> bool:
        if conta in self.lista_contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(
        self,
        cliente: pessoas.Cliente,
        conta: contas.Conta
    ) -> bool:
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(
        self,
        cliente: pessoas.Cliente,
        conta: contas.Conta
    ) -> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)


if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.lista_clientes.extend([c1, c2])
    banco.lista_contas.extend([cc1, cp1])
    banco.lista_agencias.extend([111, 222])
    print(banco)

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
