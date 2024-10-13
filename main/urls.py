import user 

from .settings import project

user.user_page.add_url_rule(rule="/user", view_func=user.render_user)
project.register_blueprint(blueprint=user.user_page)