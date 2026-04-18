# framework_universidade/universidade/dados/dao_professores.py

from typing import List
from infra import DAOBase
from universidade.entidades import Professor

class DAOProfessores(DAOBase[Professor]):
    """
    Data Access Object específico para a entidade Professor.
    Delega as operações de CRUD pesado (INSERT, UPDATE, DELETE, SELECT) 
    para o motor genérico do framework (DAOBase).
    """

    # =========================================================================
    # IMPLEMENTAÇÃO DOS CONTRATOS DA CLASSE PAI (DAOBase)
    # =========================================================================

    @property
    def _nome_tabela(self) -> str:
        """Informa ao motor SQL qual é a tabela alvo no banco de dados."""
        return "professor"

    @property
    def _chave_primaria(self) -> str:
        """Informa a coluna que atua como identificador único."""
        return "id_professor"

    def _mapear_linha_para_objeto(self, linha) -> Professor:
        """
        Converte a linha bruta do banco (sqlite3.Row) em uma 
        instância limpa da entidade Professor (@dataclass).
        """
        return Professor(
            id_professor=linha["id_professor"],
            nome=linha["nome"],
            titulacao=linha["titulacao"],
            id_departamento=linha["id_departamento"] # Chave estrangeira para Departamento
        )

    def _extrair_dicionario(self, objeto: Professor) -> dict:
        """
        Desmonta a entidade Professor em um dicionário para 
        geração dinâmica das queries de persistência.
        """
        return {
            "id_professor": objeto.id_professor,
            "nome": objeto.nome,
            "titulacao": objeto.titulacao,
            "id_departamento": objeto.id_departamento
        }

    # =========================================================================
    # MÉTODOS ESPECÍFICOS DO DOMÍNIO (Consultas Customizadas)
    # =========================================================================

    def listar_por_departamento(self, id_departamento: int) -> List[Professor]:
        """
        Exemplo de extensão: Busca o corpo docente de um departamento específico.
        Muito útil para gerar relatórios ou impedir que um departamento seja 
        excluído se ainda tiver professores lotados nele.
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE id_departamento = ?"
        linhas = self.db.executar_leitura(query, (id_departamento,))
        return [self._mapear_linha_para_objeto(linha) for linha in linhas]