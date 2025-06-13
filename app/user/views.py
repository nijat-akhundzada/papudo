import json
from sqlite3 import IntegrityError
from db.user import create


def create_user(request):
    content_length = int(request.headers.get('Content-Length', 0))
    body = request.rfile.read(content_length)
    try:
        user_data = json.loads(body.decode('utf-8'))
        create(**user_data)
        response = {'message': 'Successfully created!'}
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
