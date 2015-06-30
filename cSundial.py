import os
import uuid
from bottle import Bottle, template, run, TEMPLATE_PATH, static_file, request

static_token = str(uuid.uuid1())
static_token_len = len(static_token)

project_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(project_dir, 'tests')
theme_name = 'default'
theme_dir = os.path.join(project_dir, 'themes', theme_name)
template_dir = os.path.join(theme_dir, 'html')

TEMPLATE_PATH.insert(0, template_dir)

app = Bottle()


def send_theme_html(html_path):
    return template(html_path, static_token=static_token)


def dir_json(dir_path):
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            full_file_path = os.path.join(root, f)
            file_list.append({
                'create_datetime': 0,
                'modification_datetime': 0,
                'name': f,
                'path': full_file_path[len(root_dir):],
                'size': 0,
                'isDir': False
            })
        for d in dirs:
            full_dir_path = os.path.join(root, d)
            file_list.append({
                'create_datetime': 0,
                'modification_datetime': 0,
                'name': d,
                'path': full_dir_path[len(root_dir):],
                'size': 0,
                'isDir': True
            })
        break

    return {
        'files': file_list
    }


@app.route('/')
@app.route('/<path:path>')
def requests_handler(path=''):
    cur_path = os.path.join(root_dir, path)

    if path.startswith(static_token):
        static_file_path = os.path.join(theme_dir, path[static_token_len+1:])
        static_file_dir = os.path.dirname(static_file_path)
        static_file_name = os.path.basename(static_file_path)
        return static_file(static_file_name, static_file_dir)
    elif os.path.isdir(cur_path):
        # dir to json
        if request.query.get('type') == 'json' and request.query.get('static_token') == static_token:
            return dir_json(cur_path)

        index_html_file_path = os.path.join(cur_path, 'index.html')
        if os.path.isfile(index_html_file_path) and os.path.exists(index_html_file_path):
            with open(index_html_file_path) as f:
                return f.read()
        else:
            return send_theme_html('dir_listing.html')
    else:
        pass

if __name__ == '__main__':
    run(app, reloader=True, debug=True)
