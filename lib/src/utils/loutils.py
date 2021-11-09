import os 
import stat 
import glob
import logging
from shutil import copyfile

from models.lo import LearningObject as los


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
    folders = glob.sync(pattern).sort()
    for folder in folders:
        if (os.path.isdir(stat.S_IFLNK(folder))):
            os.chdir(folder)
            lo = locreator(parent)
            los.append(lo)
            os.chdir('..')

    return los

def findTopLos(los, lotype):
    for lo in los: 
        if lo.lotype == lotype:
            los.append(lo)
    return los

def findLos(los, lotype):
    for lo in los:
        if lo.lotype == lotype:
            los.append(lo)
        elif isinstance(Topic, lo):
            result = result.concat(findLos(lo.los, lotype))
        elif isinstance(Unit, lo):
            result = result.concat(findLos(lo.los, lotype))
    return result

def findTalksWithVideos(los, lotype):
    for lo in los:
        if lo.type == 'talk':
            talk = lo.Talk
            if talk.videoid != 'none':
                los.append(lo)
        if isinstance(Topic, los):
            result = result.concat(findTalksWithVideos(lo.los))
    return result

def publishLos(string, los):
    for lo in los:
        logging.info(' -->', lo.title)
        los.append(lo)

def copyResource():
    dest = dest + '/' + src 
    os.mkdir('-p', dest)
    copyfile('-rf', src + '/*.pdf', dest)
    copyfile('-rf', src + '/*.zip', dest)
    copyfile('-rf', src + '/*.png', dest)
    copyfile('-rf', src + '/*.jpg', dest)
    copyfile('-rf', src + '/*.jpeg', dest)
    copyfile('-rf', src + '/*.gif', dest)
