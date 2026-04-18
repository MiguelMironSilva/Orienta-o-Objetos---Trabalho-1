# framework_universidade/universidade/negocio/gerenciador_cursos.py

from typing import List
from infra.excecoes.base_errors import ErroDeValidacao
from universidade.entidades.curso import Curso
from universidade.dados.dao_cursos import DAOCursos

class GerenciadorCursos:
    """
    Controlador de Regras de Negócio para a entidade Curso.
    Responsável por garantir que dados inválidos ou irreais (ex: um curso de 0 semestres) 
    nunca sejam registrados no banco de dados.
    """

    def __init__(self, dao_cursos: DAOCursos):
        # Injeção de Dependência: recebemos o DAO da fábrica, através do Menu
        self.dao = dao_cursos

    # =========================================================================
    # FLUXO DE ESCRITA (Com Validações de Regras de Negócio)
    # =========================================================================

    def incluir(self, curso: Curso) -> Curso:
        """
        Sanitiza os dados e aplica regras de negócio antes de criar o curso.
        """
        self._validar_e_formatar_dados(curso)
        return self.dao.incluir(curso)

    def alterar(self, curso: Curso) -> None:
        """
        Sanitiza os dados e aplica regras de negócio antes de atualizar o curso.
        """
        self._validar_e_formatar_dados(curso)
        self.dao.alterar(curso)

    def excluir(self, id_curso: int) -> None:
        """
        Delega a exclusão do curso.
        Nota Arquitetural: Se houver matrículas vinculadas a este curso, 
        a restrição ON DELETE RESTRICT do nosso schema.sql lançará um erro do banco,
        que a camada de infraestrutura genérica capturará e mostrará na tela.
        """
        # Garante que o curso existe antes de tentar apagar
        self.buscar_por_id(id_curso)
        self.dao.excluir(id_curso)

    # =========================================================================
    # FLUXO DE LEITURA (Delegação e Extensões)
    # =========================================================================

    def buscar_por_id(self, id_curso: int) -> Curso:
        return self.dao.buscar_por_id(id_curso)

    def listar_todos(self) -> List[Curso]:
        return self.dao.listar_todos()

    def listar_cursos_por_departamento(self, id_departamento: int) -> List[Curso]:
        """
        Consome a pesquisa customizada que definimos lá no DAOCursos.
        """
        if id_departamento <= 0:
            raise ErroDeValidacao("ID do departamento inválido para busca.")
            
        return self.dao.listar_cursos_por_departamento(id_departamento)

    # =========================================================================
    # MÉTODOS PRIVADOS (Auxiliares de Validação)
    # =========================================================================

    def _validar_e_formatar_dados(self, curso: Curso) -> None:
        """
        Centraliza todas as regras e limpeza de dados (DRY - Don't Repeat Yourself).
        """
        
        # 1. Limpeza e Formatação (Sanitização)
        if curso.nome:
            # "  engenharia de software  " -> "Engenharia De Software"
            curso.nome = curso.nome.strip().title()

        # 2. Regra: Tamanho do Nome
        if not curso.nome or len(curso.nome) < 4:
            raise ErroDeValidacao("O nome do curso deve conter pelo menos 4 caracteres.")

        # 3. Regra: Limites de Duração (Semestres)
        # Nenhuma graduação/tecnólogo tem menos de 2 semestres ou mais de 14 semestres
        if not isinstance(curso.duracao_semestres, int):
            raise ErroDeValidacao("A duração do curso deve ser um número inteiro.")
            
        if curso.duracao_semestres < 2 or curso.duracao_semestres > 14:
            raise ErroDeValidacao(
                f"Duração inválida ({curso.duracao_semestres} semestres). "
                "Cursos universitários devem ter entre 2 e 14 semestres."
            )

        # 4. Regra: Vínculo Departamental
        if curso.id_departamento is None or curso.id_departamento <= 0:
            raise ErroDeValidacao("Todo curso deve estar obrigatoriamente vinculado a um Departamento válido.")