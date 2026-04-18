# framework_universidade/universidade/dados/dao_departamentos.py

from typing import Optional
from infra import DAOBase
from universidade.entidades import Departamento

class DAODepartamentos(DAOBase[Departamento]):
    """
    Data Access Object específico para a entidade Departamento.
    Herda todas as operações de banco de dados genéricas da classe pai (DAOBase).
    """

    # =========================================================================
    # IMPLEMENTAÇÃO DOS CONTRATOS DA CLASSE PAI (DAOBase)
    # =========================================================================

    @property
    def _nome_tabela(self) -> str:
        """Informa o nome da tabela no banco SQLite."""
        return "departamento"

    @property
    def _chave_primaria(self) -> str:
        """Informa a coluna que atua como chave primária."""
        return "id_departamento"

    def _mapear_linha_para_objeto(self, linha) -> Departamento:
        """
        Converte a linha retornada pelo banco (sqlite3.Row) em um 
        objeto da entidade Departamento.
        """
        return Departamento(
            id_departamento=linha["id_departamento"],
            nome=linha["nome"],
            sigla=linha["sigla"]
        )

    def _extrair_dicionario(self, objeto: Departamento) -> dict:
        """
        Extrai os dados do objeto Departamento para um dicionário,
        permitindo que o DAOBase gere os SQLs dinâmicos de INSERT e UPDATE.
        """
        return {
            "id_departamento": objeto.id_departamento,
            "nome": objeto.nome,
            "sigla": objeto.sigla
        }

    # =========================================================================
    # MÉTODOS ESPECÍFICOS DO DOMÍNIO (Consultas Customizadas)
    # =========================================================================

    def buscar_por_sigla(self, sigla: str) -> Optional[Departamento]:
        """
        Exemplo de extensão: Busca um departamento específico pela sua sigla.
        Útil para validações antes de inserir um novo departamento, garantindo
        que não existam duas siglas iguais no sistema.
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE sigla = ?"
        
        # Executa a leitura passando a sigla como parâmetro de segurança contra SQL Injection
        linhas = self.db.executar_leitura(query, (sigla,))
        
        if not linhas:
            return None
            
        # Como a sigla deve ser única, retornamos apenas o primeiro resultado mapeado
        return self._mapear_linha_para_objeto(linhas[0])