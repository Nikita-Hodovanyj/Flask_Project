import flask

user_page = flask.Blueprint(
    name = "user_page",
    import_name ="app",
    template_folder = "user/templates"

)