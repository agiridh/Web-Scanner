import os

# nmap scans a server to see what processes are running and what ports are open
# print get_nmap('-F', '216.58.197.46')
# google nmap for more nmap flags. -F is does a fast scan
def get_nmap(options, ip):
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command) # starts another process. (like typing a new command on terminal)
    results = str(process.read())
    return results
