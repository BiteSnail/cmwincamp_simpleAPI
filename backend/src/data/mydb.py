from datetime import datetime
import json
import os.path

class Mydb:
    __DATEFORMAT = "%Y-%m-%d"
    __DEAFULTPATH = ".\src\data\disk.json"
    def __init__(self, path: str = __DEAFULTPATH):
        if os.path.exists(path):
            with open(path, mode='r') as jsonfile:
                json_object = json.load(jsonfile)
                self.__set_db(json_object)
        else:
            self.__db = {}
            self.__disk_update()

    def __set_db(self, json_object:list):
        names=self.__get_attr(json_object, 'username')
        births=list(map(datetime.strptime, 
                    self.__get_attr(json_object, 'birthday'), 
                    [Mydb.__DATEFORMAT]*len(json_object)))
        self.__db = dict(zip(names, births))

    def __get_attr(self, json_object:list, target:str) -> list:
        return [item[target] for item in json_object]

    def __disk_update(self, path: str = __DEAFULTPATH):
        data = []
        idx = 0
        for name, birth in self.__db.items():
            data.append({
                "_id":idx,
                "username":name,
                "birthday":birth.strftime(self.__DATEFORMAT)
            })
            idx += 1
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def get_items(self, iskey:bool = True) -> list:
        return list(self.__db.keys()) if iskey else list(self.__db.values())

    def find_one_select(self, name:str) -> datetime | None:
        try:
            return self.__db[name]
        except KeyError as e:
            print(e, 'is not in db')
            return None
    
    def insert_item(self, name:str, birth:str) -> None:
        self.__db[name] = datetime.strptime(birth, self.__DATEFORMAT)
        self.__disk_update()

if __name__ == "__main__":
    db = Mydb('disk.json')
    print(db.find_one_select('박정현'))
    print(db.get_items())