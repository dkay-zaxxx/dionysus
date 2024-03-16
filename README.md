# Mass Deploy MikroTik Configuration - Dionysus

Yes! This works on both RouterOSv6 and RouterOSv7

Rather than applying a configuration individually, and wasting precious time :) automate your configuration deployments with this simple tool. Along side with this software, you will need a place to centrally host your configuration file (contains the config you would like to deploy across your devices) that the MikroTik will import, generally either a local webserver on your local LAN segment or a publically available webserver (This is risky, so I do advise allowing access to the configuration file from your network only or use some random string prepended to the configration file to prevent indexing like - `IBHfda82odfafnda-ntp.auto.rsc`). I've generally used an apache basic webserver with the configuration files left `/var/www/html/` directory (by default I've left it as `file.auto.rsc`) - Its really up to you and how you would like to host the configuration - Just note that this tool downloads the configuration using HTTP only.


# Installing The Requirements

`apt install python2.7`

`curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py`

`python2.7 get-pip.py`

`pip2.7 install RouterOS-Api`

`pip2.7 install ip-address==1.4.2`

`pip2.7 install ipaddress`

`pip install py2-ipaddress`


# RouterOS Requirements

Make sure that the RouterOS API service is enabled, you can enable by pasting in the following command:

RouterOSv6 - `/ip service enable api`

RouterOSv7 - `/ip/service/enable api`

Also your router needs to be able to route directly to the webserver, to download the configuration file.


# Getting Everything Ready

Your first step should be to populate the following files, you would be working mostly on the prefix and config text files: 

`prefixes.txt` - Use the CIDR address scheme of the group of routers you want to config, you are able to add another prefix on the next line - Take note that network and broadcast addresses are excluded.

`username.txt` - Enter the username that will be globally used.

`password.txt` - Enter the password that will be globally used.

`webserver.txt` - Enter the URL of your webserver, make sure to follow this scheme `http://{ip}/`.

`config.txt` - Enter the name of the file saved on the webserver, as your MikroTik will be performing a cURL request to `http://{ip}/file.auto.rsc` by default I've been using the name `file.auto.rsc` but you most likely want to prevent indexing of your configuration if its publically available.


# Running Your First Job

Once all of the above has been completed, you may easily execute the bash script in your terminal by running:

`python2.7 main.py`

Finally! the script will initiate and command the Python RouterOS API to log into each device and deploy your configuration, if you do enjoy the purpose and easy of use, please share with others to help everyone save some precious time :)


# Reaching Out

If you have any issues, questions or would like to contribute to this project, feel free to contact by opening an issue request or emailing `darshan@darshankowlaser.com`
