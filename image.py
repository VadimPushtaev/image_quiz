import re

class Image(object):
  subclasses = {}

  def __init__(self, filename):
    self.filename = filename

  @classmethod
  def register(cls, *exts):
    def real_register(klass):
      for ext in exts:
        cls.subclasses[ext] = klass
    return real_register

  @classmethod
  def create_from_file(cls, filename):
    ext = None
    m = re.match(r'.+[.]([^.]+)', filename)
    if m:
      ext = m.group()

    return cls.subclasses.get(ext, cls)(filename)

  @property
  def mimetype(self):
    return 'image/jpeg'

@Image.register('jpg', 'jpeg')
class JpegImage(Image):
  @property
  def mimetype(self):
    return 'image/jpeg'

