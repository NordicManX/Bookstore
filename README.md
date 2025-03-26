# Bookstore API

A Bookstore API é uma API REST desenvolvida com Django REST Framework, destinada ao gerenciamento de uma livraria. Este sistema permite a administração de produtos (livros), categorias e pedidos, oferecendo uma estrutura robusta e escalável para operações CRUD.

## Sobre o Projeto

A API foi criada para simplificar a gestão de livrarias, permitindo que desenvolvedores integrem facilmente funcionalidades como:

- **Gerenciamento de Produtos:** Criação, consulta, atualização e deleção de livros.
- **Gestão de Categorias:** Organização dos produtos em categorias para facilitar a navegação e filtragem.
- **Processamento de Pedidos:** Registro e acompanhamento dos pedidos realizados pelos usuários.
- **Autenticação Segura:** Suporte a autenticação via token, aumentando a segurança dos endpoints.

## Funcionalidades Principais

- **CRUD Completo:** Operações para gerenciar produtos, categorias e pedidos.
- **Paginação Automática:** Listagem de resultados paginada, facilitando o consumo da API.
- **Integração com Docker:** Suporte para execução em contêineres via Docker e Docker Compose.
- **Testes Automatizados:** Cobertura de testes utilizando pytest e ferramentas de qualidade de código como flake8, black e mypy.
- **CI/CD:** Configurações de integração contínua utilizando GitHub Actions para garantir a qualidade do código.

## Tecnologias Utilizadas

- Python 3.12+
- Django 5.x
- Django REST Framework
- PostgreSQL (opcional – uso de SQLite para desenvolvimento)
- Poetry (gerenciador de dependências)
- Docker e Docker Compose

## Pré-requisitos

- Python 3.12 ou superior
- Poetry

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. **Instalar o Python 3.12+**  
   Faça o download e instale o Python 3.12 ou superior a partir do [site oficial](https://www.python.org/downloads/).  
   Verifique a instalação:
   ```powershell
   python --version
   ```

2. **Instalar o Poetry**  
   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
   ```

3. **Configurar o Poetry no PATH**  
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\rodap\AppData\Roaming\Python\Scripts", "User")
   ```  
   Após executar este comando, feche e reabra o terminal.

## Clonando e Configurando o Projeto

1. **Clonar o repositório**
   ```powershell
   git clone [URL_DO_REPOSITÓRIO]
   cd bookstore
   ```

2. **Instalar as dependências**
   ```powershell
   poetry install
   ```

3. **Ativar o ambiente virtual**
   ```powershell
   poetry shell
   ```  
   > **Importante:** Utilize o ambiente virtual gerenciado pelo Poetry e não o `venv` padrão.

4. **Aplicar as migrações do banco de dados**
   ```powershell
   python manage.py migrate
   ```

5. **Criar superusuário (opcional)**
   ```powershell
   python manage.py createsuperuser
   ```

## Executando o Projeto

Para iniciar o servidor de desenvolvimento:

```powershell
python manage.py runserver
```
A API estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Utilizando Docker

O projeto conta com suporte a Docker para facilitar a configuração e a execução em ambientes isolados:

1. **Construir e iniciar os containers**
   ```powershell
   docker-compose up -d --build
   ```

2. **Executar os testes dentro do container**
   ```powershell
   docker-compose exec -T web python manage.py test
   ```

## Estrutura do Projeto

O projeto está dividido em duas principais aplicações Django:

- **product/**: Gerencia produtos e categorias.
- **order/**: Gerencia os pedidos realizados.

Outros pontos importantes:
- **Admin do Django:** Acesse `/admin/` para utilizar a interface administrativa.
- **Endpoints da API:** Disponíveis em `/api/` (documentação em desenvolvimento) e para autenticação em `/api-token-auth/`.

## Desenvolvimento

Para contribuir e dar continuidade ao projeto, siga as recomendações abaixo:

- **Ativação do ambiente virtual**
  ```powershell
  poetry shell
  ```
- **Migrar alterações nos modelos**
  ```powershell
  python manage.py makemigrations
  python manage.py migrate
  ```
- **Manutenção das dependências (opcional)**
  ```powershell
  pip freeze > requirements.txt
  ```

## Testes e Qualidade de Código

O projeto utiliza uma suíte de testes automatizados e ferramentas de linting para garantir a qualidade do código. Para rodar os testes:
```powershell
python manage.py test
```
Ou, se estiver usando Docker:
```powershell
docker-compose exec -T web python manage.py test
```

## Integração Contínua (CI/CD)

Foram configurados workflows no GitHub Actions para:
- Realizar testes automatizados.
- Verificar a qualidade do código com ferramentas de lint (flake8, black, mypy).


## Contato

**Autor:** Rodrigo Cinelli  
**Email:** rodcinelli@gmail.com  


