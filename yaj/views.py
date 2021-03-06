from flask import send_from_directory

from yaj import app
from yaj.config import YAJ_WEB_ASSETS_DIR, YAJ_DIR

# ---- MAKO templating

from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['yaj/templates'], module_directory='/tmp/mako_modules')

def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    return mytemplate.render(**kwargs)

# ---- Routing

@app.route("/bootstrap/<path:filename>")
def bootstrap(filename):
    return send_from_directory(YAJ_WEB_ASSETS_DIR+"/bootstrap", filename)

@app.route("/bootstrap-native/<path:filename>")
def bootstrap_native(filename):
    return send_from_directory(YAJ_WEB_ASSETS_DIR+"/bootstrap-native", filename)

@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory(YAJ_DIR+"/static/yaj/css", filename)

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory(YAJ_DIR+"/static/yaj/images", filename)

@app.route("/")
def main_page(**kwargs):
    return serve_template("published.mako", publish_id = "announce1", no_comments=True)

@app.route("/about.html")
def about():
    return serve_template("published.mako", publish_id = "about", no_comments=True)
