from ..autograph import autograph_session


def auth() -> bool:
    autograph_session.auth()
    return autograph_session.auth_params
