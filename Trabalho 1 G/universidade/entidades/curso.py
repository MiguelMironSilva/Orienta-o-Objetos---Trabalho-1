# framework_universidade/universidade/entidades/curso.py

from dataclasses import dataclass
from typing import Optional
from infra.entidades.registro import Registro

@dataclass
class Curso(Registro):
    """
    Entidade de Domínio que representa um Curso oferecido pela Universidade.
    O uso do @dataclass elimina a necessidade de escrever construtores, 
    getters e setters manualmente.
    """
    
    # O ID é Optional porque um Curso recém-criado na tela de Inclusão 
    # ainda não foi salvo no banco e, portanto, não possui um ID.
    id_curso: Optional[int]
    nome: str
    duracao_semestres: int
    id_departamento: int  # Chave estrangeira que vincula o curso ao seu departamento

    def get_rotulo(self) -> str:
        """
        Implementação obrigatória do contrato 'Registro'.
        Define como o curso será renderizado nas listas, menus e telas de confirmação 
        da camada visual (Console).
        """
        # Formata o ID com zeros à esquerda (ex: 005) para manter as tabelas alinhadas,
        # ou exibe [NOVO] se o curso ainda não foi pro banco de dados.
        id_str = f"[{self.id_curso:03d}]" if self.id_curso else "[NOVO]"
        
        return f"{id_str} {self.nome} - {self.duracao_semestres} Semestres (Depto ID: {self.id_departamento})"