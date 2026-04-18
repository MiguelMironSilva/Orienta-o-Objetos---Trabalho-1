# framework_universidade/infra/console/util/console_util.py

import os
from datetime import datetime
from typing import Optional

class ConsoleUtil:
    """
    Classe utilitária para operações de entrada e saída no console.
    Fornece métodos seguros para ler diferentes tipos de dados do usuário,
    garantindo que o programa não quebre (crash) por entradas inválidas.
    """

    @staticmethod
    def limpar_tela():
        """Limpa a tela do terminal (funciona em Windows e Linux/Mac)."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_cabecalho(titulo: str):
        """Imprime um cabeçalho padronizado."""
        ConsoleUtil.limpar_tela()
        print("=" * 50)
        print(titulo.center(50))
        print("=" * 50)
        print()

    @staticmethod
    def ler_texto(mensagem: str, obrigatorio: bool = True) -> str:
        """Lê uma string do teclado. Pode ser configurada para não aceitar texto vazio."""
        while True:
            valor = input(mensagem).strip()
            if obrigatorio and not valor:
                print("[Erro] Este campo não pode ficar em branco. Tente novamente.")
            else:
                return valor

    @staticmethod
    def ler_inteiro(mensagem: str) -> int:
        """Lê um número inteiro de forma segura."""
        while True:
            try:
                valor = input(mensagem).strip()
                return int(valor)
            except ValueError:
                print("[Erro] Digite apenas números inteiros válidos.")

    @staticmethod
    def ler_decimal(mensagem: str) -> float:
        """Lê um número decimal de forma segura, aceitando ponto ou vírgula."""
        while True:
            try:
                valor = input(mensagem).strip().replace(',', '.')
                return float(valor)
            except ValueError:
                print("[Erro] Digite um número decimal válido (ex: 7.5).")

    @staticmethod
    def ler_data(mensagem: str, formato: str = "%d/%m/%Y") -> str:
        """
        Lê uma data e valida se ela está no formato correto.
        Retorna a string da data validada.
        """
        while True:
            valor = input(mensagem).strip()
            try:
                # Tenta converter a string para data para validar
                data_obj = datetime.strptime(valor, formato)
                # Retorna a data formatada como string novamente (ou poderia retornar o objeto datetime)
                return data_obj.strftime(formato)
            except ValueError:
                print(f"[Erro] Formato de data inválido. Use o formato {formato} (ex: 25/12/2024).")

    @staticmethod
    def ler_confirmacao(mensagem: str) -> bool:
        """Lê uma confirmação do tipo Sim/Não e retorna um booleano."""
        while True:
            valor = input(f"{mensagem} (S/N): ").strip().upper()
            if valor == 'S':
                return True
            elif valor == 'N':
                return False
            else:
                print("[Erro] Digite apenas 'S' para Sim ou 'N' para Não.")

    @staticmethod
    def pausar():
        """Pausa a execução até o usuário apertar Enter."""
        print()
        input("Pressione [ENTER] para continuar...")