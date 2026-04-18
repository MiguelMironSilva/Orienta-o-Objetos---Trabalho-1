# framework_universidade/universidade/negocio/gerenciador_alunos.py

from typing import List
from infra.excecoes.base_errors import ErroDeValidacao
from universidade.entidades.aluno import Aluno
from universidade.dados.dao_alunos import DAOAlunos

class GerenciadorAlunos:
    """
    Controlador de Regras de Negócio para a entidade Aluno.
    """

    def __init__(self, dao_alunos: DAOAlunos):
        self.dao = dao_alunos

    def incluir(self, aluno: Aluno) -> Aluno:
        self._validar_e_formatar_dados(aluno)
        return self.dao.incluir(aluno)

    def alterar(self, aluno: Aluno) -> None:
        self._validar_e_formatar_dados(aluno)
        self.dao.alterar(aluno)

    def excluir(self, id_aluno: int) -> None:
        self.buscar_por_id(id_aluno)
        self.dao.excluir(id_aluno)

    def buscar_por_id(self, id_aluno: int) -> Aluno:
        return self.dao.buscar_por_id(id_aluno)

    def listar_todos(self) -> List[Aluno]:
        return self.dao.listar_todos()

    def _validar_e_formatar_dados(self, aluno: Aluno) -> None:
        if aluno.nome:
            aluno.nome = aluno.nome.strip().title()

        if not aluno.nome or len(aluno.nome) < 3:
            raise ErroDeValidacao("O nome do aluno deve conter pelo menos 3 caracteres.")
        
        if not aluno.cpf or len(aluno.cpf) != 11:
             raise ErroDeValidacao("O CPF deve conter exatamente 11 dígitos.")
