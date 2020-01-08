import yaml

_PATH='/kb/module/data/schema.yaml'

def load_schemas():
  schemas = {}
  with open(_PATH) as fd:
    schemas = yaml.safe_load(fd.read())
  return schemas
