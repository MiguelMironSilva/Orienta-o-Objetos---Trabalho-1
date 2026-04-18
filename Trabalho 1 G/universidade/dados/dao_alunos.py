# framework_universidade/universidade/dados/dao_alunos.py

from typing import List
from infra import DAOBase
from universidade.entidades import Aluno

class DAOAlunos(DAOBase[Aluno]):
    """
    Data Access Object específico para a entidade Aluno.
    Ganha automaticamente as operações de CRUD (incluir, alterar, excluir, 
    listar_todos, buscar_por_id) da classe DAOBase.
    """

    # =========================================================================
    # IMPLEMENTAÇÃO DOS CONTRATOS DA CLASSE PAI (DAOBase)
    # =========================================================================

    @property
    def _nome_tabela(self) -> str:
        """Informa ao DAOBase qual tabela ele deve atacar nos SQLs gerados."""
        return "aluno"

    @property
    def _chave_primaria(self) -> str:
        """Informa ao DAOBase qual é o nome da coluna de ID."""
        return "id_aluno"

    def _mapear_linha_para_objeto(self, linha) -> Aluno:
        """
        Ensina o DAOBase como converter uma linha do banco (sqlite3.Row) 
        em um objeto Aluno real da aplicação.
        """
        return Aluno(
            id_aluno=linha["id_aluno"],
            nome=linha["nome"],
            data_ingresso=linha["data_ingresso"],
            matricula_ativa=bool(linha["matricula_ativa"]) # Converte o 0/1 do SQLite de volta para booleano
        )

    def _extrair_dicionario(self, objeto: Aluno) -> dict:
        """
        Ensina o DAOBase como desmontar um objeto Aluno em um dicionário 
        para que ele possa montar os comandos INSERT e UPDATE dinamicamente.
        """
        return {
            "id_aluno": objeto.id_aluno,
            "nome": objeto.nome,
            "data_ingresso": objeto.data_ingresso,
            "matricula_ativa": int(objeto.matricula_ativa) # Converte o booleano para 1/0 para o SQLite
        }

    # =========================================================================
    # MÉTODOS ESPECÍFICOS DO DOMÍNIO (Consultas Customizadas)
    # =========================================================================

    def listar_alunos_ativos(self) -> List[Aluno]:
        """
        Exemplo de extensão: O DAOBase faz o CRUD genérico, mas e se precisarmos
        de uma busca muito específica da regra de negócio? Implementamos aqui!
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE matricula_ativa = 1"
        
        # O self.db já está disponível porque a classe pai (DAOBase) inicializou
        linhas = self.db.executar_leitura(query)
        
        # Reutilizamos o mapeador que criamos acima
        return [self._mapear_linha_para_objeto(linha) for linha in linhas]