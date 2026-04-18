# framework_universidade/universidade/console/formularios/departamentos/fa_departamento.py

from infra import FAlteracao
from universidade.entidades.departamento import Departamento
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos

class FADepartamento(FAlteracao):
    """
    Formulário responsável por alterar os dados de um Departamento existente.
    Utiliza o padrão Template Method herdado de FAlteracao para gerenciar 
    o ciclo de vida da operação.
    """

    def __init__(self, gerenciador_deptos: GerenciadorDepartamentos):
        # Injeção do título e do gerenciador específico na superclasse
        super().__init__(titulo="ALTERAÇÃO DE DEPARTAMENTO", gerenciador=gerenciador_deptos)

    def _coletar_alteracoes(self, departamento: Departamento) -> Departamento:
        
        """
        Método 'hook' que define quais campos podem ser editados.
        O objeto 'departamento' já foi carregado do banco de dados pela classe pai.
        """
        print("\n[DICA] Pressione ENTER sem digitar nada para manter o valor atual.")

        # 1. Alteração do Nome do Departamento
        novo_nome = input(f"Nome do Departamento [{departamento.nome}]: ").strip()
        if novo_nome:
            departamento.nome = novo_nome

        # 2. Alteração da Sigla (ex: de 'MAT' para 'DMAT')
        nova_sigla = input(f"Sigla do Departamento [{departamento.sigla}]: ").strip()
        if nova_sigla:
            departamento.sigla = nova_sigla

        # Nota: A validação de unicidade da sigla e o tamanho do nome 
        # serão processados pelo GerenciadorDepartamentos assim que 
        # este método terminar e a classe pai chamar o método salvar.
        return departamento
