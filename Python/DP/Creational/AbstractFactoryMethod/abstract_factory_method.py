import json
import yaml
from mysql import connector


class DBConfig:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password


class MySQLClient:
    def __init__(self, config: DBConfig):
        self._config = config
        self.conn = connector.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password,
            port=config.port,
        )

    def server_version(self):
        return self.conn.get_server_version()


class Config:
    def __init__(self):
        self._config = {}

    @property
    def config(self):
        return self._config

    def from_file(self, filename):
        raise NotImplementedError('.from_file method must be implemented')


class YAMLConfig(Config):
    def from_file(self, filename):
        with open(filename, 'r') as f:
            self._config = yaml.safe_load(f)


class JSONConfig(Config):
    def from_file(self, filename):
        with open(filename, 'r') as f:
            self._config = json.load(f)


if __name__ == '__main__':
    json_config = JSONConfig()
    json_config.from_file('./config.json')
    config = json_config.config
    print(config)

    mysql_client = MySQLClient(DBConfig(**config))
    print(mysql_client.server_version())

    yaml_config = YAMLConfig()
    yaml_config.from_file('./config.yml')
    config = yaml_config.config
    print(config)
