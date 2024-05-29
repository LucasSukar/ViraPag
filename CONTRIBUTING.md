# Contribuindo para o Projeto ViraPag 📚
Olá! Obrigado por considerar contribuir para o Projeto ViraPag. Seu apoio é muito apreciado para tornar nossa biblioteca virtual ainda melhor! Antes de começar, por favor, leia este documento para entender como você pode contribuir.


<details><br>
<summary>Configurações do ambiente</summary>
Antes de começar a contribuir para o projeto, é importante configurar corretamente seu ambiente de desenvolvimento. Siga os passos abaixo para garantir que todas as dependências necessárias estejam instaladas:


## Python
Certifique-se de ter o Python instalado em sua máquina. Recomendamos usar a versão 3.7 ou superior.


## Ambiente Virtual
É altamente recomendável criar um ambiente virtual para isolar as dependências do projeto. Você pode usar criar e ativar um ambiente virtual usando os seguintes comandos:<br>
Criar Ambiente Virtual: python -m venv nome-do-ambiente-virtual<br>
Ativar Ambiente Virtual:<br>
Windows - . nome-do-ambiente-virtual/Scripts/activate<br>
MacOS ou Linux - source nome-do-ambiente-virtual/bin/activate	 


## Instalando Dependências
Após configurar seu ambiente virtual, navegue até o diretório raiz do projeto e execute o seguinte comando para instalar todas as dependências necessárias:<br>

pip install Django<br>
pip install python-dotenv<br>   
pip install whitenoise<br>   
pip install requests<br> 


## Configuração do Banco de Dados
Abra o arquivo settings.py localizado no diretório projeto e ajuste as configurações de conexão do banco de dados de acordo com a configuração local do PostgreSQL.


## Migrações do Banco de Dados
Para criar as tabelas necessárias no banco de dados, execute o seguinte comando:<br>

python manage.py migrate<br>


## Executando o Servidor de Desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento executando o seguinte comando:<br>

python manage.py runserver<br>
O servidor estará rodando em http://127.0.0.1:8000/<br>

</details>


<details><br>
<summary>Como Contribuir</summary>

Existem várias maneiras de contribuir para o Projeto ViraPag:<br>


## Resolver problemas: 

Verifique os Issues do projeto para encontrar tarefas abertas atribuídas a você.


## Reportar problemas: 

Se você encontrar algum problema, bug ou tiver uma ideia para uma melhoria e ela não estiver nos issues, sinta-se à vontade para abrir uma issue em nosso repositório no GitHub.


## Enviar solicitações de pull (Pull Requests - PRs): 

Você pode enviar PRs com correções de bugs, novos recursos ou melhorias de documentação.


## Melhorar a documentação: 

Melhorias na documentação são sempre bem-vindas. Isso inclui corrigir erros de ortografia, adicionar exemplos claros ou melhorar a estrutura do documento.

</details>


<details><br>
<summary>Guia de Contribuição</summary>

Aqui estão alguns passos para contribuir para o Projeto ViraPag:

## Fork do Repositório: 

Faça um fork do repositório do Projeto ViraPag para sua própria conta do GitHub.


## Clone o Repositório: 

Clone o repositório do Projeto ViraPag para o seu ambiente de desenvolvimento local.<br>
git clone https://github.com/viniciusdandrade/ViraPag.git


## Crie um Branch: 
Crie um novo branch para trabalhar em sua contribuição.<br>
git checkout -b nome-do-seu-branch


## Faça as Alterações: 
Faça as alterações necessárias em seu branch local. Certifique-se de seguir as convenções de codificação e estilo do projeto.<br>


## Teste suas Alterações: 
Execute os testes locais para garantir que suas alterações não causem regressões.<br>


## Salvar Alterações: 
Após testar e garantir que suas alterações não gere outros problemas, faça o commit e envie para seu repositório forkado.<br>
git add .<br>
git commit -m "Descrição das mudanças"<br>
git push origin nome-do-seu-branch<br>


## Envie um Pull Request: 
Depois de fazer suas alterações, envie um PR para o repositório principal do Projeto ViraPag.


## Aguarde Revisão: 
Aguarde a revisão do seu PR pela equipe do Projeto ViraPag. Este processo pode levar algum tempo, então seja paciente e esteja aberto a feedback e revisões.

</details>

<details><br>
<summary>Código de Conduta</summary>

Por favor, lembre-se de seguir nosso Código de Conduta em todas as interações relacionadas ao projeto.

</details>

<details><br>
<summary>Suporte</summary>

Se você tiver dúvidas ou precisar de suporte, sinta-se à vontade para abrir uma issue ou entrar em contato com a equipe de desenvolvimento do Projeto ViraPag.

</details>

<details><br>
<summary>Reconhecimento</summary>

Agradecemos a todos os contribuidores que dedicaram seu tempo e esforço para melhorar o Projeto ViraPag.

</details>
