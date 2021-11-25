from ..autograph import autograph_session


def auth() -> bool:
    ''' Обновление token'а '''

    autograph_session.auth()
    return autograph_session.auth_params
