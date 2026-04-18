# framework_universidade/universidade/console/formularios/cursos/fa_curso.py

from infra import FAlteracao, ErroDeValidacao
from universidade.entidades.curso import Curso
from universidade.negocio.gerenciador_cursos import GerenciadorCursos

class FACurso(FAlteracao):
    """
    Formulário responsável por alterar os dados de um Curso existente.
    """

    def __init__(self, gerenciador_cursos: GerenciadorCursos):
        # Repassa o título e a inteligência de negócios para a superclasse
        super().__init__(titulo="ALTERAÇÃO DE CURSO", gerenciador=gerenciador_cursos)

    def _coletar_alteracoes(self, curso: Curso) -> Curso:
        
        """
        Método 'gancho' chamado pela FAlteracao. 
        Neste ponto, o 'curso' já foi validado e buscado no banco de dados.
        """
        print("\n[DICA] Pressione ENTER sem digitar nada para manter o valor atual.")

        # 1. Altera o nome
        novo_nome = input(f"Nome do Curso [{curso.nome}]: ").strip()
        if novo_nome:
            curso.nome = novo_nome

        # 2. Altera a duração em semestres (Requer conversão para inteiro)
        nova_duracao = input(f"Duração (semestres) [{curso.duracao_semestres}]: ").strip()
        if nova_duracao:
            try:
                curso.duracao_semestres = int(nova_duracao)
            except ValueError:
                raise ErroDeValidacao("A duração informada deve ser um número inteiro (ex: 8).")

        # 3. Altera o vínculo com o departamento (Requer conversão para inteiro)
        novo_depto = input(f"ID do Departamento [{curso.id_departamento}]: ").strip()
        if novo_depto:
            try:
                curso.id_departamento = int(novo_depto)
            except ValueError:
                raise ErroDeValidacao("O ID do departamento deve ser um número numérico válido.")

        # Note que não checamos aqui se a duração é menor que 2 ou se o departamento existe.
        # Isso é responsabilidade do GerenciadorCursos! A tela apenas coleta e tipa os dados.
        return curso
