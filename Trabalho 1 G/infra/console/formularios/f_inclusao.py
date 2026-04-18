# framework_universidade/infra/console/formularios/f_inclusao.py

from abc import abstractmethod
from typing import Any
from infra.console.formularios.formulario_base import FormularioBase
from infra.console.util.console_util import ConsoleUtil
from infra.excecoes.base_errors import ErroDeValidacao

class FInclusao(FormularioBase):
    """
    Formulário genérico para inclusão (cadastro) de novos registros.
    Delega a coleta de dados para as classes filhas e centraliza o 
    fluxo de confirmação, salvamento e tratamento de erros.
    """

    def __init__(self, titulo: str, gerenciador: Any):
        super().__init__(titulo)
        self.gerenciador = gerenciador

    def executar(self):
        """Fluxo principal de inclusão (Não deve ser sobrescrito)."""
        self._mostrar_cabecalho()
        
        try:
            # 1. Delega à classe filha a responsabilidade de fazer os inputs
            # e montar o objeto (instância da entidade)
            novo_registro = self._coletar_dados()
            
            # Permite que a coleta seja cancelada se a classe filha retornar None
            if novo_registro is None:
                print("\n[Aviso] Operação cancelada durante a entrada de dados.")
                ConsoleUtil.pausar()
                return

            # 2. Exibe os dados coletados para conferência final
            print("-" * 50)
            print("CONFERÊNCIA DE DADOS".center(50))
            print(novo_registro)
            print("-" * 50)
            
            # 3. Confirmação e Salvamento
            if ConsoleUtil.ler_confirmacao("Confirma o cadastro deste novo registro?"):
                
                # A camada de negócio (gerenciador) recebe o objeto, valida as regras
                # e manda para o DAO salvar no banco.
                self.gerenciador.incluir(novo_registro)
                print("\n[Sucesso] Registro cadastrado com sucesso no sistema!")
                
            else:
                print("\n[Aviso] Operação cancelada. O registro foi descartado.")

        except ErroDeValidacao as e:
            # Captura regras de negócio quebradas (ex: Aluno menor de idade, CPF inválido)
            print(f"\n[Erro de Validação] Não foi possível salvar: {e}")
            
        except Exception as e:
            print(f"\n[Erro Inesperado] Falha crítica ao tentar cadastrar: {e}")
            
        ConsoleUtil.pausar()

    @abstractmethod
    def _coletar_dados(self) -> Any:
        """
        Método abstrato protegido.
        As classes filhas (ex: FIAluno) DEVEM implementar este método, 
        usar o ConsoleUtil para ler os dados, instanciar a entidade (Aluno) 
        e retorná-la.
        """
        pass