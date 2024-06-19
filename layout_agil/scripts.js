// Função para adicionar tarefa
function addTask(timeOfDay) {
    var taskText = prompt("Digite a nova tarefa:");
    if (taskText) {
        var listId = timeOfDay === 'day' ? 'day-tasks' : 'night-tasks';
        var taskList = document.getElementById(listId);
        var newTask = document.createElement('li');
        newTask.textContent = taskText;

        var deleteButton = document.createElement('span');
        deleteButton.textContent = '✔';
        deleteButton.className = 'delete-task';

        // Evento para mostrar o botão de exclusão ao passar o mouse sobre a tarefa
        newTask.addEventListener('mouseover', function() {
            deleteButton.style.display = 'inline-block';
        });

        // Evento para ocultar o botão de exclusão ao retirar o mouse de cima da tarefa
        newTask.addEventListener('mouseout', function() {
            deleteButton.style.display = 'none';
        });

        deleteButton.onclick = function() {
            taskList.removeChild(newTask);
        };

        newTask.appendChild(deleteButton);
        taskList.appendChild(newTask);

        // Atualiza os eventos de exibição/ocultação para todas as tarefas
        updateTaskEvents();
    }
}

// Função para atualizar eventos de exibição/ocultação do botão de exclusão
function updateTaskEvents() {
    var deleteButtons = document.querySelectorAll('.delete-task');
    deleteButtons.forEach(function(button) {
        var taskItem = button.parentNode;
        taskItem.addEventListener('mouseover', function() {
            button.style.display = 'inline-block';
        });
        taskItem.addEventListener('mouseout', function() {
            button.style.display = 'none';
        });
    });
}

// Inicializar a lista de tarefas com funcionalidade de remoção
document.addEventListener('DOMContentLoaded', function() {
    updateTaskEvents();

    var deleteButtons = document.querySelectorAll('.delete-task');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            this.parentNode.remove();
        });
    });
});
