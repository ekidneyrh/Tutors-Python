import os
import glob
import shutil as sh
import frontmatter as fm
import utils.futils as futils
from models.lo import LearningObject

class Chapter:
    
    def __init__(self):
        self.title = ''
        self.shortTitle = ''
        self.contentMd = ''
        self.content = ''
        self.route = ''

class Lab(LearningObject):
    directories = list()
    chapters = list()

    def __init__(self):
        super().__init__()
        self.reap()
        self.link = 'index.html'
        self.lotype = 'lab'
        if os.path.exists('videoid'):
            self.videoid = futils.readFile('videoid')

    def reapChapters(mdFiles):
        chapters = list()
        for chapterName in mdFiles:
            wholeFile = os.read(chapterName)
            contents = fm(wholeFile)
            theTitle = contents[0, contents.index('\n')]
            theTitle = theTitle.replace('\r', '')
            chapter = {
                'file': chapterName,
                'title': theTitle,
                'shortTitle': chapterName[chapterName.index('.') + 1, chapterName.rindex('.')],
                'contentMd': contents,
                'route': '',
                'content': ''
            }
            chapters.append(chapter)
        return chapters
            

    def reap(self):
        mdFiles = glob.glob('*.md').sort
        if len(mdFiles) == 0:
            pass
        resourceName = mdFiles[0].name
        self.reap(resourceName)
        self.directories = futils.getDirectories('.')
        self.chapters = self.reapChapters(mdFiles)
        self.title = self.chapters[0].shortTitle
        self.img = futils.getImageFile('img/main')

    def publish(self, path):
        os.chdir(self.folder)
        labPath = path + '/' + self.folder
        futils.initPath(labPath)
        for directory in self.directories:
            futils.copyFolder(directory, labPath)
        os.chdir('..')