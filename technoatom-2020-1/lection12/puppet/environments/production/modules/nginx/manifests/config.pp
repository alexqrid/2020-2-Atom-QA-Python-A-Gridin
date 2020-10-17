class nginx::config($port='8080') {

  file { "/tmp/nginx.conf":
    ensure => file,
    content => template("nginx/nginx.conf.erb"),
    notify => Service["nginx"]
  }

}