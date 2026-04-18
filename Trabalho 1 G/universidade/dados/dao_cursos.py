# framework_universidade/universidade/dados/dao_cursos.py

from typing import List
from infra import DAOBase
from universidade.entidades import Curso

class DAOCursos(DAOBase[Curso]):
    """
    Data Access Object específico para a entidade Curso.
    Herda todo o poder de CRUD genérico do DAOBase.
    """

    # =========================================================================
    # IMPLEMENTAÇÃO DOS CONTRATOS DA CLASSE PAI (DAOBase)
    # =========================================================================

    @property
    def _nome_tabela(self) -> str:
        """Informa ao framework qual tabela do banco de dados deve ser consultada."""
        return "curso"

    @property
    def _chave_primaria(self) -> str:
        """Informa qual coluna é o identificador único (ID)."""
        return "id_curso"

    def _mapear_linha_para_objeto(self, linha) -> Curso:
        """
        Converte o resultado do banco de dados (sqlite3.Row) em uma 
        instância real da classe Curso.
        """
        return Curso(
            id_curso=linha["id_curso"],
            nome=linha["nome"],
            duracao_semestres=linha["duracao_semestres"],
            id_departamento=linha["id_departamento"] # Chave estrangeira para o Departamento
        )

    def _extrair_dicionario(self, objeto: Curso) -> dict:
        """
        Desmonta o objeto Curso em um dicionário para que o DAOBase possa
        montar os comandos INSERT e UPDATE dinamicamente.
        """
        return {
            "id_curso": objeto.id_curso,
            "nome": objeto.nome,
            "duracao_semestres": objeto.duracao_semestres,
            "id_departamento": objeto.id_departamento
        }

    # =========================================================================
    # MÉTODOS ESPECÍFICOS DO DOMÍNIO (Consultas Customizadas)
    # =========================================================================

    def listar_cursos_por_departamento(self, id_departamento: int) -> List[Curso]:
        """
        Exemplo de consulta específica: Busca todos os cursos que pertencem
        a um departamento específico. Isso seria muito útil para um relatório
        ou para uma tela de listagem filtrada.
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE id_departamento = ?"
        
        # self.db é a conexão Singleton herdada do DAOBase
        linhas = self.db.executar_leitura(query, (id_departamento,))
        
        return [self._mapear_linha_para_objeto(linha) for linha in linhas]