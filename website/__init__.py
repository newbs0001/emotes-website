from flask import Flask, g

import os

from . import views, models, admin_views, discord

def before_request():
    g.user = discord.User.current()
    g.guilds = discord.BriefGuild.managed()

def create_app(conf):
    app = Flask(__name__)
    app.config.update(
        MAX_CONTENT_LENGTH=2*1024*1024, # 2 MiB max upload
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    app.config.from_object(conf)

    app.config['UPLOAD_FOLDER'] = os.path.realpath(app.config['UPLOAD_FOLDER'])

    try:
        os.makedirs(app.config['UPLOAD_FOLDER'])
    except OSError:
        pass

    if 'http://' in app.config['OAUTH2_REDIRECT_URI']:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'

    app.before_request(before_request)

    # extension lazy init
    admin_views.admin.init_app(app)
    models.db.init_app(app)
    models.migrate.init_app(app, models.db)
    views.csrf.init_app(app)

    app.register_blueprint(views.main)
    return app
