import sys
import time
import httplib

mtucx = 1
dzx = 4

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

if sys.platform == 'win32':
	bcolors.disable()

print (bcolors.OKGREEN + '***************************************')
print (bcolors.OKGREEN + '* pyhthon filename.py www.target.com  *')
print (bcolors.OKGREEN + '***************************************')

BAD_RESP = [400,401,404]

def main(path):

    print "Scan:",host.split("/",1)[1]+path

    try:

        h = httplib.HTTP(host.split("/",1)[0])

        h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)

        h.putheader("Host", host.split("/",1)[0])

        h.endheaders()

        resp, reason, headers = h.getreply()

        return resp, reason, headers.get("Server")

    except(), msg:

        print "Error Occurred:",msg

        pass

def timer():

    now = time.localtime(time.time())

    return time.asctime(now)


dzx = { "wp-content/themes/linenity/functions/download.php?imgurl=1" : ["LFI WordPress Theme LineNity"], "career-details-2/?jobid=1" : ["SQl injection (Career2)"], "career-details/?jobid=" : ["SQl Injection (Career)"],"wp-content/themes/dandelion/" : ["www.exploit-db.com/exploits/31571/"],"wp-content/uploads/feuGT_uploads/feuGT_1790_43000000_948109840.php" : ["http://www.exploit-db.com/exploits/31570/"] , "wp-content/plugins/formcraft/form.php?id=1" : ["Wordpress formcraft Plugin Sql Injection"],"wp-content/themes/kernel-theme/functions/upload-handler.php" : ["http://www.exploit-db.com/exploits/29482/"], "wp-content/themes/saico/framework/_scripts/valums_uploader/php.php" : ["http://www.exploit-db.com/exploits/29150/"],"wp-content/themes/ThinkResponsive/includes/uploadify/upload_settings_image.php" : ["http://www.exploit-db.com/exploits/29332/"],"wp-content/themes/rockstar-theme/functions/upload-handler.php" :["http://www.exploit-db.com/exploits/29946/"],"wp-content/plugins/page-flip-image-gallery/upload.php" : ["http://www.exploit-db.com/exploits/30084/"],"wp-content/plugins/dzs-videogallery/deploy/designer/preview.php?swfloc=" : ["(dzs-videogallery) 3.1.3 Plugins Remote and LFD Vulnerability"],"wp-content/themes/area53/framework/_scripts/valums_uploader/php.php" : ["http://www.exploit-db.com/exploits/29068/"],"wp-content/plugins/wp-realty/index_ext.php?action=contact_friend&popup=yes&listing_id=1" : ["wp-realty - MySQL Time Based Injection"],"wp-content/plugins/lazy-seo/lazyseo.php" : ["Lazy SEO plugin Shell Upload Vulnerability"],"wp-content/plugins/complete-gallery-manager/frames/upload-images.php" : ["http://www.exploit-db.com/exploits/28377/"] , "wp-content/plugins/proplayer/playlist-controller.php?id=1" : ["ProPlayer Plugin SQL Injection"], "wp-content/themes/elegance/lib/scripts/dl-skin.php" : ["Wordpress Theme Elegance Arbitrary File Download Vulnerability"]}

if len(sys.argv) != 2:

    sys.exit(1)

host = sys.argv[1].replace("http://","").rsplit("/",1)[0]

if host[-1] != "/":

    host = host+"/"

print bcolors.HEADER + "\n [*] Target:",host

print bcolors.HEADER + "\n [*] Scanning Exploit\n"

print bcolors.FAIL

for xpl,(poc) in dzx.items():

    resp,reason,server = main(xpl)

    if resp not in BAD_RESP:

        print bcolors.WARNING + "\n [*] Result:",resp, reason
        print bcolors.OKGREEN + "\n [!] Vuln",poc

    else:

        print bcolors.FAIL + "\n [x] Result:",resp, reason
        print

print bcolors.OKGREEN + "[*] Finsihed Scanning"
