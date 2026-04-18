# framework_universidade/infra/console/menus/menu.py

from typing import Callable, Dict, Tuple
from infra.console.util.console_util import ConsoleUtil

class Menu:
    """
    Classe base genérica para construção de menus interativos no console.
    Permite registrar opções dinamicamente, associando um número digitado 
    a uma função (ação) específica a ser executada.
    """

    def __init__(self, titulo: str):
        self.titulo = titulo
        # Dicionário que mapeia a opção (int) para uma tupla: (Descrição, Função)
        self._opcoes: Dict[int, Tuple[str, Callable]] = {}

    def adicionar_opcao(self, numero: int, descricao: str, acao: Callable):
        """
        Registra uma nova opção no menu.
        
        :param numero: O número que o usuário deve digitar para escolher esta opção.
        :param descricao: O texto que aparecerá na tela para o usuário.
        :param acao: O método ou função que será executado (sem os parênteses).
        """
        self._opcoes[numero] = (descricao, acao)

    def _desenhar_tela(self):
        """Método interno para renderizar as opções do menu na tela."""
        ConsoleUtil.mostrar_cabecalho(self.titulo)
        
        # Percorre as opções ordenadas pelo número
        for numero, (descricao, _) in sorted(self._opcoes.items()):
            print(f"[{numero}] {descricao}")
            
        print("[0] Sair / Voltar")
        print("-" * 50)

    def executar(self):
        """
        Inicia o loop principal do menu.
        Só é interrompido quando o usuário digita '0'.
        """
        while True:
            self._desenhar_tela()
            escolha = ConsoleUtil.ler_inteiro("Escolha uma opção: ")

            if escolha == 0:
                # Quebra o laço de repetição, voltando ao menu anterior ou saindo do programa
                break
                
            elif escolha in self._opcoes:
                # Extrai a função (ação) do dicionário e a executa
                acao = self._opcoes[escolha][1]
                
                try:
                    acao()  # Executa o formulário ou submenu associado
                except Exception as e:
                    print(f"\n[Erro Inesperado] Falha ao executar a rotina: {e}")
                
                # Pausa para o usuário ler o resultado antes de limpar a tela e redesenhar o menu
                ConsoleUtil.pausar()
                
            else:
                print("\n[Aviso] Opção inválida. Escolha um número do menu.")
                ConsoleUtil.pausar()