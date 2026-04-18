# framework_universidade/universidade/negocio/gerenciador_matriculas.py

from typing import List
from infra.excecoes.base_errors import ErroDeValidacao, RegistroNaoEncontradoError
from universidade.entidades.matricula import Matricula
from universidade.dados.dao_matriculas import DAOMatriculas
from datetime import datetime

class GerenciadorMatriculas:
    """
    Controlador de Regras de Negócio para Matrículas.
    Atua como um "escudo" entre a Interface do Usuário (Console) e o 
    Banco de Dados (DAO), garantindo que apenas dados consistentes e 
    que obedeçam às regras da universidade sejam salvos.
    """

    def __init__(self, dao_matriculas: DAOMatriculas):
        # Injeção de Dependência: O gerenciador não cria o banco, ele o recebe.
        self.dao = dao_matriculas

    # =========================================================================
    # FLUXO DE ESCRITA (Com Validações de Regras de Negócio)
    # =========================================================================

    def incluir(self, matricula: Matricula) -> Matricula:
        """
        Valida as regras de negócio antes de permitir uma nova matrícula.
        """
        # Regra 1: Validação de Data
        self._validar_data(matricula.data_matricula)

        # Regra 2: Um aluno não pode se matricular duas vezes no mesmo curso 
        # se a matrícula atual dele ainda estiver "Ativa" ou "Trancada".
        matriculas_existentes = self.dao.listar_por_aluno(matricula.id_aluno)
        
        for mat_existente in matriculas_existentes:
            if mat_existente.id_curso == matricula.id_curso:
                if mat_existente.status in ["Ativa", "Trancada"]:
                    raise ErroDeValidacao(
                        f"O aluno já possui uma matrícula {mat_existente.status.upper()} neste curso!"
                    )

        # Se passou por todas as barreiras (nenhuma exceção foi lançada), manda salvar
        return self.dao.incluir(matricula)

    def alterar(self, matricula: Matricula) -> None:
        """
        Valida as regras antes de atualizar o status de uma matrícula existente.
        """
        self._validar_data(matricula.data_matricula)

        # Regra 3: Validação de Status Permitidos
        status_permitidos = ["Ativa", "Trancada", "Concluída", "Cancelada"]
        # Normaliza a string (ex: 'ativa' vira 'Ativa')
        matricula.status = matricula.status.capitalize() 
        
        if matricula.status not in status_permitidos:
            raise ErroDeValidacao(
                f"Status inválido: '{matricula.status}'. Use apenas: {', '.join(status_permitidos)}"
            )

        self.dao.alterar(matricula)

    def excluir(self, id_matricula: int) -> None:
        """
        Delega a exclusão, mas poderia ter regras (ex: não excluir matrículas concluídas).
        """
        # Busca primeiro para garantir que existe (o DAO já lança erro se não achar)
        matricula_alvo = self.buscar_por_id(id_matricula)
        
        # Regra 4: Segurança Histórica
        if matricula_alvo.status == "Concluída":
            raise ErroDeValidacao("Matrículas de alunos já formados (Concluídas) não podem ser excluídas do histórico.")
            
        self.dao.excluir(id_matricula)

    # =========================================================================
    # FLUXO DE LEITURA (Apenas repassa para o DAO)
    # =========================================================================

    def buscar_por_id(self, id_matricula: int) -> Matricula:
        return self.dao.buscar_por_id(id_matricula)

    def listar_todos(self) -> List[Matricula]:
        return self.dao.listar_todos()

    # =========================================================================
    # MÉTODOS PRIVADOS (Auxiliares de Validação)
    # =========================================================================

    def _validar_data(self, data_texto: str) -> None:
        """
        Tenta converter a string de data para um objeto datetime para garantir 
        que não foram digitados valores absurdos (ex: 32/13/2026).
        """
        try:
            # Tenta fazer o parse no formato brasileiro
            datetime.strptime(data_texto, "%d/%m/%Y")
        except ValueError:
            raise ErroDeValidacao("A data informada é inválida. Utilize o formato DD/MM/AAAA.")