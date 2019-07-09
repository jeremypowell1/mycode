#! /usr/bin/python3

import warnings

import paramiko

# filter out any warnings with the word 'paramiko'

warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """ our runtime code that calls other functions """

    credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "fry", "ip": "10.10.2.4"}, {"un": "zoidberg", "ip": "10.10.2.5"}]

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey = mykey)

        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        print(sessout.read().decode('utf-8'))

        sshsession.close()

    print("Thanks for looping!")

main()

