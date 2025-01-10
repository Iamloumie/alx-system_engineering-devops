# Using Puppet, create a file in /tmp.

file {'/tmp/school':
ensure  => file,
path    => '/tmp/school',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
mode    => '0744',
}
