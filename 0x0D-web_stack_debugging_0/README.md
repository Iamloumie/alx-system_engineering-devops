# Web Debugging Project

## 0-give_me_a_page

This script fixes and configures an Apache server to display "Hello Holberton" on the default page.

### Description

The script performs the following operations:

1. Updates the package lists using `apt-get update`
2. Installs Apache2 web server
3. Starts the Apache service
4. Creates an index.html file with "Hello Holberton" content
5. Restarts the Apache service to apply changes

### Script Content

```bash
#!/usr/bin/env bash
# fixing commands with bash
# make the apache server print Hello Holberton

sudo apt-get update -y
sudo apt-get install -y apache2
sudo /etc/init.d/apache2 start
echo "Hello Holberton" | sudo tee -a /var/www/html/index.html
sudo /etc/init.d/apache2 restart
```

### Requirements

- Ubuntu server
- Root/sudo privileges
- Bash shell

### Usage

1. Make the script executable:

```bash
chmod +x 0-give_me_a_page
```

2. Run the script:

```bash
./0-give_me_a_page
```

### Expected Result

After running the script, accessing the server through a web browser should display "Hello Holberton" on the default page.

### Troubleshooting

If the page doesn't display properly:

- Check if Apache is running: `sudo systemctl status apache2`
- Verify the content of index.html: `cat /var/www/html/index.html`
- Check Apache error logs: `sudo tail /var/log/apache2/error.log`
