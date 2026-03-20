class monitoring_config {

  file { '/etc/nagios/services.cfg':
    ensure  => file,
    source  => 'puppet:///modules/monitoring/services.cfg',
    owner   => 'nagios',
    group   => 'nagios',
    mode    => '0644',
  }

}