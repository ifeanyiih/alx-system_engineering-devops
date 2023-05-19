# fix Too many files open error to enable nginx recieve 2000 request, 100 at a time

exec { 'increase ULIMIT':
command => 'sudo sed -i "s/ULIMIT.*/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
path    => 'usr/local/bin/:bin/'
}

exec {'restart nginx':
command => 'sudo service nginx restart',
path    => '/etc/init.d/'
}


