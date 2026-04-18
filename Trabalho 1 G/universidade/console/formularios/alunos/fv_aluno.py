# framework_universidade/universidade/console/formularios/alunos/fv_aluno.py

from infra import FVisualizacao
from universidade.negocio.gerenciador_alunos import GerenciadorAlunos

class FVAluno(FVisualizacao):
    """
    Formulário de Visualização Detalhada de um Aluno.
    Utiliza a estrutura genérica da infraestrutura para exibir os campos
    específicos da entidade Aluno.
    """

    def __init__(self, gerenciador_alunos: GerenciadorAlunos):
        # Injeção do título e do gerenciador na classe base.
        super().__init__(titulo="DETALHES DO ALUNO", gerenciador=gerenciador_alunos)

    def _exibir_detalhes(self, aluno):
        """
        Método 'Hook' (Gancho) chamado pela classe pai após 
        localizar o aluno com sucesso no banco de dados.
        """
        print("-" * 40)
        print(f"ID:               {aluno.id_aluno:03d}")
        print(f"Nome Completo:    {aluno.nome}")
        print(f"Data de Ingresso: {aluno.data_ingresso}")
        print(f"Situação:         {'ATIVO' if aluno.matricula_ativa else 'INATIVO'}")
        print("-" * 40)
        input("\nPressione [ENTER] para voltar ao menu...")