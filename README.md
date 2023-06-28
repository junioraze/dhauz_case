### DHAUZ-CASE
---
Arquivos:

## Setup: 
* Deve-se criar um virtualenv ou um container docker para executar o arquivo result.py
* Para virtualenv, execute na raiz do repositório:
```
python -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```
* Para o docker, execute na raiz do repositório:
```
docker build --tag dhauz-case .
docker run dhauz-case
```
* É necessário para ambos os casos criar um arquivo .env no diretório contendo o preenchimento dos seguintes campos:
```
USER=seu_usuario_no_banco
PSWD=pswd_do_usuario
HOST=endpoit_do_banco
DB=nome_do_db
```

## Arquivos Principais:
result.py => amalgama do notebook em forma de script
queries.py => todas as consultas executadas
how_to.ipynb => notebook com o processo de resolução
requirements.txt => dependencias para executar de forma isolada o result.py

## Resultado

* O Resultado final deve ser um print conforme abaixo:<br>
  <img src="/utils/resultado.png">

Descritivo:<br>
PRIMEIRA PARTE:<br>
Questão 1 => V1 = ENDEREÇO DA CARTEIRA V2 = VOLUME<br>
Questão 2 => V1 = DIA DA CARTEIRA V2 = VOLUME<br>
Questão 3 => V1 = DIA DA SEMANA (3 = Quinta-Feira) DA CARTEIRA V2 = Realizadas<br>
Questão 4 => Nessa questão o resultado de fato é o inscrito no notebook, que são os valores duplicados e os status diferentes<br>
Questão 5 => V1 = ENDEREÇO DA CARTEIRA V2 = SALDO<br>
<br>
SEGUNDA PARTE:<br>
Questão 4 => V1 = SO DESCRITIVO V2 = VALOR DA MEDIA<br>
Questão 3 => V1 = ID DA TRANSACAO V2 = MAIOR TAXA PAGA<br>
Questão 2 => V1 = ENDEREÇO DA CARTEIRA V2 = MAIOR PAGAMENTO<br>
Questão 1 => V1 = ENDEREÇO DA CARTEIRA V2 = MAIOR PAGAMENTO<br>

TERCEIRA PARTE: 

Para colocar essa solução na nuvem, eu indicaria que fosse construída uma arquitetura serveless. 
Se utilizarmos o script result.py com algumas adequações para se passado como função, podemos inserí-lo em um rotina
de Pub-Sub > aciona execução de Cloud Function result.py > a cloud function insere os dados. Os dados vão ser inserido 
no BigQuery que é uma ótima opção para BD serveless ou salvos como arquivos tabulados no Cloud Storage para utilização como um Lake. 

<img src="/utils/questao.png">