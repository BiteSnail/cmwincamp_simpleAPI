from configparser import ConfigParser
import os.path

class myconfigs:
    def __init__(self, default_path: str = ".\src\config\config.ini") -> None:
        if os.path.exists(default_path):
            self.data = ConfigParser()
            self.data.read(default_path)
        else:
            print(default_path + " file is not exist")
            self.data = ConfigParser()
            self.data['DEFAULT'] = {'port':8000,
                                    'appname':"main:app",
                                    'hostname':"127.0.0.1"}
            with open(default_path, 'w') as configfile:
                self.data.write(configfile)
            
    def get_config(self, option: str) -> dict | None:
        try:
            return dict(self.data[option])
        except KeyError as e:
            print(e, "That's option is not in Config")
            return None


if __name__ == "__main__":
    test = myconfigs("config.ini")
    print(type(test.get_config("DEFAULT")))
    print((test.get_config("DEFAULT")))

