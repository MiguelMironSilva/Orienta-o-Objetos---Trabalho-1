# framework_universidade/universidade/console/formularios/professores/fe_professor.py

from infra import FExclusao
from universidade.negocio.gerenciador_professores import GerenciadorProfessores

class FEProfessor(FExclusao):
    """
    Formulário responsável por remover um Professor do sistema.
    Utiliza a estrutura genérica de exclusão para garantir um fluxo
    seguro e padronizado de remoção de dados.
    """

    def __init__(self, gerenciador_professores: GerenciadorProfessores):
        # Repassa o título e o controlador de negócio para a classe base.
        super().__init__(titulo="EXCLUSÃO DE PROFESSOR", gerenciador=gerenciador_professores)

    # O método executar() herdado garante:
    # 1. Entrada de ID validada.
    # 2. Exibição do nome e titulação do professor antes da exclusão.
    # 3. Confirmação obrigatória do usuário.
    # 4. Tratamento de exceções caso o docente possua vínculos ativos no banco.