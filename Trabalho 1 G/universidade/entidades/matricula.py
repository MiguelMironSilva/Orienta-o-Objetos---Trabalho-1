# framework_universidade/universidade/entidades/matricula.py

from dataclasses import dataclass
from typing import Optional
from infra.entidades.registro import Registro

@dataclass
class Matricula(Registro):
    """
    Entidade de Domínio que representa o vínculo entre um Aluno e um Curso.
    Esta classe resolve o relacionamento N:M (Muitos para Muitos) no modelo
    orientado a objetos.
    """
    
    # O ID é Optional pois a matrícula começa sem identificador até ser salva
    id_matricula: Optional[int]
    id_aluno: int
    id_curso: int
    data_matricula: str
    status: str = "Ativa"  # Ex: "Ativa", "Trancada", "Concluída", "Cancelada"

    def get_rotulo(self) -> str:
        """
        Implementação do contrato 'Registro' para exibição na interface de texto.
        """
        id_str = f"[{self.id_matricula:03d}]" if self.id_matricula else "[NOVA]"
        
        # Como a entidade possui apenas as chaves estrangeiras, exibimos os IDs.
        # (A camada de interface ou negócio pode fazer a "tradução" para os nomes reais)
        return f"{id_str} Aluno ID: {self.id_aluno:03d} -> Curso ID: {self.id_curso:03d} | Status: {self.status.upper()} ({self.data_matricula})"