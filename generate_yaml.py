def create_yaml(apps):
    result = \
r"""runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /favicon.ico
  static_files: favicon.ico
  upload: favicon.ico"""
    for app in apps:
        name = app['name']
        dir = app['dir']
        prefix = app['prefix']
        routes = \
r"""
- url: {prefix}/(.*)\.json
  static_files: {app_dir}/build/\1.json
  upload: {app_dir}/build/(.*)\.json
- url: {prefix}/static
  static_dir: {app_dir}/build/static
- url: {prefix}/(.*)\.js
  static_files: {app_dir}/build/\1.js
  upload: {app_dir}/build/(.*)\.js
- url: {prefix}/api(.*)
  script: {app_name}.app
- url: {prefix}.*
  static_files: {app_dir}/build/index.html
  upload: {app_dir}/build/index.html
""".format(app_name=name, app_dir=dir, prefix=prefix)

        result = result + routes

    result = result + \
r"""
libraries:
- name: ssl
  version: latest

skip_files:
- ^(.*/)?#.*#$
- ^(.*/)?.*~$
- ^(.*/)?.*\.py[co]$
- ^(.*/)?.*/RCS/.*$
- ^(.*/)?\..*$
- ^(.*/)?node_modules/
"""
    for app in apps:
        dir = app['dir']
        result = result + '- {app_dir}/src/\n'.format(app_dir=dir)
    return result

apps = [
    {
        "name": "main",
        "dir": "client",
        "prefix": ""
    },
]

with open('app.yaml', 'w') as f:
    f.write(create_yaml(apps))
