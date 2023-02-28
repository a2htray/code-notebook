import json
import abc
import psycopg2
import yaml
from mysql import connector

DatabaseDriver = int


class DBConfig:
    DATABASE_DRIVER_MYSQL: DatabaseDriver = 1
    DATABASE_DRIVER_POSTGRES: DatabaseDriver = 2

    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password


class Client(abc.ABC):
    def get_server_version(self):
        raise NotImplementedError


class MySQLClient(Client):
    def __init__(self, config: DBConfig):
        self._config = config
        self.conn = connector.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password,
            port=config.port,
        )

    def get_server_version(self):
        version_tokens = list(self.conn.get_server_version())
        return 'MySQL ' + '.'.join([str(token) for token in version_tokens])


class PostgresClient(Client):
    def __init__(self, config: DBConfig):
        self._config = config
        self.conn = psycopg2.connect(
            database=config.database,
            user=config.user,
            password=config.password,
            host=config.host,
        )

    def get_server_version(self):
        return 'Postgres ' + '.'.join(str(self.conn.server_version).split('000'))


ConfigType = int


class Config:
    CONFIG_JSON: ConfigType = 1
    CONFIG_YAML: ConfigType = 2

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


def create_db_config(filename: str) -> DBConfig:
    if filename.endswith('json'):
        config = JSONConfig()
    if filename.endswith('yml'):
        config = YAMLConfig()

    config.from_file(filename)
    return DBConfig(**config.config)


def create_client(config: DBConfig, database_driver: DatabaseDriver) -> Client:
    if database_driver == DBConfig.DATABASE_DRIVER_MYSQL:
        return MySQLClient(config)
    if database_driver == DBConfig.DATABASE_DRIVER_POSTGRES:
        return PostgresClient(config)


if __name__ == '__main__':
    typ = input('''Select a config type and a database driver
1) use json and MySQL
2) use yaml and Postgres
> ''')
    if typ == '1':
        config = create_db_config('./config.json')
        client = create_client(config, DBConfig.DATABASE_DRIVER_MYSQL)
        print(client.get_server_version())

    if typ == '2':
        config = create_db_config('./config.yml')
        client = create_client(config, DBConfig.DATABASE_DRIVER_POSTGRES)
        print(client.get_server_version())
