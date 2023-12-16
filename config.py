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
    STRING_SESSION = "1BJWap1wBu2MEKc2PVtsg_5aOleCsr05lB62q0TQgSd_ELXQ82Ns-0ZVuw9GvqyRx-alwjYG3U3-hBsLhIYOGZBI2Y28kQtT4HEXF4vTUPiDa8poJzmdSKQkV_AHlpGZe0HpjL69Rsc9gLFQcvjk-TI5qipDfGev5u5ot77Fm1KQLspKYZvJgCLFMr-gwM3tUGLoLHfEACjWVJrOTSpeFConrsBaYnHGDASkMcWPoaPVzveBXawBq0_DRmDYQjuZfOPzyA-XAL8TirjQC9uYvt715EMBxaYaEKUUYKjJNmdODVerwxCjTkf6W5FoUux1zFy8I_nkRYGZ2jkscpIar-OFzYL3OPho="
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
