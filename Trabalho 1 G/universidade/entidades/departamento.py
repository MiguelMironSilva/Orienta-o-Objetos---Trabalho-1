# framework_universidade/universidade/entidades/departamento.py

from dataclasses import dataclass
from typing import Optional
from infra.entidades.registro import Registro

@dataclass
class Departamento(Registro):
    """
    Entidade de Domínio que representa um Departamento da Universidade.
    Atua como o agrupador lógico para Professores e Cursos.
    """
    
    # O ID é Optional (pode ser None) pois um departamento recém-digitado 
    # na tela de inclusão ainda não foi salvo no banco de dados.
    id_departamento: Optional[int]
    nome: str
    sigla: str

    def get_rotulo(self) -> str:
        """
        Implementação obrigatória do contrato 'Registro' (da infraestrutura).
        Define a aparência do departamento quando listado no console.
        """
        # Formata o ID com 3 dígitos (ex: 001) para manter tabelas perfeitamente alinhadas,
        # ou avisa que é um registro novo se ainda não possuir ID.
        id_str = f"[{self.id_departamento:03d}]" if self.id_departamento else "[NOVO]"
        
        # Exibe a sigla em destaque seguida do nome completo
        return f"{id_str} {self.sigla.upper()} - {self.nome}"