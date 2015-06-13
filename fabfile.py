from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer
from datetime import datetime

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.theme_path = 'themes'
DEPLOY_PATH = env.deploy_path
THEME_PATH = env.theme_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

author_info = { 'josh': {'name': 'Joshua Loyal',
                         'email': 'jloyal25@gmail.com',
                         'about': 'Data scientist, '
                                  'physicist, wannabe guitar player, '
                                  'and an avid climber.'}
}

def make_entry(title, author_name):
    """ generate a blog post """

    template = """
Title: {title}
Date: {year}-{month}-{day} 
Tags:
Category:
Author: {author}
about_author: {about}
Email: {email}

"""
    
    # derive some info
    today = datetime.today()
    try:
        author = author_info[author_name]
    except KeyError:
        raise KeyError('{} not a valid author'.format(author))
    slug = title.lower().strip().replace(' ', '-')
    
    f_create = 'content/{}/{}_{:0>2}_{:0>2}_{}.md'.format(
        today.year, author_name, today.month, today.day, slug)
    

    t = template.strip().format(title=title, 
                                year=today.year, month=today.month, day=today.day,
                                author=author['name'],
                                about=author['about'],
                                email=author['email'])

    with open(f_create, 'w') as w:
        w.write(t)
    print('File created -> ' + f_create)

def live_build(port=8000):
    """ Setup a livereload server to preview the post as you edit.
        Note: You need to install the python package as well as
              the plugin in your browser of choice.
    """

    try:
        import livereload
    except ImportError:
        raise ImportError('You need to install livereload...')

    # clean everything
    local('make clean')
    local('make html')
    os.chdir('output')

    # setup server and add files you want to watch
    server = livereload.Server()
    server.watch('../content/',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('../templates/pure/',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.serve(liveport=35729, port=port)

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def collectstatic():
    if os.path.isdir(DEPLOY_PATH):
        local('mkdir -p {deploy_path}/images/'.format(**env))
        #local('cp -rf {theme_path}/images/* {deploy_path}/images/'.format(**env))

def build():
    local('pelican -s pelicanconf.py')
    #collectstatic()

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
