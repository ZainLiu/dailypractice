import re

router_dict = {}

def url_map(url):
    def warrper(func):

        def inner(*args,**kwargs):
            response = func(*args,**kwargs)
            return response

        router_dict[url] = inner
        return inner
    return warrper


def application(env,start_response):
    url_path = env['PATH_INFO']
    for path, function in router_dict.items():
        match = re.match(path,url_path)
        if match:
            file_content = function(match)
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    return file_content