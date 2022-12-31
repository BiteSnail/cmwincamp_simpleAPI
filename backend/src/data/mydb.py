from datetime import datetime
import json

class Mydb:
    __DATEFORMAT = "%Y-%m-%d"
    def __init__(self, default_path: str = ".\src\data\disk.json"):
        try:
            with open(default_path) as jsonfile:
                json_object = json.load(jsonfile)
                self.__set_db(json_object)
        except FileNotFoundError as e:
            print(e)
            return
    def __set_db(self, json_object:list):
        names=self.__get_attr(json_object, 'username')
        births=list(map(datetime.strptime, 
                    self.__get_attr(json_object, 'birthday'), 
                    [Mydb.__DATEFORMAT]*len(json_object)))
        self.__db = dict(zip(names, births))
    def __get_attr(self, json_object:list, target:str) -> list:
        return [item[target] for item in json_object]
    def find_one_select(self, name:str) -> datetime | None:
        try:
            return self.__db[name]
        except KeyError as e:
            print(e, 'is not in db')
            return None

if __name__ == "__main__":
    db = Mydb('disk.json')
    print(db.find_one_select('박정현'))