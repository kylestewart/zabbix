import mailMonitorClass

mail = mailMonitorClass.mailMonitor()

mailboxes = mail.find_mailboxes()

print(mailboxes)

