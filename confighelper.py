import configparser

from paths import get_game_directory


def game_directory():
    configfile = "config.ini"

    config = configparser.ConfigParser()
    config.read(configfile)

    gamedir = config['General']['GameDirectory']
    if not gamedir:
        gamedir = get_game_directory()
        config['General']['GameDirectory'] = gamedir
        with open(configfile, 'w') as writeconfigfile:
            config.write(writeconfigfile)
    
    return gamedir