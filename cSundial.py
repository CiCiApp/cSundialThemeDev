import os
import uuid
from bottle import Bottle, template, run, TEMPLATE_PATH

static_token = str(uuid.uuid1())

project_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(project_dir, 'tests')
theme_name = 'solar'
theme_dir = os.path.join(project_dir, 'themes', theme_name)
template_dir = os.path.join(theme_dir, 'html')

TEMPLATE_PATH.insert(0, template_dir)

app = Bottle()


def send_theme_html(html_path):
    return template(html_path, static_token=static_token)


@app.route('/')
@app.route('/<path:path>')
def requests_handler(path=''):
    cur_path = os.path.join(root_dir, path)
    print(cur_path)

    if os.path.isdir(cur_path):
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
