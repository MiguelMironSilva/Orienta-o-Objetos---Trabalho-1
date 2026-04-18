# framework_universidade/universidade/negocio/gerenciador_alunos.py

from typing import List
from datetime import datetime
from infra.excecoes.base_erros import ErroDeValidacao
from universidade.entidades.aluno import Aluno
from universidade.dados.dao_alunos import DAOAlunos

class GerenciadorAlunos:
    """
    Controlador de Regras de Negócio para a entidade Aluno.
    Garante a integridade, formatação e validade dos dados antes que 
    eles alcancem a camada de persistência (DAO).
    """

    def __init__(self, dao_alunos: DAOAlunos):
        # Injeção de Dependência da camada de dados
        self.dao = dao_alunos

    # =========================================================================
    # FLUXO DE ESCRITA (Com Validações de Regras de Negócio)
    # =========================================================================

    def incluir(self, aluno: Aluno) -> Aluno:
        """
        Aplica regras de formatação e negócio antes de cadastrar um aluno.
        """
        self._validar_e_formatar_dados(aluno)
        
        # Como é uma inclusão nova, garantimos que a matrícula nasça ativa
        aluno.matricula_ativa = True
        
        return self.dao.incluir(aluno)

    def alterar(self, aluno: Aluno) -> None:
        """
        Aplica regras de formatação e negócio antes de atualizar um aluno.
        """
        self._validar_e_formatar_dados(aluno)
        self.dao.alterar(aluno)

    def excluir(self, id_aluno: int) -> None:
        """
        Verifica se o aluno existe e delega a exclusão ao DAO.
        Nota: No nosso schema.sql, configuramos ON DELETE CASCADE para matrículas.
        Portanto, ao excluir o aluno aqui, o banco limpará o histórico dele automaticamente.
        """
        # Apenas garante que não estamos tentando apagar um fantasma
        self.buscar_por_id(id_aluno)
        self.dao.excluir(id_aluno)

    # =========================================================================
    # FLUXO DE LEITURA (Delegação direta)
    # =========================================================================

    def buscar_por_id(self, id_aluno: int) -> Aluno:
        return self.dao.buscar_por_id(id_aluno)

    def listar_todos(self) -> List[Aluno]:
        return self.dao.listar_todos()

    def listar_alunos_ativos(self) -> List[Aluno]:
        """Consome a extensão customizada que criamos no DAOAlunos."""
        return self.dao.listar_alunos_ativos()

    # =========================================================================
    # MÉTODOS PRIVADOS (Auxiliares de Validação)
    # =========================================================================

    def _validar_e_formatar_dados(self, aluno: Aluno) -> None:
        """
        Centraliza as regras de negócio para não repetir código 
        nos métodos incluir() e alterar().
        """
        
        # 1. Limpeza e Formatação (Sanitização)
        # Remove espaços inúteis nas pontas e força as iniciais em maiúsculas (Title Case)
        # Ex: " miguel  miron " -> "Miguel Miron"
        if aluno.nome:
            aluno.nome = aluno.nome.strip().title()

        # 2. Regra de Negócio: Tamanho do Nome
        if