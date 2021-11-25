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
