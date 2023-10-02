from my_app import app
from my_app import (
    errorHandler,
    studentModule,
    facultyModule,
    userModule,
    auth_middleware,
)
import secrets

# SECRET_KEY = "o@rkfencGQ#MD8UVA5QXi%mhHHgXWYMP"
SECRET_KEY = secrets.token_urlsafe(32)
print(SECRET_KEY)
app.config["SECRET_KEY"] = SECRET_KEY

if __name__ == "__main__":
    app.run(debug=True)
