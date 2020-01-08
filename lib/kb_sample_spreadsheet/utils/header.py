import yaml

_PATH='/kb/module/data/header.yaml'

def load_headers():
  headers = {}
  with open(_PATH) as fd:
    headers = yaml.safe_load(fd.read())
  return headers
