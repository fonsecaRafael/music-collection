# music-collection
A small application built with Django Framework, should be able to store artist names, their albums and songs

Como rodar este projeto localmente? (Windows)

* Instale o [python](https://www.python.org/downloads/) 3.8 ou posterior
* Clone ou faça o download do projeto para o seu ambiente local
* Abra um prompt de comando navegue até a raiz do projeto e execute o comando
> pip install -r requirements.txt
* Instale o [postgreSQL](https://www.postgresql.org/download/)
> Você nao precisa de nenhuma ferramenta do Stack Builder mas crie uma senha que lembrará para o super usuario.
* Na aba de pesquisas do windows, digite ***psql*** e abra o shell do postgreSQL
* Pressione enter 4 vezes, o prompt solicitará a senha criada durante a instalação.
* Crie um banco de dados para a aplicação com o comando
> CREATE DATABASE *music_collection*;  
> **Obs:** Você pode alterar *music_collection* para o nome que preferir.
* Existe um diretório chamado *contrib* na raiz do projeto, dentro dele existe o arquivo *env_sample*  
* Copie o arquivo env_sample e cole dentro do diretório *musics*
* Renomeie o arquivo para .env
> **Atenção!** Este arquivo conterá suas variáveis locais e não deve subir para nenhum repositório o nome **.env** já consta no arquivo .gitignore
* Altere as variaveis constantes no arquivo *.env* conforme os seus valores e conforme o template
> **P.S:**  
> ***SECRET_KEY*** deve ser uma string qualquer  
> ***DATABASE_URL*** Os campos do exemplo escritos em maiusculas deve ser alterados, os valores padrão são:  
> **USERNAME** = postgres   
> **PASSWORD** = A senha que você criou na instalação do postgresql  
> **HOST** = localhost  
> **DBNAME** = music_collection se você não alterou o comando fornecido neste guia.
* No prompt de comando que está na raiz do projeto, execute o comando:
> python manage.py migrate  
>
> **Obs:** Este comando irá criar no seu banco de dados local a estrutura que este projeto espera.
* No mesmo terminal, crie um superusuario com o comando:
> python manage.py createsuperuser  
>
> **Obs:** Para fins de teste, você pode colocar *admin* em todos os campos
* Realize a coleta de arquivos estáticos, no mesmo terminal execute o comando:
> python manage.py collectstatic
* Pronto agora vamos rodar o servidor:
> python manage.py runserver  
> 
> **Obs:** Se tudo ocorreu certo, a aplicação estará escutando em http://127.0.0.1:8000 e também pode ser acessado em http://localhost:8000
