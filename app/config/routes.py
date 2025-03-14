from app.controllers.home_controller import home_blueprint
from app.controllers.todo_controller import todo_blueprint

def register_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(todo_blueprint)
