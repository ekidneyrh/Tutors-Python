import os
import glob
from abc import ABC, abstractmethod
from lib.src.models.lo import LearningObject
import utils.futils as futils
import utils.loutils as loutils

class DiscreteLearningObject(LearningObject):
    def __init__(self):
        super().__init__()

    def reap(self, pattern):
        self.link = 'error: missing ' + self.lotype
        resourceList = glob.glob(pattern).sort
        if len(resourceList) > 0:
            resourceName = os.path.split(resourceList[0]['name'])
            self.reap(resourceName)
            self.link = resourceList[0]
        else:
            resourceList = glob.glob('*.md').sort
            resourceName = os.path.split(resourceList[0]['name'])
            self.reap(resourceName)
            self.link = resourceList[0]
    def publish(self, path):
        loutils.copyResource(self.folder, path)

class Talk(DiscreteLearningObject):
    def __init__(self):
        super().__init__()
        self.lotype = 'talk'
        self.reap('*.pdf')


class PanelTalk(DiscreteLearningObject):
    def __init__(self):
        super().__init__()
        self.lotype = 'paneltalk'
        self.reap('*.pdf')

class Archive(DiscreteLearningObject):
    def __init__(self):
        super().__init__()
        self.lotype = 'archive'
        self.reap('*.zip')