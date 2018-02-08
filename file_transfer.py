#!/usr/bin/env python

from scp import SCPClient
from argparse import ArgumentParser
import paramiko

_port = 22

def connect_server(hostname, username, password, filename):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname, port=_port, username=username, password=password)

        print ('Creating a paramiko transport for SCP...')

        # SCPCLient takes a paramiko transport and progress callback as its arguments.
        with SCPClient(ssh.get_transport()) as scp:
            print 'Putting the file "{}" in the remote_host: {}'.format(filename, hostname)
            scp.put(filename, '~/remote_filename')

            # print 'Getting the file in the remote_host: %s', hostname
            # scp.get('~/remote_filename')

    except Exception as e :
            print str(e)

def addparser(argv=None):
    parser = ArgumentParser(description='Transfer file using paramiko')
    parser.add_argument('-host', '--hostname', help = 'Enter the hostname', required = True)
    parser.add_argument('-u', '--username', help = 'Enter the username for the host', required = True)
    parser.add_argument('-p', '--password', help = 'Enter the password for the host', required = True)
    parser.add_argument('-f', '--filename', help = 'Enter the full path of file to be transfered', required = True)
    return parser.parse_args()


if __name__ == "__main__":
    args = addparser()
    hostname = args.hostname
    username = args.username
    password = args.password
    filename = args.filename

    connect_server(hostname, username, password, filename)
