from infra import FListagem
from universidade.negocio.gerenciador_professores import GerenciadorProfessores

class FLProfessor(FListagem):
    """Exibe o corpo docente e suas titulações."""
    def __init__(self, gerenciador_professores: GerenciadorProfessores):
        super().__init__(titulo="LISTAGEM DE PROFESSORES", gerenciador=gerenciador_professores, colunas=["ID", "Nome", "Titulação", "Depto ID"], atributos=["id_professor", "nome", "titulacao", "id_departamento"])