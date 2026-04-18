# framework_universidade/universidade/console/formularios/departamentos/fe_departamento.py

from infra import FExclusao
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos

class FEDepartamento(FExclusao):
    """
    Formulário responsável por remover um Departamento do sistema.
    Herda o comportamento padrão de confirmação e tratamento de erros da infraestrutura.
    """

    def __init__(self, gerenciador_deptos: GerenciadorDepartamentos):
        # Injeção de dependência: passamos o título e o gerenciador específico
        # para a classe base FExclusao.
        super().__init__(titulo="EXCLUSÃO DE DEPARTAMENTO", gerenciador=gerenciador_deptos)

    # O comportamento de exclusão é 100% herdado:
    # 1. Pede o ID.
    # 2. Busca o Departamento para mostrar o rótulo (ex: "[001] DCEX - Depto de Exatas").
    # 3. Solicita confirmação de segurança.
    # 4. Executa a delegação para o Gerenciador e trata exceções de integridade.