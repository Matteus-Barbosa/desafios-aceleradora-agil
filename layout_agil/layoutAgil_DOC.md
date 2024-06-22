# Layout de Lista de Tarefas
## Estrutura HTML
### Importação de fontes e estilos

O documento HTML inicia com a importação da fonte do Google Fonts (Ubuntu) e do arquivo de estilos (styles.css).

### Criação do layout
Indo para o ``<body>``, é utilizado uma estrutura ``<div>`` como principal ``(container)`` para conter a área do menu e do conteúdo.

O menu lateral ``<aside>`` com a classe ``menu`` contém um perfil fictício com foto e informações do usuário, seguido por links de navegação formatados.

A área principal ``<main>`` com a classe ``content`` é dedicada à lista de tarefas, subdividida em tarefas do dia e da noite, cada uma em suas respectivas divisões ``(task-table)``.

### Inclusão do script

No final do ``<body>``, é incluído o script JavaScript (scripts.js) responsável pela funcionalidade dinâmica do sistema de tarefas.

## Estilo CSS
### Estilos gerais

Define a fonte padrão ``(Arial, sans-serif)`` e o fundo da página.
Os estilos específicos para a fonte Ubuntu são aplicados a elementos necessários.

### Layout principal

``container`` usa ``flex`` para distribuir o menu e o conteúdo principal horizontalmente, com alinhamento e espaçamento apropriados.

### Menu lateral

``menu`` possui largura fixa, fundo colorido, texto branco, bordas arredondadas, e uma sombra para destaque.
Elementos como imagem do perfil, nome, descrição, e links de navegação são estilizados individualmente, com foco em centralização e interatividade (ex. ``hover`` nos links).

### Conteúdo principal

``content`` ocupa o espaço disponível, com fundo branco, bordas arredondadas, e sombra.

``tasks`` é um ``flex container`` que divide o espaço igualmente entre as tarefas do dia e da noite.

### Estilo das tabelas de tarefas

``task-table`` possui fundo claro, ``padding``, bordas arredondadas e sombra.

Títulos ``<h2>`` são centralizados e estilizados para destaque.

Listas de tarefas ``<ul e li>`` são estilizadas para uma apresentação clara e interativa enquanto os botões possuem estilos específicos para aparência e interatividade.

## Script JavaScript
### Função addTask(timeOfDay)

Solicita ao usuário a nova tarefa via ``prompt``.

Determina a lista de tarefas correta (``day-tasks`` ou ``night-tasks``) e cria um novo item (``li``).

Adiciona um botão de exclusão (``span``) para cada tarefa, que aparece ao passar o mouse sobre a tarefa.

### Eventos de exibição do botão de exclusão

``mouseover`` e ``mouseout`` alternam a visibilidade do botão de exclusão.

A Função ``updateTaskEvents()`` reaplica os eventos de exibição/ocultação do botão de exclusão a todas as tarefas.

### Inicialização de eventos
Quando o documento HTML é carregado, o código inicializa a funcionalidade de remoção das tarefas existentes.

No evento ``DOMContentLoaded``, aplica a funcionalidade de remoção a todas as tarefas presentes inicialmente na lista.