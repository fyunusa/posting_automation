import os
import subprocess
import sys


def email_copier(
    file_source: list,
    root_source: str,
    root_dest: str
):

    # root_source = '/home/hallvrqh/mail/'
    # root_dest = '/home/hallvrqh/public_html/email_copier'

    isExist = os.path.exists(root_dest)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(root_dest)    

    email_accts = [acct.split("@")[0] for acct in file_source]
    email_domain = file_source[0].split("@")[1]

    for itm in os.listdir(root_source + email_domain):
        if itm in email_accts and os.path.isdir(os.path.join(root_source+email_domain,itm)):
            print(itm)
            isExist = os.path.exists("{0}/{1}_emailextrct".format(root_dest,itm))
            if not isExist:
                # Create a new directory because it does not exist 
                os.makedirs("{0}/{1}_emailextrct".format(root_dest,itm))

            src_new = '{0}{1}/{2}/new'.format(root_source,email_domain,itm)
            src_cur = '{0}{1}/{2}/cur'.format(root_source,email_domain,itm)
            src_maildir = '{0}{1}/{2}/maildirsize'.format(root_source,email_domain,itm)

            dst_ = '{0}/{1}_emailextrct/'.format(root_dest,itm)

            cmd = 'scp -r {0} {1}'.format(src_new, dst_)
            cmd2 = 'scp -r {0} {1}'.format(src_cur, dst_)
            cmd2 = 'scp {0} {1}'.format(src_maildir, dst_)
            # Executing the command by calling the subprocess.call()
            try:
                status = subprocess.call([cmd, src_new, dst_], shell=True)
                status = subprocess.call([cmd2, src_cur, dst_], shell=True)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    root_source = int(input("Input root source: \n 1.) /home/hallvrqh/mail/ \n 2.) /home/meedconsulting/mail/ \n"))
    root_dest = int(input("Input root destination: \n 1.) /home/hallvrqh/public_html/email_copier \n 2.) /home/meedconsulting/public_html/email_copier \n"))

    if root_source == 1:
        root_source = '/home/hallvrqh/mail/'
    elif root_source == 2:
        root_source = '/home/meedconsulting/mail/'
    else:
        print("Invalid input for root destination")
        sys.exit()

    if root_dest == 1:
        root_dest = '/home/hallvrqh/public_html/email_copier'
    elif root_dest == 2:
        root_dest = '/home/meedconsulting/public_html/email_copier'
    else:
        print("Invalid input for root destination")
        sys.exit()

    emails_data = input("Input the emails to get as a comma seperated value:\n e.g abdulmajid@passolutions.net,accounts@passolutions.net \n")
    # emails_data = "abdulmajid@passolutions.net,accounts@passolutions.net,dayo@passolutions.net,director@passolutions.net,hafiz@passolutions.net,ibrahim@passolutions.net,info@passolutions.net,nurses@passolutions.net,process@passolutions.net,promax@passolutions.net ,saheed@passolutions.net,secretary@passolutions.net"
    email_list = emails_data.split(",")
    email_copier(email_list, root_source, root_dest)


            
