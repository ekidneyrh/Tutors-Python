from models.lo import LearningObject
from utils.properties import Properties
import utils.futils as futils
import utils.loutils as loutils
import topic as Topic
import os
from abc import ABC, abstractmethod
 
class Course(LearningObject):
   enrollment: Properties
   calendar: Properties
   los: list(LearningObject)
   walls: list(LoWall)
   def insertCourseRef(self, los):
      for lo in los:
          lo.course = self
      if lo is Topic:
          self.insertCourseRef(lo.los)
      self.course = self
 
   def __init__(self):
      super().__init__()
      self.los = futils.reapLos({'parent': self})
      self.lotype = 'course'
      self.reap('course')
      ignoreList = self.properties
      if ignoreList:
          for lo in self.los:
              if ignoreList.properties.index(lo.folder) >= 0:
                  los = list()
                  los.append(lo)
                  for learnobj in self.los:
                      lo.hide = True
     
 
 
class LoWall:
   course: Course
   isWall: bool
   los: list
