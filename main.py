import graphene

from flask import Flask, render_template
from flask_graphql import GraphQLView

from data.starwars.schem import starwars_schema

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template("hello.html", name=str(starwars_schema))


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=starwars_schema, graphiql=True)
)
