# framework_universidade/universidade/entidades/aluno.py

from dataclasses import dataclass
from typing import Optional
from infra.entidades.registro import Registro

@dataclass
class Aluno(Registro):
    """
    Entidade de Domínio que representa um Aluno.
    Utiliza @dataclass para gerar automaticamente __init__, __repr__ e __eq__,
    e herda de Registro para garantir compatibilidade com a interface gráfica.
    """
    
    # id_aluno é Optional porque, antes de salvar no banco, o ID não existe (é None)
    id_aluno: Optional[int]
    nome: str
    data_ingresso: str
    matricula_ativa: bool = True  # Valor padrão: todo aluno novo começa ativo

    def get_rotulo(self) -> str:
        """
        Cumpre o contrato da interface abstrata 'Registro' (da camada infra).
        Define como este aluno deve aparecer nas listas e menus de exclusão/alteração.
        """
        status = "Ativo" if self.matricula_ativa else "Inativo"
        
        # Formata o ID para ter 3 dígitos (ex: 001, 012) para alinhar visualmente as listas
        id_str = f"[{self.id_aluno:03d}]" if self.id_aluno else "[NOVO]"
        
        return f"{id_str} {self.nome} - Ingresso: {self.data_ingresso} ({status})"