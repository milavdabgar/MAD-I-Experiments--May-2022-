from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.models import Article

@app.route("/", methods=["GET", "POST"])
def articles():
    app.logger.info("Inside get all articles using info")
    articles = Article.query.all()    
    app.logger.debug("Inside get all articles using debug")
    return render_template("articles.html", articles=articles)

@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
def articles_by_author(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    return render_template("articles_by_author.html", articles=articles, username=user_name)
