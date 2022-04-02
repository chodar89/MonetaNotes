from flask_openapi3 import Info, OpenAPI, Tag
from pydantic import BaseModel

info = Info(title="MonetaNotes", version="1.0.0")


ping_tag = Tag(name="ping", description="test tag")

# instantiate the app
app = OpenAPI(__name__, info=info)

app.config.from_object("src.config.DevelopmentConfig")


class PingQuery(BaseModel):
    id: int


@app.get("/", tags=[ping_tag])
def get_ping(query: PingQuery):
    return {"id": query.id}
