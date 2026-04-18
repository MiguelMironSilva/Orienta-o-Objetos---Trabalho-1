# framework_universidade/universidade/dados/dao_matriculas.py

from typing import List
from infra import DAOBase
from universidade.entidades import Matricula

class DAOMatriculas(DAOBase[Matricula]):
    """
    Data Access Object específico para a entidade Matricula.
    Responsável por gerenciar o vínculo (muitos-para-muitos) entre Alunos e Cursos.
    """

    # =========================================================================
    # IMPLEMENTAÇÃO DOS CONTRATOS DA CLASSE PAI (DAOBase)
    # =========================================================================

    @property
    def _nome_tabela(self) -> str:
        """Informa o nome da tabela associativa no banco SQLite."""
        return "matricula"

    @property
    def _chave_primaria(self) -> str:
        """Informa a chave primária da tabela de matrículas."""
        return "id_matricula"

    def _mapear_linha_para_objeto(self, linha) -> Matricula:
        """
        Converte a linha retornada pelo banco de dados em um objeto Matricula.
        """
        return Matricula(
            id_matricula=linha["id_matricula"],
            id_aluno=linha["id_aluno"],       # Chave estrangeira para Aluno
            id_curso=linha["id_curso"],       # Chave estrangeira para Curso
            data_matricula=linha["data_matricula"],
            status=linha["status"]
        )

    def _extrair_dicionario(self, objeto: Matricula) -> dict:
        """
        Extrai os dados da Matricula para que o framework possa
        salvá-los ou atualizá-los dinamicamente.
        """
        return {
            "id_matricula": objeto.id_matricula,
            "id_aluno": objeto.id_aluno,
            "id_curso": objeto.id_curso,
            "data_matricula": objeto.data_matricula,
            "status": objeto.status
        }

    # =========================================================================
    # MÉTODOS ESPECÍFICOS DO DOMÍNIO (Consultas Customizadas)
    # =========================================================================

    def listar_por_aluno(self, id_aluno: int) -> List[Matricula]:
        """
        Exemplo de extensão 1: Busca todas as matrículas de um aluno específico.
        Essencial para mostrar o histórico do aluno na tela.
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE id_aluno = ?"
        linhas = self.db.executar_leitura(query, (id_aluno,))
        return [self._mapear_linha_para_objeto(linha) for linha in linhas]

    def listar_por_curso(self, id_curso: int) -> List[Matricula]:
        """
        Exemplo de extensão 2: Busca todas as matrículas atreladas a um curso.
        Essencial para gerar a lista de chamada dos professores, por exemplo.
        """
        query = f"SELECT * FROM {self._nome_tabela} WHERE id_curso = ?"
        linhas = self.db.executar_leitura(query, (id_curso,))
        return [self._mapear_linha_para_objeto(linha) for linha in linhas]