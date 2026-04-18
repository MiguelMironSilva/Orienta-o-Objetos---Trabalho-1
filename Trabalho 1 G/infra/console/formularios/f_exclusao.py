# framework_universidade/infra/console/formularios/f_exclusao.py

from typing import Any
from infra.console.formularios.formulario_base import FormularioBase
from infra.console.util.console_util import ConsoleUtil
from infra.excecoes.base_errors import RegistroNaoEncontradoError

class FExclusao(FormularioBase):
    """
    Formulário genérico para exclusão de registros.
    Implementa um fluxo seguro: busca o registro, exibe seus dados para 
    conferência (evitando exclusões acidentais) e solicita confirmação dupla 
    antes de delegar a remoção ao gerenciador de negócios.
    """

    def __init__(self, titulo: str, gerenciador: Any):
        super().__init__(titulo)
        self.gerenciador = gerenciador

    def executar(self):
        self._mostrar_cabecalho()
        
        id_busca = ConsoleUtil.ler_inteiro("Digite o ID do registro que deseja EXCLUIR: ")
        
        try:
            print("\nBuscando registro...")
            
            # 1. Busca o registro primeiro para que o usuário veja o que está apagando
            registro_atual = self.gerenciador.buscar_por_id(id_busca)
            
            print("-" * 50)
            print("ATENÇÃO: DADOS A SEREM EXCLUÍDOS".center(50))
            print(registro_atual)
            print("-" * 50)
            
            # 2. Confirmação de segurança (crucial para operações destrutivas)
            print("\n[CUIDADO] Esta operação é irreversível no banco de dados.")
            if ConsoleUtil.ler_confirmacao("Tem certeza absoluta que deseja excluir este registro?"):
                
                # 3. Delega a exclusão ao gerenciador passando o ID
                self.gerenciador.excluir(id_busca)
                print("\n[Sucesso] Registro excluído com sucesso do sistema!")
                
            else:
                print("\n[Aviso] Operação cancelada. O registro foi mantido intacto.")

        except RegistroNaoEncontradoError as e:
            print(f"\n[Aviso] {e}")
            
        except Exception as e:
            # Captura falhas do banco de dados, como violação de chave estrangeira
            print(f"\n[Erro Inesperado] Não foi possível excluir o registro: {e}")
            
        ConsoleUtil.pausar()