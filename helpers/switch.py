from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
import os

secrets = os.getenv('cisco_secrets')

class switch:
    def __init__(self,switch_loopback_addr):
        self.switch_loopback_addr = switch_loopback_addr
        self.info = self.get_information()
    
    def get_information(self):
        device = {
            "device_type": "cisco_xr",
            "host": self.switch_loopback_addr,
            "username": 'admin',
            "password": secrets,
        }
        # Show command that we execute.
        commands = [
            "sh run",
        ]
        result = ""
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                for command in commands:
                    output = ssh.send_command(command)
                    result += output
            return str(result)
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
            return False