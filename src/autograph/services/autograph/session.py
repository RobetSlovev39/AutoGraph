import httpx


class Session:
    ''' Класс для работы с AutoGraph '''

    auth_params: dict | None = None  # Параметры для отправки запросов

    def __init__(self, api: str, login: str, password: str, time_difference: int) -> None:
        self.api, self.login, self.password, self.time_difference = api, login, password, time_difference
        self.auth()

    def auth(self) -> bool:
        response = httpx.post(
            self.api + 'Login',
            json={
                'UserName': self.login,
                'Password': self.password,
                'UTCOffset': self.time_difference
            }
        )

        if response:
            self.auth_params = {'session': response.text}
            return True

        return False

    def post(self, method: str, data: dict) -> dict | bool:
        try:
            response = httpx.post(
                self.api + method,
                data={**data, **self.auth_params},
                timeout=50
            )
        except httpx.ReadTimeout:
            response = self.post(method, data)

        if response:
            return response.json()

        return False

    def get_schemas(self) -> dict | bool:
        '''  Получение схем '''

        return self.post(
            'EnumSchemas', dict()
        )

    def get_devices(self, schema_id: str) -> dict | bool:
        ''' Получение машин '''

        return self.post(
            'EnumDevices', {'schemaID': schema_id}
        )
