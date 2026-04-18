# framework_universidade/universidade/console/formularios/matriculas/fe_matricula.py

from infra import FExclusao
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas

class FEMatricula(FExclusao):
    """
    Formulário responsável por remover uma Matrícula (vínculo Aluno/Curso).
    Utiliza a lógica padronizada da infraestrutura para garantir a 
    confirmação do usuário antes da remoção física.
    """

    def __init__(self, gerenciador_matriculas: GerenciadorMatriculas):
        # Injeção do título e do gerenciador na superclasse genérica.
        super().__init__(titulo="EXCLUSÃO DE MATRÍCULA", gerenciador=gerenciador_matriculas)

    # O fluxo completo é herdado de FExclusao:
    # 1. Solicita o ID da Matrícula.
    # 2. Exibe o resumo (ex: "Matrícula [05] - Aluno: 10 / Curso: 02").
    # 3. Solicita confirmação "S/N".
    # 4. Remove o registro através do GerenciadorMatriculas.