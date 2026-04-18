# framework_universidade/universidade/console/formularios/alunos/fe_aluno.py

from infra import FExclusao
from universidade.negocio.gerenciador_alunos import GerenciadorAlunos

class FEAluno(FExclusao):
    """
    Formulário responsável por remover um Aluno do sistema.
    Graças ao design Orientado a Objetos (padrão Template Method da infraestrutura), 
    esta classe é puramente declarativa.
    """

    def __init__(self, gerenciador_alunos: GerenciadorAlunos):
        # Apenas passamos o título da tela e o "cérebro" (gerenciador) para a classe pai.
        super().__init__(titulo="EXCLUSÃO DE ALUNO", gerenciador=gerenciador_alunos)

    # 1. Pede o ID para o usuário.
    # 2. Chama self.gerenciador.buscar_por_id() e trata o erro se não achar.
    # 3. Chama o método get_rotulo() da entidade Aluno para mostrar quem é.
    # 4. Imprime: "Deseja realmente excluir este registro? (S/N)"
    # 5. Se o usuário digitar 'S', chama self.gerenciador.excluir(id).
    # 6. Exibe a mensagem de sucesso ou captura erros de banco (ex: chaves estrangeiras).