import graphene

from flask import Flask, render_template

from flask_graphql import GraphQLView

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template("hello.html", name=name)


class Query(graphene.ObjectType):
    hello = graphene.String(description="Typical hello world")

    def resolve_hello(self, args, context, info):
        return "World"

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
