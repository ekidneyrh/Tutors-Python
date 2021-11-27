import os
import utils.futils as futils
import utils.loutils as loutils
from models.lo import LearningObject

class WebLearningObject(LearningObject):
    def __init__(self, resourceId):
        super().__init__()
        self.link = futils.readFile(resourceId)
        
class Video(WebLearningObject):
    def __init__(self):
        super().__init__('videoid')
        self.reap('video')
        self.lotype = 'video'
    
    def publish(self, path):
        loutils.copyResource(self.folder, path)

class PanelVideo(WebLearningObject):
    def __init__(self):
        super().__init__('videoid')
        self.reap('panelvideo')
        self.lotype = 'panelvideo'

    def publish(self, path):
        loutils.copyResource(self.folder, path)

class Git(WebLearningObject):
    githubid: str

    def __init__(self):
        super().__init__('githubid')
        self.reap('github')
        self.lotype = 'github'
        self.videoid = 'none'

    def publish(self, path):
        loutils.copyResource(self.folder, path)

class Web(WebLearningObject):
    weburl: str

    def __init__(self):
        super().__init__('weburl')
        self.reap('web')
        self.lotype = 'web'

    def publish(self, path):
        loutils.copyResource(self.folder, path)
