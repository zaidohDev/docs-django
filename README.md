# docs-django
1 - criar diretorio : projetos-django/

2 - dentro de projetos-django/ um subdiretorio para as envs: projetos-django/envs/:

3 - dentro do subdireitorio criado use o comando para criar uma env: python3 -m venv env-polls

4 - agora ative env usando o ./bin/activate

5 - dentro do direitorio root do diretorio criado e com a venv ativada, instale o django via pip:
pip install django==2.1.

6 - crie o projeto django: django-admin startproject mysite

7 - entre dentro da pasta criada no item 6 e aplique: python manage.py runserve

8 - abra o navegador padrao e acesse o endereço http://127.0.0.1:8000/

9 - crie um app para o projeto: python manage.py startapp polls

10 -chame uma view simples de polls e import : from django.http import HttpRespons

11 - crie uma urls dentro de polls e configure ela para include na url do projeto

    11.1 - dessecando o path: 
        11.1.1 -path() argument: route
        11.1.1 -path() argument: view
        11.1.1 -path() argument: kwargs
        11.1.1 -path() argument: name

12 - aplique python manage.py runserv para acesse novamente a pagina e verifique a mensagem a view criada.

13 - Configuração do banco de dados:

    13.1 - Altere o banco padrão do django para o postgres
        13.1.1 - configure o banco no arquivo settings.py.
        13.1.2 - provavelmente precisará instalar o psycopg2 e o psycopg2-binary, use o pip.
        13.1.3 - faça as migrações.
        13.1.4 - crie o superuser.
        13.1.5 - verifique o banco criado por meio de um gerenciador de banco de dados.

14 - configure mysite/settings.py, mude TIME_ZONE para o seu fuso horário,

15 - Criando modelos: Em nossa simples aplicação de enquete, nós iremos criar dois modelos: Question e Choice.
Uma Question tem uma pergunta e uma data de publicação. Uma Choice tem dois campos: o texto da escolha e um
totalizador de votos. Cada Choice é associada a uma Question.

    15.1 - Edite o arquivo polls/models.py

    15.2- Ativando modelos:

        15.2.1 - Para incluir a aplicação no nosso projeto, precisamos adicionar a referência à classe de configuração
        da aplicação na definição do INSTALLED_APPS . A classe PollsConfig``está no arquivo  :file:`polls/apps.py`,
        então seu caminha pontuado é ``'polls.apps.PollsConfig'. Edite o arquivo mysite/settings.py e adicione aquele
        caminho com notação de ponto a definição do INSTALLED_APPS.

    152.2 - rode o comando python manage.py makemigrations

        152.2.1 - usando o comando python manage.py sqlmigrate polls 0001. O comando sqlmigrate na realidade não roda
        o SQL no seu banco de dados - ele apenas o exibe na tela para que você saiba qual SQL o Django acha que é
        necessário. É útil para verificar o que Django vai fazer ou se você tem administradores de bancos de dados que
        necessitam dos scripts SQL para mudanças.

        15.2.2 - agora rode o migrate: python manage.py migrate.

    15.3 - três passos para fazer mudanças nos seus modelos:

        15.3.1 - Mude seus modelos (em models.py).
        15.3.2 - Rode python manage.py makemigrations para criar migrações para suas modificações.
        15.3.3 - Rode python manage.py migrate para aplicar suas modificações no banco de dados.

16 - Brincando com a API

    16.1 - Para invocar o shell do Python, use esse comando: python manage.py shell. Nós usaremos isso em vez de
    simplesmente digitar “python”, porque o manage.py configura a variável de ambiente DJANGO_SETTINGS_MODULE, O que
    da ao Django o caminho de importação Python do arquivo mysite/settings.py.

        16.1.1 - from polls.models import Choice, Question
        16.1.2 - Question.objects.all()
        16.1.3 - from django.utils import timezone
        16.1.4 - q = Question(question_text="What's new?", pub_date=timezone.now())
        16.1.5 - q.save()
        16.1.6 - q.id
        16.1.7 - q.question_text
        16.1.8 - q.pub_date

    16.2 - editando o models.py e deixando Question e Choice mais amigavel com o uso do __str__

17 - O site de administração vem ativado por padrão. Vamos iniciar o servidor de desenvolvimento e explora-lo.
Se o servidor não estiver sendo executado, inicie-o da seguinte forma:

    17.1 - Torne a aplicação de enquetes editável no site de administração:

        17.1.1 - polls/admin.py : admin.site.register(Question), faça as devida importações.
        17.1.2 - rode o runserver e entre no admin e veirifique o ambiente.
# docs-django
