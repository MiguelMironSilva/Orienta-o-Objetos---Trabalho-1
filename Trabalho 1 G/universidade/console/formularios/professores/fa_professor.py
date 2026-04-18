# framework_universidade/universidade/console/formularios/professores/fa_professor.py

from infra import FAlteracao, ErroDeValidacao
from universidade.entidades.professor import Professor
from universidade.negocio.gerenciador_professores import GerenciadorProfessores

class FAProfessor(FAlteracao):
    """
    Formulário responsável por alterar os dados de um Professor existente.
    """

    def __init__(self, gerenciador_professores: GerenciadorProfessores):
        # Injeção do título e do gerenciador na superclasse genérica
        super().__init__(titulo="ALTERAÇÃO DE PROFESSOR", gerenciador=gerenciador_professores)

    def _coletar_alteracoes(self, professor: Professor) -> Professor:
        
        """
        Método hook para coleta de dados do docente.
        O objeto 'professor' já contém os dados atuais vindos do banco.
        """
        print("\n[DICA] Pressione ENTER sem digitar nada para manter o valor atual.")

        # 1. Alteração do Nome
        novo_nome = input(f"Nome do Professor [{professor.nome}]: ").strip()
        if novo_nome:
            professor.nome = novo_nome

        # 2. Alteração da Titulação
        print("Titulações: Graduado, Especialista, Mestre, Doutor, Pós-Doutor")
        nova_titulacao = input(f"Titulação [{professor.titulacao}]: ").strip()
        if nova_titulacao:
            professor.titulacao = nova_titulacao

        # 3. Alteração do Departamento (Conversão para Inteiro)
        novo_depto = input(f"ID do Departamento [{professor.id_departamento}]: ").strip()
        if novo_depto:
            try:
                professor.id_departamento = int(novo_depto)
            except ValueError:
                raise ErroDeValidacao("O ID do departamento deve ser um número inteiro.")

        # O GerenciadorProfessores validará se a titulação é permitida e 
        # se o ID do departamento faz sentido antes de persistir.
        return professor
