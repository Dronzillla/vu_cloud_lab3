from blueprintapp.app import create_app

# For production
# flask_app = create_app(config_class="config.config.ProductionConfig")
# For development
flask_app = create_app()


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0")
