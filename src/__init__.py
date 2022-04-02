import os

from flask_openapi3 import Info, OpenAPI, Tag
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel

info = Info(title="MonetaNotes", version="1.0.0")

ping_tag = Tag(name="ping", description="test tag")

# instantiate the app
app = OpenAPI(__name__, info=info)

# set flask app config
app.config.from_object(os.getenv("APP_SETTINGS"))

# initiate db
db = SQLAlchemy(app)


class PingQuery(BaseModel):
    id: int


@app.get("/", tags=[ping_tag])
def get_ping(query: PingQuery):
    return {"id": query.id}
