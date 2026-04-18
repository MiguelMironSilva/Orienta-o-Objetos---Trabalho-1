# framework_universidade/universidade/negocio/gerenciador_departamentos.py

from typing import List, Optional
from infra.excecoes.base_errors import ErroDeValidacao
from universidade.entidades.departamento import Departamento
from universidade.dados.dao_departamentos import DAODepartamentos

class GerenciadorDepartamentos:
    """
    Controlador de Regras de Negócio para a entidade Departamento.
    Assegura regras de formatação (siglas sempre em maiúsculas) e 
    integridade de unicidade (evitando siglas duplicadas no sistema).
    """

    def __init__(self, dao_departamentos: DAODepartamentos):
        # Injeção da dependência (recebida lá da FabricaDAOSQLite no MenuPrincipal)
        self.dao = dao_departamentos

    # =========================================================================
    # FLUXO DE ESCRITA (Com Validações de Regras de Negócio)
    # =========================================================================

    def incluir(self, departamento: Departamento) -> Departamento:
        """
        Formata, valida as regras estruturais e garante que a sigla não existe 
        antes de autorizar o cadastro.
        """
        self._validar_e_formatar_dados(departamento)
        self._garantir_sigla_unica(departamento)
        
        return self.dao.incluir(departamento)

    def alterar(self, departamento: Departamento) -> None:
        """
        Formata, valida e garante que a nova sigla não pertença a outro departamento.
        """
        self._validar_e_formatar_dados(departamento)
        self._garantir_sigla_unica(departamento)
        
        self.dao.alterar(departamento)

    def excluir(self, id_departamento: int) -> None:
        """
        Verifica a existência do registro e delega a exclusão.
        Nota de Arquitetura: O banco de dados (via ON DELETE RESTRICT) vai bloquear
        a exclusão se houverem Cursos ou Professores atrelados a este departamento,
        e a infraestrutura exibirá o erro na tela automaticamente.
        """
        self.buscar_por_id(id_departamento)
        self.dao.excluir(id_departamento)

    # =========================================================================
    # FLUXO DE LEITURA (Delegação e Extensões)
    # =========================================================================

    def buscar_por_id(self, id_departamento: int) -> Departamento:
        return self.dao.buscar_por_id(id_departamento)

    def buscar_por_sigla(self, sigla: str) -> Optional[Departamento]:
        """Expõe a busca por sigla para a camada de console (se necessário)."""
        if not sigla:
            raise ErroDeValidacao("A sigla não pode ser vazia para a busca.")
        return self.dao.buscar_por_sigla(sigla.strip().upper())

    def listar_todos(self) -> List[Departamento]:
        return self.dao.listar_todos()

    # =========================================================================
    # MÉTODOS PRIVADOS (Auxiliares de Validação)
    # =========================================================================

    def _validar_e_formatar_dados(self, departamento: Departamento) -> None:
        """
        Sanitiza entradas do usuário e aplica regras de tamanho.
        """
        
        # 1. Sanitização (Formatando por baixo dos panos para o usuário)
        if departamento.nome:
            departamento.nome = departamento.nome.strip().title()
            
        if departamento.sigla:
            # Siglas SEMPRE devem ser salvas em letras maiúsculas
            departamento.sigla = departamento.sigla.strip().upper()

        # 2. Regras de Tamanho
        if not departamento.nome or len(departamento.nome) < 5:
            raise ErroDeValidacao("O nome do departamento deve ter no mínimo 5 caracteres.")
            
        if not departamento.sigla or len(departamento.sigla) < 2 or len(departamento.sigla) > 8:
            raise ErroDeValidacao("A sigla do departamento deve ter entre 2 e 8 caracteres (ex: 'MAT', 'DCEX').")

    def _garantir_sigla_unica(self, departamento: Departamento) -> None:
        """
        Verifica no banco de dados se a sigla solicitada já foi pega por outro departamento.
        """
        depto_existente = self.dao.buscar_por_sigla(departamento.sigla)
        
        if depto_existente is not None:
            # Se encontramos um departamento com essa sigla, precisamos ter certeza 
            # de que não é o próprio departamento sendo alterado.
            if depto_existente.id_departamento != departamento.id_departamento:
                raise ErroDeValidacao(
                    f"A sigla '{departamento.sigla}' já está em uso pelo '{depto_existente.nome}'."
                )