# fix Too many files open error to enable nginx recieve 2000 request, 100 at a time

exec { 'fix':
provider => shell,
command  => 'sudo sed -i "s/ULIMIT.*/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'restart':
provider => shell,
command  => 'sudo service nginx restart'
}


