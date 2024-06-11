from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete

tasks = []
task_id_control = 1 # task_id foi criada em cima para não ter seus identificadores duplicados, toda vez que fizesse uma requisição

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control # Utilizando global para pegar a referência fora do método
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1 # Soma 1 no identificador
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":  "Nova tarefa criada com sucesso"}) # Retorno em dicionário

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {     
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
                    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

if __name__ == "__main__":
    app.run(debug=True) 
