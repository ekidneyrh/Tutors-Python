import os 
import stat 
import glob
import shutil
import logging
from models.lab import Lab
from models.topic import Topic, Unit
from models.lo import LearningObject
from models.course import Course
from models.los import Archive, PanelTalk, Talk
from models.weblos import Git, PanelVideo, Video, Web


def reapLos(LearningObject):
    for 'course' in LearningObject:
        Course = reapLoType('course')
        return Course

    for 'unit' in LearningObject:
        Unit = reapLoType('unit')
        return Unit

    for 'talk' in LearningObject:
        Talk = reapLoType('talk')
        return Talk

    for 'book' in LearningObject:
        Lab = reapLoType('book')
        return Lab

    for 'video' in LearningObject:
        Video = reapLoType('video')
        return Video

    for 'panelvideo' in LearningObject:
        PanelVideo = reapLoType('panelvideo')
        return PanelVideo

    for 'paneltalk' in LearningObject:
        PanelTalk = reapLoType('paneltalk')
        return PanelTalk

    for 'archive' in LearningObject:
        Archive = reapLoType('archive')
        return Archive

    for 'github' in LearningObject:
        Git = reapLoType('github')
        return Git

    for 'web' in LearningObject:
        Web = reapLoType('web')
        return Web
    
    return los
    
def reapLoType(pattern, parent, locreator):
    los = list()
    folders = sorted(glob.sync(pattern))
    for folder in folders:
        if (os.path.isdir(stat.S_IFLNK(folder))):
            os.chdir(folder)
            lo = locreator(parent)
            los.append(lo)
            os.chdir('..')
    return los

def findTopLos(los, objType):
    result = list()
    for object in los: 
        if object.lotype is objType:
            result.append(object)
    return result

def findLos(los, lotype):
    result = list()
    for lo in los:
        if lo.lotype is lotype:
            result.append(lo)
        elif isinstance(lo, Topic):
            result = result.append(findLos(lo.los, lotype))
        elif isinstance(lo, Unit):
            result = result.append(findLos(lo.los, lotype))
    return result

def findTalksWithVideos(los):
    result = list()
    for lo in los:
        if lo.lotype is 'talk':
            talk = lo
            if talk.videoid is not 'none':
                result.append(lo)
        if isinstance(los, Topic):
            result = result.append(findTalksWithVideos(lo.los))
    return result

def publishLos(path, los):
    for lo in los:
        logging.info(' -->', lo.title)
        lo.publish(path)

def copyResource(src, dest):
    dest = dest + '/' + src 
    os.mkdir('-p', dest)
    shutil.copyfile('-rf', src + '/*.pdf', dest)
    shutil.copyfile('-rf', src + '/*.zip', dest)
    shutil.copyfile('-rf', src + '/*.png', dest)
    shutil.copyfile('-rf', src + '/*.jpg', dest)
    shutil.copyfile('-rf', src + '/*.jpeg', dest)
    shutil.copyfile('-rf', src + '/*.gif', dest)
