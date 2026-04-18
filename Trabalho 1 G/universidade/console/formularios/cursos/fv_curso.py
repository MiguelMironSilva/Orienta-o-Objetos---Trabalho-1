# framework_universidade/universidade/console/formularios/cursos/fv_curso.py

from infra import FVisualizacao
from universidade.negocio.gerenciador_cursos import GerenciadorCursos

class FVCurso(FVisualizacao):
    """
    Formulário de Visualização Detalhada de um Curso.
    Exibe informações sobre duração e vínculo departamental.
    """

    def __init__(self, gerenciador_cursos: GerenciadorCursos):
        # Injeção do título e do gerenciador na classe base genérica.
        super().__init__(titulo="DETALHES DO CURSO", gerenciador=gerenciador_cursos)

    def _exibir_detalhes(self, curso):
        """
        Método 'Hook' que define o layout de exibição dos dados do curso.
        Recebe o objeto 'curso' já populado pelo DAO através do Gerenciador.
        """
        print("-" * 45)
        print(f"ID do Curso:      {curso.id_curso:03d}")
        print(f"Nome:             {curso.nome}")
        print(f"Duração:          {curso.duracao_semestres} semestres")
        print(f"ID Departamento:  {curso.id_departamento:03d}")
        print("-" * 45)
        input("\nPressione [ENTER] para voltar ao menu...")