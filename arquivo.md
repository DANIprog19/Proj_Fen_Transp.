# 📂 Estrutura do Projeto Backend
## 1. 🗂️ Camada de Banco de Dados (/db)
- connection.py: É o arquivo que contém o "motor" de acesso.
Nele são feitos as configurações para abrir e fechar a conexão com o SQLite e os comandos SQL básicos para buscar ou salvar dados.
## 2. 🗂️ Camada de Modelos (/models)
Nessa pasta contém programas responsáveis por representar as "entidades" ou os objetos do sistema.
- leitura_model.py: Define como uma leitura de vazão deve ser estruturada (ID, valor, data, ID do sensor).
sensor_model.py: Define o que é um sensor (Nome, Modelo, Localização).
## 3. 🗂️ Camada de Serviços (/services)
Nessa pasta ficam as regras de negócio.
- leitura_service.py: Contém o cálculo matemático da vazão (volume / tempo).
- sensor_service.py: Gerencia a lógica de negócio dos sensores, como verificar se um sensor pode ser cadastrado ou buscar a lista de aparelhos que estão em atividade.
## 4. 🗂️ Camada de Controladores (/controllers)
Nessa pasta contém a delegação das tarefas.
- leituras_controller.py: Recebe os dados brutos da web, pede para validar e conferir, mandar o Service calcular e decidir o que responder para o usuário.
- sensores_controllers.py: Gerencia as requisições sobre os aparelhos (cadastrar, listar ou excluir).
## 5. 🗂️ Camada de Rotas (/routes)
Define os endereços (URLs) do site.
- leituras.py: Cria as rotas como /leituras/calcular.
- sensores.py: Cria as rotas como /sensores/cadastro.
- login.py: Cria uma rota que verifica usuário e senha através do banco de dados.
## 6. 🗂️ Camada de Utilidades (/utils)
Ferramentas de suporte que ajudam o projeto.
- validators.py: Verifica se o usuário não digitou algo errado(ex: tempo negativo ou campos vazios).
- error.py: Se algo der errado, ele garante que o sistema responda uma mensagem de erro.
## 7. 🗂️ Interface (/templates)
- index.html: É um teste de página web. É nele que foi feito o teste do backend, onde o usuário interage com os formulários e vê os resultados do dashboard.
## 8. 📄 Arquivo Principal (Raiz)
- app.py: É o arquivo que executa. Ele liga o servidor Flask, registra todas as rotas e coloca o site no ar.
