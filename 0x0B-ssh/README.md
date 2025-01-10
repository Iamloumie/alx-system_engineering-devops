# SSH Configuration Project

This project contains files and scripts for configuring and managing SSH keys and configurations, as well as an example Puppet manifest for SSH setup.

## Files Description

### 0-use_a_private_key

A script or configuration for using a private SSH key to authenticate. Ensure you have the corresponding private key to access remote servers.

### 1-create_ssh_key_pair

A script or guide to create an SSH key pair. Run this script to generate a public/private key pair for secure authentication.

### 2-ssh_config

An SSH configuration file that contains custom settings for your SSH client. This file can include configurations like host aliases, user settings, and key paths.

### school

A file that could represent a host or system information. Check its content for specific usage.

### school.pub

The public SSH key file. This key can be shared with remote systems to enable passwordless login.

### 100-puppet_ssh_config.pp

A Puppet manifest for configuring SSH settings programmatically. Use this to automate SSH configuration deployment.

## Usage

1. **Set Up an SSH Key Pair**:
   Run the `1-create_ssh_key_pair` script to generate a new SSH key pair.

2. **Configure SSH Client**:
   Use the `2-ssh_config` file to customize your SSH client settings. Update the file with your preferred configurations.

3. **Use the Private Key**:
   Use the `0-use_a_private_key` script to authenticate using your private key. Ensure the private key file is correctly secured.

4. **Deploy Configuration with Puppet**:
   Apply the `100-puppet_ssh_config.pp` manifest to set up SSH configurations automatically on your systems.

## Notes

- Keep your private keys secure. Do not share or expose them to unauthorized users.
- Ensure the `school.pub` key is added to the `~/.ssh/authorized_keys` file on the target server for passwordless login.
- Validate the `2-ssh_config` file syntax by running `ssh -T` to check for errors.

## Requirements

- SSH client and server installed.
- Puppet (for `100-puppet_ssh_config.pp` usage).
