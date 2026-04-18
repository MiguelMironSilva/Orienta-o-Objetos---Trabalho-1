# framework_universidade/universidade/console/formularios/alunos/fl_aluno.py

from infra import FListagem
from universidade.negocio.gerenciador_alunos import GerenciadorAlunos

class FLAluno(FListagem):
    """
    Formulário responsável por exibir todos os alunos cadastrados no sistema.
    A lógica de iteração e impressão na tela é herdada do mini-framework (infra).
    """

    def __init__(self, gerenciador_alunos: GerenciadorAlunos):
        # Injeta o título da tela e o controlador de negócio na superclasse.
        super().__init__(titulo="LISTAGEM GERAL DE ALUNOS", gerenciador=gerenciador_alunos, colunas=["ID", "Nome", "Ingresso", "Ativo"], atributos=["id_aluno", "nome", "data_ingresso", "matricula_ativa"])