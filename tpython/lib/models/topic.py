from models.lo import LearningObject
import utils.loutils as loutils
import utils.futils
import os
import shutil as sh
 
class Topic(LearningObject):
 
   los: list(LearningObject)
   units: list(LearningObject)
   panelVideos: list(LearningObject)
   panelTalks: list(LearningObject)
   standardLos: list(LearningObject)
   allLos: LearningObject
 
   def __init__(self):
       super().__init__()
       self.los = loutils.reapLos(self)
       self.reap('topic')
       self.link = 'index.html'
       self.lotype = 'topic'
       # Missing setDefaultImage()
 
       for lo in self.los:
           self.allLos = lo
       for lo in self.los:
           if lo.lotype is 'unit':
               self.units = lo
           elif lo.lotype is 'panelvideo':
               self.panelVideos = lo
           elif lo.lotype is 'paneltalk':
               self.panelTalks = lo
           else:
               self.standardLos = lo
 
   def setDefaultImage(self):
       if not self.img and len(self.los) > 0:
           img = self.los[0].folder + '/' + self.los[0].img # Look into !!
           if os.path.exists(img):
               self.img = img
 
   def publish(self, path):
       os.chdir(self.folder)
       topicPath = path + '/' + self.folder
       utils.futils.copyFileToFolder(self.img, topicPath) # Look into !
       # Missing publishLos
       os.chdir('..')

class Unit(Topic):
    los = list()
    def __init__(self):
        super().__init__(self)
        self.lotype = "unit"
        self.standardLos = filter(lambda lo: (lo.lotype is not "panelvideo"), self.los)


