import config
from cache import Cache
from s3iterable import S3Iterable

class Sou(S3Iterable):
  def __init__(self):
    super(Sou, self).__init__() 
    self.config = config.config()
    self.bucketname = self.config['sou']['bucket']
  
  def metadata(self, subset):
    dh = self.cache.directhandle(self.bucketname, subset)
    o = []
    for l in dh:
      p = l.split('|')
      o.append((p[0],p[1],int(p[2])))
    return o
