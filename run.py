from app.app import application
import os


@application.route('/', methods=['GET'])
def index():
    return "Welcome to PeterPark application."


if __name__ == '__main__':
    application.run(host=os.getenv('APPLICATION_HOST'),
                    port=os.getenv('APPLICATION_PORT'),
                    debug=os.getenv('APPLICATION_DEBUG'))
