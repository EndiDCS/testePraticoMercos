Frameworks utilizados :

Django: Foi escolhido pois é o framework python que mais tenho domínio no momento.

Bootstrap : Foi escolhido pois facilita a criação do front-end de forma responsiva.

Instruções de Uso utilizando Linux:

Abra o terminal e vá para a pasta do projeto

Crie um virtual env: virtualenv -p python3 envname 

ative o virtual env: source ./envname/bin/activate

Instale os requerimentos necessários para rodar o código(disponivel dentro da pasta testePraticoMercos-master): pip install -r requirements.txt

Realize a migração dos banco de dados : python manage.py migrate

Rode o servidor : python manage.py runserver

vá até o browser e acesse o site : localhost:8000

Ok agora tudo está funcionando :)
