class nginx::repo {

    file { "/etc/yum.repos.d/nginx.repo":
      ensure => file,
      source => 'puppet:///modules/nginx/nginx.repo',
      notify => Exec["clean yum"]
    }

    exec { "clean yum":
      command => "/usr/bin/yum clean all",
      subscribe => File["/etc/yum.repos.d/nginx.repo"]
    }

}