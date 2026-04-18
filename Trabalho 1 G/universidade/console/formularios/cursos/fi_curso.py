# framework_universidade/universidade/console/formularios/cursos/fi_curso.py

from infra import FInclusao, ErroDeValidacao
from universidade.entidades.curso import Curso
from universidade.negocio.gerenciador_cursos import GerenciadorCursos

class FICurso(FInclusao):
    """
    Formulário responsável pela coleta de dados para criação de um novo Curso.
    """

    def __init__(self, gerenciador_cursos: GerenciadorCursos):
        # Inicializa a classe base com o título e o gerenciador de cursos
        super().__init__(titulo="INCLUSÃO DE CURSO", gerenciador=gerenciador_cursos)

    def _coletar_dados(self) -> Curso:
        """
        Implementação do método abstrato para capturar os dados do curso via console.
        """
        nome = input("Nome do Curso: ").strip()
        
        # Coleta a duração com tratamento de erro de conversão
        duracao_str = input("Duração em Semestres: ").strip()
        try:
            duracao = int(duracao_str)
        except ValueError:
            raise ErroDeValidacao("A duração deve ser um número inteiro.")

        # Coleta o ID do departamento com tratamento de erro de conversão
        depto_id_str = input("ID do Departamento Responsável: ").strip()
        try:
            id_depto = int(depto_id_str)
        except ValueError:
            raise ErroDeValidacao("O ID do departamento deve ser um número inteiro.")

        # Retorna a entidade Curso. O id_curso é None pois será gerado pelo SQLite.
        return Curso(
            id_curso=None, 
            nome=nome, 
            duracao_semestres=duracao, 
            id_departamento=id_depto
        )