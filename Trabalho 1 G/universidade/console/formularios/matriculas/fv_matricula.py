# framework_universidade/universidade/console/formularios/matriculas/fv_matricula.py

from infra import FVisualizacao
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas

class FVMatricula(FVisualizacao):
    """
    Formulário de Visualização Detalhada de uma Matrícula.
    Mostra o status do vínculo entre um Aluno e um Curso.
    """

    def __init__(self, gerenciador_matriculas: GerenciadorMatriculas):
        # Injeta o título e o gerenciador na classe base da infraestrutura.
        super().__init__(titulo="DETALHES DA MATRÍCULA", gerenciador=gerenciador_matriculas)

    def _exibir_detalhes(self, matricula):
        """
        Método hook para renderizar as informações da matrícula.
        """
        print("-" * 45)
        print(f"ID Matrícula:    {matricula.id_matricula:03d}")
        print(f"ID Aluno:        {matricula.id_aluno:03d}")
        print(f"ID Curso:        {matricula.id_curso:03d}")
        print(f"Data Registro:   {matricula.data_matricula}")
        print(f"Status Atual:    {matricula.status.upper()}")
        print("-" * 45)
        input("\nPressione [ENTER] para retornar...")