import json
from http import HTTPStatus

from flask import Flask, Response
from strawberry.flask.views import GraphQLView
from .schema import schema


app = Flask(__name__)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema)
)


@app.get("/")
def index():
    return Response(
        json.dumps({"status": "awesome"}),
        status=HTTPStatus.OK,
        headers={"content-type": "application/json"},
    )
