class nginx($ensure='stopped', $port='8080') {

  class { "nginx::config":
      port => $port
  } ->

  class { "nginx::repo": }

  pkg { "nginx":
    require  => File["/etc/yum.repos.d/nginx.repo"]
  }

  service { "nginx":
    ensure  => $ensure,
    start   => '/usr/sbin/nginx -c /tmp/nginx.conf',
    stop    => '/usr/sbin/nginx -s stop',
    require => Package["nginx"],
    subscribe => File["/tmp/nginx.conf"]
  }
}