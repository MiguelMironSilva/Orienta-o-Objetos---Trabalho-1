# framework_universidade/universidade/console/formularios/alunos/fa_aluno.py

from infra import FAlteracao, ErroDeValidacao
from universidade.entidades.aluno import Aluno
from universidade.negocio.gerenciador_alunos import GerenciadorAlunos

class FAAluno(FAlteracao):
    """
    Formulário responsável por alterar os dados de um Aluno existente.
    Herda todo o ciclo de vida (pedir ID, buscar no banco, tratar erros) da classe pai.
    """

    def __init__(self, gerenciador_alunos: GerenciadorAlunos):
        # Passamos o título da tela e a instância do gerenciador (camada de negócio)
        # para a classe pai (FAlteracao) orquestrar o fluxo.
        super().__init__(titulo="ALTERAÇÃO DE ALUNO", gerenciador=gerenciador_alunos)

    def _coletar_alteracoes(self, aluno: Aluno) -> Aluno:
        
        """
        Método 'gancho' (Hook Method) do padrão Template Method.
        A classe pai já pediu o ID para o usuário, já foi no banco, achou o aluno
        e o passou para este método. Agora só precisamos pedir os novos dados.
        """
        print("\n[DICA] Pressione ENTER sem digitar nada para manter o valor atual.")

        # 1. Coleta o novo nome
        novo_nome = input(f"Nome do Aluno [{aluno.nome}]: ").strip()
        if novo_nome:
            aluno.nome = novo_nome

        # 2. Coleta o novo CPF
        novo_cpf = input(f"CPF [{aluno.cpf}]: ").strip()
        if novo_cpf:
            aluno.cpf = novo_cpf

        # 3. Coleta a nova data de ingresso
        nova_data = input(f"Data de Ingresso [{aluno.data_ingresso}]: ").strip()
        if nova_data:
            aluno.data_ingresso = nova_data

        # 3. Coleta o novo status de matrícula
        status_atual = "S" if aluno.matricula_ativa else "N"
        novo_status = input(f"Matrícula Ativa (S/N) [{status_atual}]: ").strip().upper()
        
        if novo_status == "S":
            aluno.matricula_ativa = True
        elif novo_status == "N":
            aluno.matricula_ativa = False
        elif novo_status != "":
            # Se o usuário não apertou ENTER e digitou algo inválido (ex: 'X'),
            # lançamos o erro. A classe FAlteracao capturará isso e mostrará na tela sem "crashar".
            raise ErroDeValidacao("Status inválido. Digite apenas 'S' para Sim ou 'N' para Não.")
        return aluno
