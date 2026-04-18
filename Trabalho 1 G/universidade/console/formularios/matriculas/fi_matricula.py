# framework_universidade/universidade/console/formularios/matriculas/fi_matricula.py

from infra import FInclusao, ErroDeValidacao
from universidade.entidades.matricula import Matricula
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas

class FIMatricula(FInclusao):
    """
    Formulário responsável por registrar uma nova matrícula no sistema.
    Coleta as chaves estrangeiras necessárias e a data do registro.
    """

    def __init__(self, gerenciador_matriculas: GerenciadorMatriculas):
        # Inicializa a base com o título e o gerenciador de matrículas
        super().__init__(titulo="INCLUSÃO DE MATRÍCULA", gerenciador=gerenciador_matriculas)

    def _coletar_dados(self) -> Matricula:
        """
        Coleta os IDs e a data. A validação se os IDs existem no banco 
        será feita pelo Gerenciador ou pela integridade referencial do SQLite.
        """
        
        # 1. Coleta do ID do Aluno
        id_aluno_str = input("ID do Aluno: ").strip()
        try:
            id_aluno = int(id_aluno_str)
        except ValueError:
            raise ErroDeValidacao("O ID do aluno deve ser um número inteiro.")

        # 2. Coleta do ID do Curso
        id_curso_str = input("ID do Curso: ").strip()
        try:
            id_curso = int(id_curso_str)
        except ValueError:
            raise ErroDeValidacao("O ID do curso deve ser um número inteiro.")

        # 3. Coleta da Data
        data = input("Data da Matrícula (DD/MM/AAAA): ").strip()

        # Retorna a entidade. O status padrão 'Ativa' já está definido no @dataclass,
        # mas passamos aqui para garantir a clareza.
        return Matricula(
            id_matricula=None,
            id_aluno=id_aluno,
            id_curso=id_curso,
            data_matricula=data,
            status="Ativa"
        )