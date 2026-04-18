# framework_universidade/universidade/console/formularios/professores/fv_professor.py

from infra import FVisualizacao
from universidade.negocio.gerenciador_professores import GerenciadorProfessores

class FVProfessor(FVisualizacao):
    """
    Formulário de Visualização Detalhada de um Professor.
    Apresenta o nome, a titulação e o vínculo departamental do docente.
    """

    def __init__(self, gerenciador_professores: GerenciadorProfessores):
        # Repassa as dependências para a superclasse da camada infra
        super().__init__(titulo="DETALHES DO PROFESSOR", gerenciador=gerenciador_professores)

    def _exibir_detalhes(self, professor):
        """
        Método hook que define o layout de exibição para a entidade Professor.
        """
        print("-" * 45)
        print(f"ID Professor:     {professor.id_professor:03d}")
        print(f"Nome Docente:     {professor.nome}")
        print(f"Titulação:        {professor.titulacao}")
        print(f"ID Departamento:  {professor.id_departamento:03d}")
        print("-" * 45)
        input("\nPressione [ENTER] para retornar ao menu...")