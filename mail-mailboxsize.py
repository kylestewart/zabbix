import mailMonitorClass
import sys
import getopt
import os.path

mail = mailMonitorClass.mailMonitor()

if len(sys.argv) == 1:
  exit()

owner = sys.argv[1]

if owner in mail.find_mailboxes():
  size = mail.mailbox_size(owner)
  print size

