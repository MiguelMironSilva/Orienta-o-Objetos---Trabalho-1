# framework_universidade/universidade/console/formularios/departamentos/fi_departamento.py

from infra import FInclusao
from universidade.entidades.departamento import Departamento
from universidade.negocio.gerenciador_departamentos import GerenciadorDepartamentos

class FIDepartamento(FInclusao):
    """
    Formulário responsável pela coleta de dados para criação de um novo Departamento.
    """

    def __init__(self, gerenciador_deptos: GerenciadorDepartamentos):
        # Inicializa a classe base com o título e o gerenciador de departamentos
        super().__init__(titulo="INCLUSÃO DE DEPARTAMENTO", gerenciador=gerenciador_deptos)

    def _coletar_dados(self) -> Departamento:
        """
        Implementação do método hook para capturar os dados via console.
        """
        nome = input("Nome do Departamento: ").strip()
        sigla = input("Sigla (ex: MAT, DCEX, dirc): ").strip()
        
        # Retorna a entidade Departamento. 
        # O id_departamento é None pois o SQLite o gerará automaticamente.
        return Departamento(
            id_departamento=None, 
            nome=nome, 
            sigla=sigla
        )