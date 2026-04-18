Docente: Eduardo Kessler Piveta
Discente: Miguel Miron Silva

Este guia explica como configurar e executar o Framework de Gestão Universitária, um sistema desenvolvido com arquitetura em camadas, seguindo princípios de Análise e Projeto de Software como SOLID, Injeção de Dependência e Design Patterns (DAO, Template Method e Factory).

Pré-requisitos
Python 3.10 ou superior.

SQLite3 (já incluso na biblioteca padrão do Python).

Estrutura do Projeto
O projeto está organizado para isolar responsabilidades e facilitar a manutenção:

infra/: Contém a base genérica do sistema (conexão com banco, DAOs abstratos e templates de formulários).

universidade/:

dados/: Implementações específicas de acesso ao banco e o script schema.sql.

entidades/: Classes @dataclass que representam o domínio (Aluno, Curso, etc.).

negocio/: Os "Gerenciadores" que aplicam as regras de negócio e validações.

console/: Camada de interface de usuário (Menus e Formulários).

Como Executar
1. Preparação do Ambiente
Certifique-se de que todos os arquivos estão em seus respectivos diretórios conforme a estrutura acima. O arquivo app.py deve estar na raiz do projeto.

2. Inicialização do Banco de Dados
O sistema está configurado para verificar a existência do arquivo universidade.db ao iniciar. Caso não exista, ele executará automaticamente o script universidade/dados/schema.sql para criar as tabelas.

3. Execução
No terminal, dentro da pasta raiz do projeto, execute:

Bash
python app.py
Funcionamento das Camadas
Inicialização (app.py): O script cria a FabricaDAOSQLite, que gera os DAOs necessários. Estes são injetados nos Gerenciadores, que por sua vez são injetados no MenuPrincipal.

Interface: Ao navegar pelo menu, você acessará os formulários (Inclusão, Alteração, Exclusão, Listagem e Detalhes).

Validação: Qualquer tentativa de inserir dados inválidos (ex: titulação de professor incorreta ou IDs inexistentes) será barrada pela camada de Negócio, disparando um ErroDeValidacao que a interface exibirá de forma amigável.

Persistência: Os dados são salvos de forma permanente no arquivo universidade.db.

Observações Acadêmicas
Este trabalho demonstra o uso de Injeção de Dependência no app.py, permitindo que o sistema seja testado ou expandido para outros bancos de dados com alteração mínima de código.