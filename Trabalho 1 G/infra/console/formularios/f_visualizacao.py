# framework_universidade/infra/console/formularios/f_visualizacao.py

from infra.console.formularios.formulario_base import FormularioBase
from infra.console.util.console_util import ConsoleUtil
from infra.excecoes.base_errors import RegistroNaoEncontradoError
from typing import Any

class FVisualizacao(FormularioBase):
    """
    Formulário genérico para visualização dos detalhes de um único registro.
    Solicita o identificador (ID) ao usuário, busca na base de dados 
    (através do gerenciador) e exibe os dados em tela.
    """

    def __init__(self, titulo: str, gerenciador: Any):
        """
        O formulário recebe o gerenciador da camada de negócios para
        poder realizar a busca no banco de dados sem acoplar regras de SQL.
        """
        super().__init__(titulo)
        self.gerenciador = gerenciador

    def executar(self):
        # 1. Desenha o cabeçalho padronizado da classe pai
        self._mostrar_cabecalho()
        
        # 2. Solicita a chave primária (ID) de forma segura
        id_busca = ConsoleUtil.ler_inteiro("Digite o ID do registro que deseja visualizar: ")
        
        try:
            print("\nBuscando registro...")
            
            # 3. Delega a busca para o gerenciador de negócios
            registro = self.gerenciador.buscar_por_id(id_busca)
            
            # 4. Exibe os dados formatados
            print("-" * 50)
            print("DADOS DO REGISTRO".center(50))
            print("-" * 50)
            
            # O Python converte o objeto para texto automaticamente chamando o __str__()
            print(registro) 
            
            print("-" * 50)
            
        except RegistroNaoEncontradoError as e:
            # Captura a exceção específica do framework (tratamento amigável)
            print(f"\n[Aviso] {e}")
            
        except Exception as e:
            # Captura erros técnicos imprevistos (ex: queda de conexão com o banco)
            print(f"\n[Erro Inesperado] Falha na comunicação com os dados: {e}")
        
        # 5. Pausa a tela para que o usuário leia a informação antes do menu redesenhar
        ConsoleUtil.pausar()