from flask import Flask

app = Flask(__name__)
app.secret_key = 'nose'

# esto es un truco para no usar blueprints, los imports que siguen si son necesarios
import static2.python.routes.app

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(ssl_context='adhoc')