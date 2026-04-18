# framework_universidade/universidade/negocio/gerenciador_professores.py

from typing import List
from infra.excecoes.base_errors import ErroDeValidacao
from universidade.entidades.professor import Professor
from universidade.dados.dao_professores import DAOProfessores

class GerenciadorProfessores:
    """
    Controlador de Regras de Negócio para a entidade Professor.
    Garante que os docentes sejam cadastrados com titulações padronizadas
    e vinculados corretamente a um departamento existente.
    """

    def __init__(self, dao_professores: DAOProfessores):
        # Injeção de dependência fornecida pelo orquestrador (MenuPrincipal)
        self.dao = dao_professores

    # =========================================================================
    # FLUXO DE ESCRITA (Com Validações de Regras de Negócio)
    # =========================================================================

    def incluir(self, professor: Professor) -> Professor:
        """
        Aplica formatação e validações estritas antes de cadastrar um docente.
        """
        self._validar_e_formatar_dados(professor)
        return self.dao.incluir(professor)

    def alterar(self, professor: Professor) -> None:
        """
        Aplica formatação e validações estritas antes de atualizar um docente.
        """
        self._validar_e_formatar_dados(professor)
        self.dao.alterar(professor)

    def excluir(self, id_professor: int) -> None:
        """
        Verifica a existência do registro e delega a exclusão ao DAO.
        """
        self.buscar_por_id(id_professor)
        self.dao.excluir(id_professor)

    # =========================================================================
    # FLUXO DE LEITURA (Delegação e Extensões)
    # =========================================================================

    def buscar_por_id(self, id_professor: int) -> Professor:
        return self.dao.buscar_por_id(id_professor)

    def listar_todos(self) -> List[Professor]:
        return self.dao.listar_todos()

    def listar_por_departamento(self, id_departamento: int) -> List[Professor]:
        """
        Consome a pesquisa customizada que definimos no DAOProfessores.
        """
        if id_departamento <= 0:
            raise ErroDeValidacao("ID do departamento inválido para busca.")
        return self.dao.listar_por_departamento(id_departamento)

    # =========================================================================
    # MÉTODOS PRIVADOS (Auxiliares de Validação)
    # =========================================================================

    def _validar_e_formatar_dados(self, professor: Professor) -> None:
        """
        Centraliza todas as regras de limpeza de strings e integridade do domínio.
        """
        
        # 1. Limpeza e Formatação de Nome
        if professor.nome:
            professor.nome = professor.nome.strip().title()

        if not professor.nome or len(professor.nome) < 3:
            raise ErroDeValidacao("O nome do professor deve ter no mínimo 3 caracteres.")

        # 2. Padronização Rigorosa de Titulação Acadêmica
        titulacoes_permitidas = ["Graduado", "Especialista", "Mestre", "Doutor", "Pós-Doutor"]
        
        if professor.titulacao:
            # "  MESTRE  " -> "Mestre"
            professor.titulacao = professor.titulacao.strip().title()

            # Corrige variações comuns digitadas por erro de digitação do usuário
            if professor.titulacao in ["Pos-Doutor", "Pos Doutor", "Pós Doutor"]:
                professor.titulacao = "Pós-Doutor"

        if professor.titulacao not in titulacoes_permitidas:
            raise ErroDeValidacao(
                f"Titulação '{professor.titulacao}' não reconhecida pelo MEC/Universidade.\n"
                f"Utilize apenas: {', '.join(titulacoes_permitidas)}."
            )

        # 3. Regra: Vínculo Departamental Obrigatório
        if professor.id_departamento is None or professor.id_departamento <= 0:
            raise ErroDeValidacao("Todo professor deve estar obrigatoriamente vinculado a um Departamento válido.")