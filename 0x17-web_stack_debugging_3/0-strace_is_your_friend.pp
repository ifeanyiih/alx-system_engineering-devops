# Automate apache2 fix

file { '/var/www/html/index.html':
ensure  => 'present',
content => 'Hello, World!'
}


