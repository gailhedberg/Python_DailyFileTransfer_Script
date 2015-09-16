#!/usr/bin/end python

# gail hedberg - daily_file_transfer_2.py
# july 14, 2015
# july 21, 2015 - this is to be a stand alone script - do not include!

""" file_transfer.py copies files from a hard coded source folder to a
hard coded destination folder based on file age. The files must be new or
modified within the past 24 hours. """



import shutil
import os
from os import path
import datetime
from datetime import date, time, timedelta


archived_ctr = 0
ready_to_archive_ctr = 0
src_path = 'c:\users\gail\Desktop\FolderA'
dst_path = 'c:\users\gail\Desktop\FolderB'


def SetSrcPath(path):
  global src_path
  if os.path.exists(path):
    src_path = path
  else: return False


def SetDstPath(path):
  global dst_path
  if os.path.exists(path):
    dst_path = path
  else: return False


def file_has_changed(fname):

# get file modified time
  file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))
  


#get the delta between today and file mod time
  td = datetime.datetime.now() - file_m_time
  

# file can be archived if mod within last 24 hours
  if td.days == 0:
    global ready_to_archive_ctr
    ready_to_archive_ctr = ready_to_archive_ctr + 1
    return True
  else: return False
  


def MainLoop():

  global archived_ctr
  global src_path
  global dst_path

  for fname in os.listdir(src_path):

    src_fname = '%s\%s' % (src_path, fname)
        
    if file_has_changed(src_fname):    
      dst_fname = '%s\%s' % (dst_path, fname)
     
      try:
        shutil.copy2(src_fname, dst_path)
        archived_ctr = archived_ctr + 1
      except IOError as e:
        print 'could not open the file: %s ' % e

  
def PrintResults():
  global ready_to_archive_ctr
  global archived_ctr
   
  print '***   Archive Report for %s   ***' % datetime.datetime.now()
  print '%d files ready for archiving ' % ready_to_archive_ctr
  print '%d files archived' % archived_ctr
  print '***   End of Archive Report   ***'


def GetNumberFilesArchived():
  global archived_ctr
  return archived_ctr


if __name__ == "__main__":

  MainLoop()
  PrintResults()
 
  



