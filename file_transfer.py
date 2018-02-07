#!/usr/bin/env python

from scp import SCPClient
from argparse import ArgumentParser
import paramiko

def connect_server(hostname, filename):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname)

        print ('Creating a paramiko transport for SCP...')

        # SCPCLient takes a paramiko transport and progress callback as its arguments.
        with SCPClient(ssh.get_transport()) as scp:
            print 'Putting the file "{}" in the remote_host: {}'.format(filename, hostname)
            scp.put(filename, '~/remote_test.py')

            # print 'Getting the file in the remote_host: %s', hostname
            # scp.get('~/remote_test.py')

    except Exception as e :
            print str(e)

def addparser(argv=None):
    parser = ArgumentParser(description='Transfer file using paramiko')
    parser.add_argument('-host', '--hostname', help = 'Enter the hostname', required = True)
    parser.add_argument('-file', '--filename', help = 'Enter the full path file to be transfered', required = True)
    return parser.parse_args()


if __name__ == "__main__":
    args = addparser()
    hostname = args.hostname
    filename = args.filename

    connect_server(hostname, filename)
