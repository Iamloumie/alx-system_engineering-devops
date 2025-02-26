# fix error line (to find out why Apache is returning a 500 error)

exec {'replace':
  path    => ['/bin','/usr/bin'],
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
