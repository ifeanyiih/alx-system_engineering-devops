# Automate apache2 fix

exec { 'fix':
provider => shell,
command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}


