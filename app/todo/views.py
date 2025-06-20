import json
from sqlite3 import IntegrityError
from db.todo import create, update, get_all


def create_todo(request):
    content_length = int(request.headers.get('Content-Length', 0))
    body = request.rfile.read(content_length)
    try:
        todo_data = json.loads(body.decode('utf-8'))
        user_email = todo_data.get("email")
        todo_name = todo_data.get("name")
        create(todo_name, user_email)
        response = {'message': 'Successfully updated!'}
        request.send_response(200)
        request.send_header("Content-Type", "application/json")
        request.end_headers()
        request.wfile.write(json.dumps(response).encode())
    except json.JSONDecodeError:
        request.send_response(400)
        request.end_headers()
        request.wfile.write(b'Invalid JSON')
    except IntegrityError as e:
        request.send_response(400)
        request.end_headers()
        e = str(e)
        error = {'error': e}
        request.wfile.write(json.dumps(error).encode())


def get_todos(request):
    content_length = int(request.headers.get('Content-Length', 0))
    body = request.rfile.read(content_length)
    try:
        body = json.loads(body.decode('utf-8'))
        user = body.get("email")
        response = get_all(email=user)
        request.send_response(200)
        print(response)
        request.send_header("Content-Type", "application/json")
        request.end_headers()
        request.wfile.write(json.dumps(response).encode())
    except json.JSONDecodeError:
        request.send_response(400)
        request.end_headers()
        request.wfile.write(b'Invalid JSON')
    except IntegrityError as e:
        request.send_response(400)
        request.end_headers()
        e = str(e)
        error = {'error': e}
        request.wfile.write(json.dumps(error).encode())

def update_todos(request):
    content_length = int(request.headers.get('Content-Length', 0))
    body = request.rfile.read(content_length)
    try:
        todo_data = json.loads(body.decode('utf-8'))
        update(**todo_data)
        response = {'message': 'Successfully updated!'}
        request.send_response(200)
        request.send_header("Content-Type", "application/json")
        request.end_headers()
        request.wfile.write(json.dumps(response).encode())
    except json.JSONDecodeError:
        request.send_response(400)
        request.end_headers()
        request.wfile.write(b'Invalid JSON')
    except IntegrityError as e:
        request.send_response(400)
        request.end_headers()
        e = str(e)
        error = {'error': e}
        request.wfile.write(json.dumps(error).encode())

