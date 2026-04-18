# framework_universidade/universidade/console/formularios/cursos/fe_curso.py

from infra import FExclusao
from universidade.negocio.gerenciador_cursos import GerenciadorCursos

class FECurso(FExclusao):
    """
    Formulário responsável por remover um Curso do sistema.
    Herda a lógica de confirmação e validação da classe genérica FExclusao.
    """

    def __init__(self, gerenciador_cursos: GerenciadorCursos):
        # Passamos o título da tela e o gerenciador de cursos (camada de negócio)
        # para que a superclasse saiba qual 'cérebro' consultar para a exclusão.
        super().__init__(titulo="EXCLUSÃO DE CURSO", gerenciador=gerenciador_cursos)

    # Nota: Não é necessário sobrescrever nenhum método aqui.
    # O método executar() da classe pai já lida com todo o fluxo:
    # 1. Solicita o ID do curso.
    # 2. Busca o objeto para mostrar o nome (via get_rotulo()).
    # 3. Pede confirmação (S/N).
    # 4. Tenta excluir e captura erros de chave estrangeira do SQLite.