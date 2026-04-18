from infra import FListagem
from universidade.negocio.gerenciador_cursos import GerenciadorCursos

class FLCurso(FListagem):
    """Exibe todos os cursos e suas respectivas durações."""
    def __init__(self, gerenciador_cursos: GerenciadorCursos):
        super().__init__(titulo="LISTAGEM DE CURSOS", gerenciador=gerenciador_cursos)