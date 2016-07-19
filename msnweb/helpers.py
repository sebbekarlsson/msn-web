from functools import wraps
from msnweb.MSN import MSN


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not MSN.get_current_user():
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def decorate_message(str):
    new_str = ''

    words = str.split(' ')
    for word in words:
        if word.startswith('http'):
            word = '<a href="{url}">{url}</a>'.format(url=word)
        new_str += word + ' '

    line_parts = new_str.split("\n")
    new_str = ''
    for part in line_parts:
        part = "<li>" + part + "</li>"
        new_str += part

    emo_map = [
                {'text': ':)', 'src': '/static/image/emo_smile.png'},
                {'text': ':D', 'src': '/static/image/emo_happy.png'},
                {'text': ':P', 'src': '/static/image/emo_tounge.png'},
                {'text': 'B)', 'src': '/static/image/emo_cool.png'}
            ]
    
    for item in emo_map:
        new_str = new_str.replace(item['text'],
                '<img class="emo" src="{}">'.format(item['src']))

    return new_str

def strip_bad_tags(str):
    str = str.\
            replace('<script>', '<pre>').\
            replace('</script>', '</pre>').\
            replace('<script', '<pre')

    if str.count('<pre') > 0 and str.count('</pre') == 0:
        str += '</pre>'

    return str
