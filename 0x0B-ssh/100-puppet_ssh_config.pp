# practice using Puppet to make changes to our configuration file
$str = "# ssh config by IHI
IdentityFile=~/.ssh/school
IdentitiesOnly=yes"

file { 'config':
    ensure  => present,
    path    => '/home/vagrant/.ssh/config',
    content => $str
}
