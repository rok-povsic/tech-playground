import graphene

from flask import Flask, render_template
from flask_graphql import GraphQLView

from data.starwars.schem import starwars_schema

app = Flask(__name__)


@app.route('/')
def hello_world(name=None):
    return render_template("main.html", name=name)


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=starwars_schema, graphiql=True)
)
