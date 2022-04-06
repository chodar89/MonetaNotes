from typing import Optional

from flask_openapi3 import APIBlueprint, Tag
from pydantic import BaseModel

ping_tag = Tag(name="ping", description="test tag")


ping_bp = APIBlueprint(
    "/ping", __name__, url_prefix="/ping", abp_tags=[ping_tag], doc_ui=True
)


class PingQuery(BaseModel):
    id: Optional[int]


@ping_bp.get("/")
def get_ping(query: PingQuery):
    """Health check endpoint"""
    return {"id": query.id}
