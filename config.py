from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 8302922
    API_HASH = "04fb2a067d35256dd92cfe0423af6504"
    # the name to display in your alive message
    ALIVE_NAME = "AF2024"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://AF2024:amirrezaL90@cluster0.ospggan.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5108409464:AAGPhvkZL6ReRtvMNUrnSJ6ilg53aauGvmU"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001565806068
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
