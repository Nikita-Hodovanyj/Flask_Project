import flask
import home_page
from .settings import project

home_page.home.add_url_rule(rule = "/", view_func = home_page.render_home, methods = ["GET", "POST"])

project.register_blueprint(blueprint=home_page.home)
