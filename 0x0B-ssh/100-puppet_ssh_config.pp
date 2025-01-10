#!/usr/bin/env bash
# Configure ssh client to use specific private key and
# disable password authentication

file { '/etc/ssh/ssh_config':
ensure  => 'present',
}

# Add IdentityFile configuration
file_line { 'Declare identity file':
path    => '/etc/ssh/ssh_config',
line    => 'IdentityFile ~/.ssh/school',
match   => '^#?\s*IdentityFile\s+~/.ssh/school$',
ensure  => 'present',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
path    => '/etc/ssh/ssh_config',
line    => 'PasswordAuthentication no',
match   => '^#?\s*PasswordAuthentication\s+(yes|no)$',
}
