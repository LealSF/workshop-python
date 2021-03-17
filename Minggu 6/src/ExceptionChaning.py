raise RuntimeError from exc

def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc


# try:
#     open('database.sqlite')
# except IOError:
#     raise RuntimeError from None