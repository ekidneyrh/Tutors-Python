from genericpath import exists
import shutil as sh
from os.path import isfile, join
from os import listdir
import os
import logging
from frontmatter import Frontmatter as yaml

def writeFile(folder,filename,contents):
    if not os.path.exists(folder):
        os.mkdir(folder)
    return os.write(folder + '/' + filename, contents)

def readFile(path1):
    if os.path.exists(path1):
        array = os.read(path1).split('\n')
        return array[0].replace('\r', '')
    else:
        logging.warning('Unable to locate ' + path1)

def getImageFile(name):
    validImageTypes = ['png','jpg','jpeg','gif']
    image = ''
    for type in validImageTypes:
        image = name + '.' + type
        if os.path.exists(image):
            return image

def getParentFolder():
    return os.path.basename(os.path.dirname(os.getcwd)) 

def getDirectories(srcpath):
    onlyfiles = [f for f in listdir(srcpath) if isfile(join(srcpath, f))]
    return onlyfiles

def verifyFolder(folder):
    if not os.path.exists(folder):
        os.mkdir('-p', folder)

def copyFileToFolder(src, dest):
    if os.path.exists(src):
        os.mkdir('-p', dest)
        sh.copy('-rf', src, dest)

def copyFolder(src, dest):
    os.mkdir('-p', dest)
    sh.copy('-rf', src, dest)

def readWholeFile(path1):
    if os.path.exists(path1):
        array = os.open(path1)
        return array
    else:
        logging.warning('Unable to locate ' + path1)

def readYaml(path):
    yamldata = ''
    try:
        yamldata = yaml.load(os.open(path, encoding='utf-8'))
    except:
        logging.warning('Tutors ${version} encountered an error reading properties.yaml:')
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.mark.buffer)
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.message)
        logging.warning('Review this file and try again....')
    return yamldata

def readEnrollment(path):
    yamldata = ''
    try:
        yamldata = yaml.load(os.open(path, encoding='utf-8'))
    except:
        logging.warning('Tutors ${version} encountered an error reading the enrollment file:')
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.mark.buffer)
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.message)
        logging.warning('Ignoring enrolling file for the moment....')
    return yamldata

def readCalendar(path):
    yamldata = ''
    try:
        yamldata = yaml.load(os.open(path, encoding='utf-8'))
    except:
        logging.warning('Tutors ${version} encountered an error reading the calendar file:')
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.mark.buffer)
        logging.warning('--------------------------------------------------------------')
        #logging.warning(err.message)
        logging.warning('Ignoring calendar file for the moment....')
    return yamldata


def getHeader(fileName):
    header = ''
    array = os.read(fileName).split('\n')
    if array[0][0] == '#':
        header = array[0][0:2]
    else:
        header = array[0]
    return header

def withoutHeader(fileName):
    content = os.read(fileName)
    line1 = content.index('\n')
    content = content[line1 + 1 : len(content)]    
    content = content.strip()
    line2 = content.index('\n')
    if(line2 > -1):
        content = content[0 : line2]
    return content

def getHeaderFromBody(body):
    array = body.split('\n')
    header = ''
    if array[0][0] == '#':
        header = array[0][0:2]
    else:
        header = array[0]
    return header           

def withoutHeaderFromBody(body):
    content = body
    line1 = content.index('\n')
    content = content[line1 + 1 : len(content)]
    content = content.strip()
    line2 = content.index('\n')
    if line2 > -1:
        content = content[0:line2]
    return content

def initPath(path):
    os.mkdir('-p', path)

