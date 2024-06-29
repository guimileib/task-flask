# Task Management API

Este projeto é uma API de gerenciamento de tarefas simples usando Flask. A API permite criar, ler, atualizar e excluir tarefas.

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a definição da API.
- `models/task.py`: Contém a definição do modelo `Task`.

## Endpoints

### Criar Tarefa

**Endpoint:** `/tasks`  
**Método:** `POST`  
**Descrição:** Cria uma nova tarefa.  
**Parâmetros:**
- `title` (string): Título da tarefa.
- `description` (string, opcional): Descrição da tarefa.

**Exemplo de Requisição:**
```json
{
    "title": "Estudar Flask",
    "description": "Aprender como criar APIs usando Flask"
}
```

**Exemplo de Resposta:**
```json
{
    "message": "Nova tarefa criada com sucesso",
    "id": 1
}
```

### Listar Tarefas

**Endpoint:** `/tasks`  
**Método:** `GET`  
**Descrição:** Lista todas as tarefas.

**Exemplo de Resposta:**
```json
{
    "tasks": [
        {
            "id": 1,
            "title": "Estudar Flask",
            "description": "Aprender como criar APIs usando Flask",
            "completed": false
        }
    ],
    "total_tasks": 1
}
```

### Obter Tarefa

**Endpoint:** `/tasks/<int:id>`  
**Método:** `GET`  
**Descrição:** Obtém os detalhes de uma tarefa específica por ID.

**Exemplo de Resposta:**
```json
{
    "id": 1,
    "title": "Estudar Flask",
    "description": "Aprender como criar APIs usando Flask",
    "completed": false
}
```

**Exemplo de Resposta (Erro):**
```json
{
    "message": "Não foi possível encontrar a atividade"
}
```

### Atualizar Tarefa

**Endpoint:** `/tasks/<int:id>`  
**Método:** `PUT`  
**Descrição:** Atualiza os detalhes de uma tarefa específica por ID.

**Parâmetros:**
- `title` (string): Título da tarefa.
- `description` (string): Descrição da tarefa.
- `completed` (boolean): Status de conclusão da tarefa.

**Exemplo de Requisição:**
```json
{
    "title": "Estudar Flask",
    "description": "Aprender como criar APIs usando Flask",
    "completed": true
}
```

**Exemplo de Resposta:**
```json
{
    "message": "Tarefa atualizada com sucesso"
}
```

**Exemplo de Resposta (Erro):**
```json
{
    "message": "Não foi possível encontrar a atividade"
}
```

### Deletar Tarefa

**Endpoint:** `/tasks/<int:id>`  
**Método:** `DELETE`  
**Descrição:** Deleta uma tarefa específica por ID.

**Exemplo de Resposta:**
```json
{
    "message": "Tarefa deletada com sucesso"
}
```

**Exemplo de Resposta (Erro):**
```json
{
    "message": "Não foi possível encontrar a atividade"
}
```

## Instruções de Execução

1. Certifique-se de ter o Python e o Flask instalados.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o comando `python app.py` para iniciar a aplicação.
5. Acesse a API em `http://127.0.0.1:5000/`.

## Estrutura do Modelo `Task`

O modelo `Task` deve ter a seguinte estrutura:

```python
class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT.

## Autor

Criado por [guimileib](https://github.com/guimileib)

---

Este script é distribuído sob a licença MIT. Sinta-se à vontade para contribuir e melhorar este projeto!
