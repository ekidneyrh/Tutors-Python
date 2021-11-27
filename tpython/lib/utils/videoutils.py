  import os
 
class VideoIdentifier:
   service: str
   id: str
   def __init__(self, service: str, id: int):
       self.service = service
       self.id = id
 
class VideoIdentifiers:
   videoid: str
   videoIds: list(VideoIdentifier)
   def __init__(self, videoid: str, videoIds: list(VideoIdentifier)):
       self.videoid = videoid
       self.videoIds = videoIds
 
 
def readVideoIds():
  videos = VideoIdentifiers('',[])
  if os.path.exists(videos.videoid):
      entries = os.read(videos.videoid.split('\n'))
      for entry in entries:
          if entry is not '':
              if 'heanet' in entry:
                  videos.videoIds.append(parseProperty(entry))
              else:
                  videos.videoid = entry
                  videos.videoIds.append({'service': 'youtube', 'id': entry})
  if len(videos.videoIds) > 0:
      videos.videoid = videos.videoIds[len(videos.videoIds)-1].id #TODO Cant access the id
  return videos
 
 
 
def parseProperty(nv):
   nameValue = nv.split('=')
   nameValue[0] = nameValue[0].replace('\r', '')
   nameValue[1] = nameValue[1].replace('\r', '')
   return {'service': nameValue[0], id: nameValue[1]}