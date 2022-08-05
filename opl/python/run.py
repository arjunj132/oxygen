d = dict(locals(), **globals())

def python(code):
  exec(code, d, d)
