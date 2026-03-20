class monitoring {

  # Ensure Nagios config directory exists
  file { '/etc/nagios':
    ensure => directory,
  }

  # Deploy services configuration
  file { '/etc/nagios/services.cfg':
    ensure  => file,
    source  => 'puppet:///modules/monitoring/services.cfg',
    owner   => 'nagios',
    group   => 'nagios',
    mode    => '0644',
  }

}