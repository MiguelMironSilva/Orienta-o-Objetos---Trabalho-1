# framework_universidade/infra/console/formularios/f_alteracao.py

from abc import abstractmethod
from typing import Any
from infra.console.formularios.formulario_base import FormularioBase
from infra.console.util.console_util import ConsoleUtil
from infra.excecoes.base_errors import RegistroNaoEncontradoError

class FAlteracao(FormularioBase):
    """
    Formulário genérico para alteração de registros.
    Implementa o fluxo padrão (Template Method) de buscar pelo ID,
    exibir os dados atuais, e salvar no banco, mas obriga as classes filhas 
    a definirem como os campos específicos serão lidos.
    """

    def __init__(self, titulo: str, gerenciador: Any):
        super().__init__(titulo)
        self.gerenciador = gerenciador

    def executar(self):
        """Fluxo principal de alteração (Não deve ser sobrescrito)."""
        self._mostrar_cabecalho()
        
        id_busca = ConsoleUtil.ler_inteiro("Digite o ID do registro que deseja alterar: ")
        
        try:
            print("\nBuscando registro...")
            # 1. Tenta buscar o registro no banco de dados
            registro_atual = self.gerenciador.buscar_por_id(id_busca)
            
            print("-" * 50)
            print("DADOS ATUAIS".center(50))
            print(registro_atual)
            print("-" * 50)
            print("Dica: Pressione [ENTER] com o campo vazio para manter o valor atual.\n")
            
            # 2. Chama o "Hook" (método gancho) que a classe filha implementou
            registro_modificado = self._coletar_alteracoes(registro_atual)
            
            # 3. Confirmação e Salvamento
            print()
            if ConsoleUtil.ler_confirmacao("Confirma a alteração destes dados?"):
                self.gerenciador.alterar(registro_modificado)
                print("\n[Sucesso] Registro atualizado com sucesso no banco de dados!")
            else:
                print("\n[Aviso] Operação de alteração cancelada. Nenhuma mudança foi salva.")

        except RegistroNaoEncontradoError as e:
            print(f"\n[Aviso] {e}")
        except Exception as e:
            print(f"\n[Erro Inesperado] Falha ao tentar alterar o registro: {e}")
            
        ConsoleUtil.pausar()

    @abstractmethod
    def _coletar_alteracoes(self, registro: Any) -> Any:
        """
        Método abstrato protegido.
        As classes filhas (ex: FAAluno) DEVEM implementar este método para
        perguntar ao usuário os novos valores dos atributos específicos e 
        atualizar o objeto 'registro'.
        """
        pass