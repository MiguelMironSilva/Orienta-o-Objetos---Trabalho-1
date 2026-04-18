# framework_universidade/universidade/console/formularios/professores/fi_professor.py

from infra import FInclusao, ErroDeValidacao
from universidade.entidades.professor import Professor
from universidade.negocio.gerenciador_professores import GerenciadorProfessores

class FIProfessor(FInclusao):
    """
    Formulário responsável pela coleta de dados para cadastrar um novo Professor.
    """

    def __init__(self, gerenciador_professores: GerenciadorProfessores):
        # Inicializa a infraestrutura com o título e o controlador de negócio
        super().__init__(titulo="INCLUSÃO DE PROFESSOR", gerenciador=gerenciador_professores)

    def _coletar_dados(self) -> Professor:
        """
        Coleta os dados do docente. 
        A validação da titulação permitida e a existência do departamento 
        serão processadas na camada de Negócio.
        """
        nome = input("Nome do Professor: ").strip()
        
        print("Titulações: Graduado, Especialista, Mestre, Doutor, Pós-Doutor")
        titulacao = input("Titulação: ").strip()

        # Coleta o ID do departamento com casting para inteiro
        depto_id_str = input("ID do Departamento de Alocação: ").strip()
        try:
            id_depto = int(depto_id_str)
        except ValueError:
            raise ErroDeValidacao("O ID do departamento deve ser um número inteiro.")

        # Retorna a entidade Professor pronta para ser validada e salva
        return Professor(
            id_professor=None,
            nome=nome,
            titulacao=titulacao,
            id_departamento=id_depto
        )