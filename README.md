<h1>
    📒 Projeto Agenda (PT-BR)
</h1>

Este é um projeto de Agenda de Contatos desenvolvido em Django, com o objetivo de praticar e aplicar conceitos de CRUD (Create, Read, Update e Delete).

Hospedado em: <a href="https://enzortorres.pythonanywhere.com" target="_blank">enzortorres.pythonanywhere.com</a>

🚀 Tecnologias utilizadas
```
○ Django — Framework web principal
○ Pillow — Para manipulação de imagens (ex: fotos dos contatos)
○ Faker — Para geração de dados aleatórios de teste
```

<h2>
    ⚙️ Como rodar o projeto
</h2>

1. Clone o repositório:
```
git clone https://github.com/enzortorres/django-agenda-app.git
```

2. Instale as dependências:
```
pip install -r requirements.txt
```


3. Aplique as migrações:
```
python manage.py migrate
```

(Opcional) Gere dados de teste:

```
python utils/create_contacts.py
```

4. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

5. Acesse no navegador:

```
http://127.0.0.1:8000/
```

<h2>
    📋 Funcionalidades
</h2>

```
○ Cadastro de contatos
○ Listagem de contatos
○ Edição de contatos
○ Exclusão de contatos
○ Busca de contatos
○ Upload de foto de perfil (usando Pillow)
```

<h2>
    📎 Observações
</h2>

```
O script utils/create_contacts.py utiliza o Faker para gerar contatos aleatórios para testes.
Certifique-se que a biblioteca Pillow está instalada para gerenciar imagens.
```


<h2>
    📄 Licença
</h2>

```
Este projeto é apenas para fins de estudo.
```

<br><br><br>

<h1>
    📒 Contacts Agenda Project (EN)
</h1>
This is a Contacts Agenda project developed with Django, aiming to practice and apply CRUD (Create, Read, Update, and Delete) concepts.

Hosted at: <a href="https://enzortorres.pythonanywhere.com" target="_blank">enzortorres.pythonanywhere.com</a>

🚀 Technologies used
```
○ Django — Main web framework
○ Pillow — For image handling (e.g., contact profile pictures)
○ Faker — For generating random test data
```

<h2>
    ⚙️ How to run the project
</h2>

1. Clone the repository
```
git clone https://github.com/enzortorres/django-agenda-app.git
```

2. Install the dependencies:
```
pip install -r requirements.txt
```


3. Apply the migrations:
```
python manage.py migrate
```

(Optional) Generate test data:

```
python utils/create_contacts.py
```

4. Start the development server:
```
python manage.py runserver
```

5. Acess in your browser:

```
http://127.0.0.1:8000/
```

<h2>
    📋 Features
</h2>

```
○ Create new contacts
○ List all contacts
○ Edit existing contacts
○ Delete contacts 
○ Search for contacts 
○ Upload contact profile picture (using Pillow)
```

<h2>
    📎 Notes
</h2>

```
The utils/create_contacts.py script uses Faker to generate random contacts for testing.
Make sure the Pillow library is installed to handle images.
```


<h2>
    📄 License
</h2>

```
This project is for educational purposes only.
```
