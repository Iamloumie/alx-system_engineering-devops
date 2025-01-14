# Server Configuration Scripts

This repository contains scripts for configuring and managing web servers, with a focus on Nginx installation and setup.

## Scripts Description

### 0-transfer_file

Transfers a file from a client to a server using secure copy protocol (SCP). The script ensures secure file transfer between systems.

### 1-install_nginx_web_server

Automates the installation and basic configuration of Nginx web server on an Ubuntu machine. The script:

- Updates package lists
- Installs Nginx
- Configures Nginx to listen on port 80
- Sets up a basic webpage

### 2-setup_a_domain_name

Configures DNS settings for a domain name to point to your server's IP address. This script helps in setting up proper domain name resolution.

### 3-redirection

Configures Nginx to perform URL redirection (301 Moved Permanently). This script helps in setting up proper HTTP redirects on your web server.

### 4-not_found_page_404

Creates and configures a custom 404 error page in Nginx. This script improves user experience by displaying a custom message when pages are not found.

### 7-puppet_install_nginx_web_server.pp

A Puppet manifest that automates the installation and configuration of Nginx using Infrastructure as Code principles. This script:

- Installs Nginx
- Configures the default settings
- Sets up basic web server functionality

## Requirements

- Ubuntu 16.04 LTS or higher
- Root access or sudo privileges
- Basic understanding of web server concepts
- Puppet (for the .pp manifest file)

## Usage

Each script can be executed with root privileges. For example:

```bash
sudo ./0-transfer_file file_name user_name server_ip /path/to/ssh/key
sudo ./1-install_nginx_web_server
```

For the Puppet manifest:

```bash
sudo puppet apply 7-puppet_install_nginx_web_server.pp
```
