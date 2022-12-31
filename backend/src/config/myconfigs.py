from configparser import ConfigParser

class myconfigs:
    def __init__(self, default_path: str = ".\src\config\config.ini") -> None:
        try:
            self.data = ConfigParser()
            self.data.read(default_path)
        except AttributeError as e:
            print(e, default_path + " file is not exist")
            self.data = ConfigParser()
            self.data['DEFAULT'] = {'port':8000,
                                    'appname':"app:app",
                                    'hostname':"127.0.0.1"}
            with open('config.ini', 'w') as configfile:
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

