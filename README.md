# Gestão de Resíduos
A waste management CRUD made in Django. Put into production using fly.io.

# Set up para desenvolvimento:
## Instalar depenências:
`pip install -r requirements-dev.txt`

## Criar arquivo `.env`
1. O arquivo `.env` deve conter duas variáveis de ambiente:
  - `SECRET_KEY`: Uma chave secreta gerada pelo Django para proteção de formuários e cookies
  - `DEBUG`: Uma flag booleana que indica se estamos em um ambiente de produção ou de desenvolvimento.

2. Para setarmos as variáveis no `.env`
  - Dentro da pasta raiz do projeto crie um arquivo chamado `.env`.
  - Se estiver em um ambiente UNIX rode `make django-secret-key`.
    - Esse comando gera uma nova chave secreta e cola ela dentro do `.env`.
  - Se estiver em um ambiente windows, devemos gerar e colar manualmente dentro do `.env`
    - Para isso dentro do interpretador python faça:
      ```
      from django.core.management.utils import get_random_secret_key
      print("SECRET_KEY=" + get_random_secret_key())
      ```
  - Abre o `.env` e cria uma cole `DEBUG=True` após a linha contendo a chave do Django.

## Rodando servidor de desenvolvimento
`python manage.py runserver`

# Estrutura
```
.
├── _dev        Alguns arquivos de criação e preenchimento de tabelas
├── classe      App para cadastro e listagem de Classes de Resíduos
├── core        Configurações do projeto
├── docs        Arquivos de documentação
├── entrada     App para cadastro e listagem da Entrada de Resíduos
├── fornecedor  App para cadastro e listagem de Fornecedores de Serviço
├── home        App para a página de Home
├── localidade  App para cadastro e listagem de Localidades/Franquias
├── saida       App para cadastro e listagem da Saída de Resíduos
└── templates   Templates HTML de cada um dos Apps
```

# Frontend Theme:
- https://demo.themesberg.com/volt/pages/dashboard/dashboard.html
- https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/widgets/
