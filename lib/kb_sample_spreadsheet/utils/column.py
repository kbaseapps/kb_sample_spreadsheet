import yaml

_PATH='/kb/module/data/column.yaml'

def load_columns():
  columns = {}
  with open(_PATH) as fd:
    columns = yaml.safe_load(fd.read())
  return columns
