 "use strict"
 
 document.addEventListener('DOMContentLoaded', () => {
            const todoForm = document.getElementById('todoForm');
            const todoInput = document.getElementById('todoInput');
            const todoList = document.getElementById('todoList');
            const emptyState = document.getElementById('emptyState');
            const todoCount = document.getElementById('todoCount');
            const clearCompleted = document.getElementById('clearCompleted');
            const filterBtns = document.querySelectorAll('.filter-btn');
            
            let todos = JSON.parse(localStorage.getItem('todos')) || [];
            let currentFilter = 'all';
            
            // Initialize
            renderTodos();
            updateCount();
            
            // Event Listeners
            todoForm.addEventListener('submit', addTodo);
            clearCompleted.addEventListener('click', clearCompletedTodos);
            filterBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    filterBtns.forEach(btn => btn.classList.remove('active'));
                    e.target.classList.add('active');
                    currentFilter = e.target.dataset.filter;
                    renderTodos();
                });
            });
            
            // Functions
            function addTodo(e) {
                e.preventDefault();
                const todoText = todoInput.value.trim();
                
                if (todoText) {
                    const newTodo = {
                        id: Date.now(),
                        text: todoText,
                        completed: false
                    };
                    
                    todos.push(newTodo);
                    saveTodos();
                    todoInput.value = '';
                    renderTodos();
                    updateCount();
                }
            }
            
            function toggleTodo(id) {
                todos = todos.map(todo => {
                    if (todo.id === id) {
                        return {
                            ...todo,
                            completed: !todo.completed
                        };
                    }
                    return todo;
                });
                
                saveTodos();
                renderTodos();
                updateCount();
            }
            
            function deleteTodo(id) {
                todos = todos.filter(todo => todo.id !== id);
                saveTodos();
                renderTodos();
                updateCount();
            }
            
            function clearCompletedTodos() {
                todos = todos.filter(todo => !todo.completed);
                saveTodos();
                renderTodos();
                updateCount();
            }
            
            function renderTodos() {
                let filteredTodos = todos;
                
                if (currentFilter === 'active') {
                    filteredTodos = todos.filter(todo => !todo.completed);
                } else if (currentFilter === 'completed') {
                    filteredTodos = todos.filter(todo => todo.completed);
                }
                
                todoList.innerHTML = '';
                
                if (filteredTodos.length === 0) {
                    emptyState.style.display = 'block';
                } else {
                    emptyState.style.display = 'none';
                    
                    filteredTodos.forEach(todo => {
                        const todoItem = document.createElement('li');
                        todoItem.className = 'todo-item';
                        if (todo.completed) {
                            todoItem.classList.add('completed');
                        }
                        
                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.className = 'todo-checkbox';
                        checkbox.checked = todo.completed;
                        checkbox.addEventListener('change', () => toggleTodo(todo.id));
                        
                        const todoText = document.createElement('span');
                        todoText.className = 'todo-text';
                        todoText.textContent = todo.text;
                        
                        const deleteButton = document.createElement('button');
                        deleteButton.className = 'delete-button';
                        deleteButton.innerHTML = '×';
                        deleteButton.addEventListener('click', () => deleteTodo(todo.id));
                        
                        todoItem.appendChild(checkbox);
                        todoItem.appendChild(todoText);
                        todoItem.appendChild(deleteButton);
                        todoList.appendChild(todoItem);
                    });
                }
            }
            
            function updateCount() {
                const activeTodos = todos.filter(todo => !todo.completed);
                todoCount.textContent = `${activeTodos.length} ${activeTodos.length === 1 ? 'item' : 'items'} left`;
            }
            
            function saveTodos() {
                localStorage.setItem('todos', JSON.stringify(todos));
            }
        });