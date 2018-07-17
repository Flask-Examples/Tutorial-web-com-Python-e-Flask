from flask import jsonify, render_template


def configure(app):
    """Function Factories."""

    @app.route("/")
    def index():
        return "Hello!"

    @app.route("/api")
    def api():
        return jsonify(data={'name': 'Bruno'})


    @app.route("/apiv2")
    def apiv2():
        return jsonify(data={'name': 'Bruno'})


    @app.route("/langs")
    def langs():
        languages = ['Python', 'Bash', 'Lua', 'Rust']
        return render_template(
            'index.html',
            title = "Melhores Linguagens",
            linguagens = languages
        )
