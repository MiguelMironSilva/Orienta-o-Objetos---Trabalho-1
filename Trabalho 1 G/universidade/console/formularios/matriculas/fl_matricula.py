from infra import FListagem
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas

class FLMatricula(FListagem):
    """Exibe o histórico de vínculos entre alunos e cursos."""
    def __init__(self, gerenciador_matriculas: GerenciadorMatriculas):
        super().__init__(titulo="LISTAGEM DE MATRÍCULAS", gerenciador=gerenciador_matriculas, colunas=["ID", "Aluno ID", "Curso ID", "Data", "Status"], atributos=["id_matricula", "id_aluno", "id_curso", "data_matricula", "status"])