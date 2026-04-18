# framework_universidade/infra/console/formularios/f_listagem.py

from infra.console.formularios.formulario_base import FormularioBase
from infra.console.util.console_util import ConsoleUtil
from typing import Any, List

class FListagem(FormularioBase):
    """
    Formulário genérico para listar todos os registros de uma entidade.
    Ele constrói automaticamente uma tabela alinhada no console baseada 
    nas colunas e atributos informados pelas classes filhas.
    """

    def __init__(self, titulo: str, gerenciador: Any, colunas: List[str], atributos: List[str]):
        """
        :param titulo: O título da tela.
        :param gerenciador: O controlador de negócios para buscar os dados.
        :param colunas: Lista com os nomes dos cabeçalhos da tabela (ex: ["ID", "Nome"]).
        :param atributos: Lista com os nomes exatos das propriedades na classe 
                          (ex: ["id_aluno", "nome"]).
        """
        super().__init__(titulo)
        self.gerenciador = gerenciador
        self.colunas = colunas
        self.atributos = atributos

        # Validação de segurança do framework
        if len(self.colunas) != len(self.atributos):
            raise ValueError("A quantidade de colunas deve ser igual à quantidade de atributos.")

    def executar(self):
        self._mostrar_cabecalho()
        
        try:
            print("Buscando registros no banco de dados...\n")
            registros = self.gerenciador.listar_todos()
            
            if not registros:
                print("[Aviso] Nenhum registro encontrado no sistema no momento.")
            else:
                self._desenhar_tabela(registros)
                print(f"\nTotal de registros encontrados: {len(registros)}")
                
        except Exception as e:
            print(f"\n[Erro Inesperado] Falha ao processar a listagem: {e}")
            
        ConsoleUtil.pausar()

    def _desenhar_tabela(self, registros: List[Any]):
        """
        Método interno (protegido) que desenha uma tabela ASCII alinhada
        dinamicamente, sem precisar de bibliotecas externas.
        """
        # 1. Calcula a largura ideal para cada coluna (tamanho do cabeçalho vs tamanho do dado)
        larguras = [len(col) for col in self.colunas]
        
        for registro in registros:
            for i, atributo in enumerate(self.atributos):
                # getattr() extrai o valor da propriedade do objeto dinamicamente pelo nome
                valor_str = str(getattr(registro, atributo, "N/A"))
                if len(valor_str) > larguras[i]:
                    larguras[i] = len(valor_str)
                    
        # Adiciona um pequeno espaçamento extra (padding)
        larguras = [l + 2 for l in larguras]

        # 2. Desenha o cabeçalho da tabela
        linha_cabecalho = "".join(col.ljust(larguras[i]) for i, col in enumerate(self.colunas))
        print(linha_cabecalho)
        print("-" * sum(larguras))

        # 3. Desenha as linhas de dados
        for registro in registros:
            linha_dados = "".join(
                str(getattr(registro, atributo, "N/A")).ljust(larguras[i]) 
                for i, atributo in enumerate(self.atributos)
            )
            print(linha_dados)