# Sistema de Clínica de Consultas

## Importação do modulo datetime
Chamei a importação do modulo datetime em python para utilização da classe datetime e seus metodos como ```.strptime()``` e ```.now()``` ambos para verificação de datas reatroativas no sistema.

## Criação de listas
Criei duas listas ```pacientes = []``` e ```agendamentos = []``` para armazenamento dos dados de pacientes e seus agendamentos, sendo esses dados armazenados e processados durante todo o uso do sistema.

## Cadastramento de Pacientes
O método de cadastramento de pacientes consiste em receber do usuario nome e telefone, sendo verificada possivel duplicidade de pacientes atraves do telefone fornecido.

Após confirmar inexistencia de duplicidade o sistema prossegue armazenando os dados criando um dicionario ```pacientes.append({"nome": nome, "telefone": telefone})``` na lista pacientes, no fim, exibindo para o usuário a mensagem de cadastro bem sucedido.

Porém, caso o telefone já tenha sido cadastrado o sistema informa para o usuário a duplicidade de dados e que o cadastrado não foi concluido, retornando a o menu inicial.

## Listagem de pacientes cadastrados
Para listar os pacientes cadastrados o método inicia verificando se a lista de pacientes não está vazia, ou seja = ```False``` e caso esteja informará ao usuário, retornando para o menu.

Após o método de cadastramento ser bem sucedido o método de listagem de pacientes irá percorrer a lista de pacientes enumerando cada iteração, exibindo os pacientes cadastrados e seus dados.
```print(f"{x}, {paciente['nome']} - {paciente['telefone']}")```

## Marcação de consulta
Semelhante ao cadastramento de pacientes, esse método chamara o ```listar_pacientes()``` caso ele retorne ```False``` retornara ao menu inicial exibindo que nenhum usuário foi cadastrado. 

Caso ```True``` o sistema irá pergunta para o usuário qual o indice do paciente que deseja marca uma consulta.

Quando o usuário informar o indice, sera verificado se o valor informado é valido ```if escolha < 1 or escolha > len(pacientes):```

Se valido prosseguirá para a coleta de dados aonde o usuário irá informar a data, hora e especialidade desejada.

Caso todas as vericações explicadas a seguir forem validadas com sucesso a marcação de consulta irá seguir, armazenando os dados em um dicionario na lista agendamentos.


### Verificando datas retroativas
Utilizando o modulo datetime anteriormente importado, a data fornecida pelo o usuário será transformada em um objeto datetime ```data_consulta = datetime.datetime.strptime(dia,'%d/%m/%Y')```
para ser verificado com a data atual.

### Verificando disponibilidade de data e hora
É iterado em ```agedamento``` todos os elementos de ```agendamentos``` e caso a data e hora sejam iguais a uma data e hora já reservada o sistema não prosseguirá com o agendamento e retornara para o menu.

## Listando os agendamentos
Seguindo a mesma lógica de ```listar_pacientes()``` o método inicia verificando se a lista de agendamentos não está vazia = ```False``` e caso esteja será informado ao usuário, retornando para o menu.

será percorrerida a lista de agendamentos enumerando cada iteração sobre seus elementos, exibindo os pacientes cadastrados, seus dados e agendamentos realizados.

## Cancelamento de consultas
Novamente com a mesma lógica de ```cadastrar_pacientes()``` e ```marcar_consultas``` o método para cancelamento de consultas verifica se ```listar_agendamentos``` retorna ```False```, caso sim voltara para o menu informando que nenhum agendamento existe e caso não prosseguirá perguntando para o usuário um indice de agendamento valido para efetuar o cancelamento ```agendamento = agendamentos.pop(escolha-1```, dessa vez fazendo uso do método ```.pop``` para remover o elemento com o respectivo indice fornecido pelo o usuário, da lista ```agendamentos[]```.

## Menu
Aqui não tem nenhum segredo é somente um loop ```while``` que enquanto ```True``` será executado o bloco de código do "centro de operações" do usuário, exibindo todas as opções das 3 principais funções aqui desenvolvidas, mais uma 4° opção para sair do sistema, encerrando assim o loop desse menu ```while = False```.