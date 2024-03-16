import routeros_api
from ipaddress import IPv4Network

with open("webserver.txt", "r") as webserver:
    for server in webserver:
        server = server.strip()
webserver.close

with open("config.txt", "r") as configuration:
    for config in configuration:
        config = config.strip()
configuration.close

with open("username.txt", "r") as username:
    for user in username:
        user = user.strip()
username.close

with open("password.txt", "r") as password:
    for passw in password:
        passw = passw.strip()
password.close

with open("prefixes.txt", "r") as prefixes:
    for prefix in prefixes:
        prefix = prefix.strip()
        net = IPv4Network(prefix)
        hosts = net.hosts()
        for addr in hosts:
            try:
                connection = routeros_api.RouterOsApiPool(str(addr), username=user, password=passw, plaintext_login=True)
                api = connection.get_api()
                api.get_binary_resource('/').call('tool/fetch', {'url': server+config})
                api.get_binary_resource('/').call('import', {'file-name': config})
                connection.disconnect()
                print("successfully deployed configuration: " + str(addr))
            except:
                print("failed configuration deployment: " + str(addr))
prefixes.close