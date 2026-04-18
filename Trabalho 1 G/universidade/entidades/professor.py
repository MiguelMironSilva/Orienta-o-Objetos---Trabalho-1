# framework_universidade/universidade/entidades/professor.py

from dataclasses import dataclass
from typing import Optional
from infra.entidades.registro import Registro

@dataclass
class Professor(Registro):
    """
    Entidade de Domínio que representa um Professor da Universidade.
    """
    
    # O ID é Optional pois o professor começa sem identificador até ser salvo no banco
    id_professor: Optional[int]
    nome: str
    titulacao: str  # Ex: "Especialista", "Mestre", "Doutor"
    id_departamento: int  # Chave estrangeira vinculando o professor ao seu departamento

    def get_rotulo(self) -> str:
        """
        Implementação do contrato 'Registro' para padronizar a exibição 
        nas telas de listagem, alteração e exclusão do framework (infra).
        """
        id_str = f"[{self.id_professor:03d}]" if self.id_professor else "[NOVO]"
        
        # Formata a exibição para destacar a titulação e o nome do docente
        return f"{id_str} Prof. {self.nome} ({self.titulacao}) - Depto ID: {self.id_departamento}"