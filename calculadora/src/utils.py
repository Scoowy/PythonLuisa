def appendToken(expression: str, token: str) -> str:
    if expression == 'ERROR':
        expression = ''

    return expression + token


def deleteToken(expression: str) -> str:
    return expression[:-1]


def deleteAllTokens() -> str:
    return ''


def evaluate(expression: str) -> str:
    if expression != '':
        try:
            res = eval(expression)
            return str(res)
        except:
            return 'ERROR'
    else:
        return ''
