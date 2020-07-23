import napalm
import json
from pprint import pprint
from getpass import getpass

my_juniper = {
    'hostname': '172.16.83.150',
    'username': 'vireak',
    'password': getpass(),
    'optional_args':{
        'port': 22
        },
    }
    
driver = napalm.get_network_driver('junos')
with driver(**my_juniper) as device:
    # with open('napalm/PNHPNH-IX-CRT03-get_facts.json', 'w') as json_file:
    #     pprint(device.get_facts())
    #     json.dump(device.get_facts(), json_file, indent=4)
    #     # pprint(device.get_ntp_peers())
    #     # pprint(device.get_ntp_servers())
    # with open('napalm/PNHPNH-IX-CRT03-get_environment.json', 'w') as json_file:
    #     # pprint(device.get_environment())
    #     json.dump(device.get_environment(), json_file, indent=4)
        # pprint(device.get_bgp_neighbors())
    commands = ['show interfaces terse | grep up','show version']
    output = device.cli(commands)
    print(output['show interfaces terse | grep up'])
    print(output['show version'])

