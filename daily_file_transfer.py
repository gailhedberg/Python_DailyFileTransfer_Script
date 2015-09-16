# gail hedberg - file_mover.py - using python 2.7
# july 14, 2015
#
# copy files from folder_a to folder_b
# if the files in folder_a have been modified within the past 24 hours
#   copy them to folder_b
#


import shutil
import os
from os import path
import datetime
from datetime import date, time, timedelta


def file_has_changed(fname):
#  print 'in file_has_changed with file : %s' % fname
#  print str(path.getmtime(fname))

# get file modified time
  file_m_time = datetime.datetime.fromtimestamp(path.getmtime(fname))
  
#  print datetime.datetime.now()
#  print file_m_time

  #get the delta between today and filed mod time
  td = datetime.datetime.now() - file_m_time
  
#  print td
#  print 'days : %d' % td.days

 # file can be archived if mod within last 24 hours
  if td.days == 0:
    global ready_to_archive
    ready_to_archive = ready_to_archive + 1
    return True
  else: return False
  


def main():
  global ready_to_archive
  global archived
  ready_to_archive, archived = 0, 0
  
  # src = "c:\users\gail\desktop\foldera"
  # dst = "c:\users\gail\desktop\folderb"

  for fname in os.listdir('c:\users\gail\Desktop\FolderA'):

    src_fname = 'c:\users\gail\Desktop\FolderA\%s' % fname

    if file_has_changed(src_fname):    
      dst_fname = 'c:\users\gail\Desktop\FolderB\%s' % fname
      dst_folder = 'c:\users\gail\Desktop\FolderB'


      try:
        shutil.copy2(src_fname, dst_folder)
        global archived;
        archived = archived + 1
      #  print 'Copying file : %s ' % (src_fname)
      #  print '      To loc : %s ' % (dst_fname)
      except IOError as e:
        print 'could not open the file: %s ' % e
         
        
      
if __name__ == "__main__":

  main()

  print '******   Archive Report for %s   ******' % datetime.datetime.now()
  print '%d files ready for archiving ' % ready_to_archive
  print '%d files archived' % archived
  print '******   End of Archive Report   ******'




