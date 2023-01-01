from src.app import app
from src.config.myconfigs import myconfigs
import uvicorn

if __name__ == "__main__":
    config = myconfigs().get_config('DEFAULT')
    uvicorn.run(config['appname'], host=config['hostname'], port=int(config['port']), reload=True)