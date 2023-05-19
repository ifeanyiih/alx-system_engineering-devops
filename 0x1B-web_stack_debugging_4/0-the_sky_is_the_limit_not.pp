# Automate apache2 fix

exec { 'fix':
provider => shell,
command  => 'sed -i "s/15/4096/g" /etc/default/nginx'
}

exec {'restart':
provider => shell,
command  => 'service nginx restart'
}


