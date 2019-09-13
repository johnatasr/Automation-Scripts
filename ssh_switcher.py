from netmiko import ConnectHandler

iosv_12 = {
    'device_type':'cisco',
    'ip': '192.168.122.15',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
output - net_connect.sed_comnnad('show ip in brief')
print (output)

config_commnads = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output =net_connect.send_config_set(config_commands)
print(output)

for n in range(2,21)>
print("Criando VLAN" + str(n))
config_commands = ['vlan '+str(n)m 'python_vlan' +str(n)]
output = net_connect.sed_confgi_set(config_commands)
print()output