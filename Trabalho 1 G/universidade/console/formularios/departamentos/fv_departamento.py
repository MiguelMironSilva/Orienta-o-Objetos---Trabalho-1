# framework_universidade/universidade/console/formularios/departamentos/fv_departamento.py

from infra import FVisualizacao
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos

class FVDepartamento(FVisualizacao):
    """
    Formulário de Visualização Detalhada de um Departamento.
    Exibe a sigla e o nome por extenso da unidade acadêmica.
    """

    def __init__(self, gerenciador_deptos: GerenciadorDepartamentos):
        # Passa o título e o gerenciador para a classe base da infraestrutura
        super().__init__(titulo="DETALHES DO DEPARTAMENTO", gerenciador=gerenciador_deptos)

    def _exibir_detalhes(self, depto):
        """
        Método hook para renderizar as informações do departamento na tela.
        """
        print("-" * 45)
        print(f"ID:    {depto.id_departamento:03d}")
        print(f"Sigla: {depto.sigla}")
        print(f"Nome:  {depto.nome}")
        print("-" * 45)
        input("\nPressione [ENTER] para retornar...")