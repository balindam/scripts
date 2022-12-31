This scripts performs the following actions,
- starts apache2 server
- starts mysql server

To use this script in linux systems, (You need to have root permissions to run the below steps) - 
1. Put _startup.sh_ inside your _/etc/init.d/_ directory.
- In terminal, type _`sudo mv -i <directory_where_the_file_was_downloaded>/startup.sh /etc/init.d/`_
2. Change the file permission to make it executible.
- In terminal type _`sudo chmod +x /etc/init.d/startup.sh`_