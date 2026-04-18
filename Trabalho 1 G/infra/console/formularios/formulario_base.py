# framework_universidade/infra/console/formularios/formulario_base.py

from abc import ABC, abstractmethod
from infra.console.util.console_util import ConsoleUtil

class FormularioBase(ABC):
    """
    Classe Abstrata Base para todos os formulários (telas) do sistema.
    Define a estrutura padrão que qualquer tela de interação no console
    deve obrigatoriamente seguir.
    """

    def __init__(self, titulo: str):
        """
        Inicializa o formulário definindo o título que aparecerá no topo da tela.
        """
        self.titulo = titulo

    def _mostrar_cabecalho(self):
        """
        Método interno e reutilizável para limpar o terminal e exibir
        o título do formulário de forma padronizada.
        O underline '_' indica que é um método protegido (para uso interno da classe e filhas).
        """
        ConsoleUtil.mostrar_cabecalho(self.titulo)

    @abstractmethod
    def executar(self):
        """
        Método principal do formulário.
        Como possui o decorador @abstractmethod, o Python OBRIGA que qualquer
        classe filha (como FInclusao, FListagem) implemente este método.
        Se um desenvolvedor esquecer de implementá-lo, o sistema acusará erro
        antes mesmo de rodar.
        """
        pass