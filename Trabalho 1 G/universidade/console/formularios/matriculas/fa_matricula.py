# framework_universidade/universidade/console/formularios/matriculas/fa_matricula.py

from infra import FAlteracao, ErroDeValidacao
from universidade.entidades.matricula import Matricula
from universidade.negocio.gerenciador_matriculas import GerenciadorMatriculas

class FAMatricula(FAlteracao):
    """
    Formulário responsável por alterar os dados de uma Matrícula existente.
    Permite atualizar o status do aluno no curso ou corrigir a data de registro.
    """

    def __init__(self, gerenciador_matriculas: GerenciadorMatriculas):
        super().__init__(titulo="ALTERAÇÃO DE MATRÍCULA", gerenciador=gerenciador_matriculas)

    def _coletar_alteracoes(self, matricula: Matricula) -> Matricula:
        
        """
        Hook Method para coleta de dados. 
        Nota: Geralmente não alteramos os IDs de Aluno/Curso de uma matrícula 
        já existente para manter a integridade histórica. Caso o aluno mude 
        de curso, o correto é excluir a antiga e criar uma nova.
        """
        print("\n[DICA] Pressione ENTER sem digitar nada para manter o valor atual.")

        # 1. Alteração do Status
        # Exibe os status válidos para orientar o usuário
        print("Status possíveis: Ativa, Trancada, Concluída, Cancelada")
        novo_status = input(f"Status Atual [{matricula.status}]: ").strip()
        if novo_status:
            matricula.status = novo_status

        # 2. Alteração da Data de Matrícula
        nova_data = input(f"Data da Matrícula (DD/MM/AAAA) [{matricula.data_matricula}]: ").strip()
        if nova_data:
            matricula.data_matricula = nova_data

        # A lógica de negócio no GerenciadorMatriculas impedirá, por exemplo,
        # que uma matrícula 'Concluída' seja alterada ou excluída sem critérios.
        return matricula
