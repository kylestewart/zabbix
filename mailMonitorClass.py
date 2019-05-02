import os
import os.path
import json

class mailMonitor:

  def find_mailboxes(self):
    maildata = []
    for root,dirs,files in os.walk("/home"):
      for name in dirs:
        if name == "Maildir":
          maildata.append({"{#MBOWNER}": os.path.basename(root)})
    json.JSONEncoder(maildata)
    return(json.dumps(maildata,separators=(',',':')).encode())

  def mailbox_size(self,mbowner):
    path = "/home/" + mbowner + "/Maildir"
    size = 0
    for root,dirs,files in os.walk(path):
      for message in files:
        message_file = os.path.join(root,message)
        size += os.path.getsize(message_file)
    return(size)

