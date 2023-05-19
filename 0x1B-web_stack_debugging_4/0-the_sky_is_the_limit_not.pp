# Automate apache2 fix

exec { 'fix':
provider => shell,
command  => 'sed -i "s/ULIMIT.*/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'restart':
provider => shell,
command  => 'service nginx restart'
}


