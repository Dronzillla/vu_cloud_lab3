from flask import render_template, Blueprint, redirect, url_for


core = Blueprint("core", __name__, template_folder="templates")


@core.route("/")
def index():
    return render_template("core/index.html")


# Single redirect
@core.route("/about")
def about():
    return redirect(url_for("core.about_page"))


@core.route("/about-page")
def about_page():
    return render_template("core/about.html")


# Chain redirect: /info -> /about -> /about-page
@core.route("/info")
def info():
    return redirect(url_for("core.about"))


# External redirect
@core.route("/github")
def github():
    return redirect("https://github.com")
