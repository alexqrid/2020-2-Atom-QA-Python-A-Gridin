node "node1" {
    file { "/test":
       ensure => absent
    }

    class { "nginx":
      ensure => 'running',
      port => '8090'
    }

    class { "jenkins_slave":
        node => "node1",
        secret => "5c4b58252d817120637abd70214e15320e51d158893db446d01f96a7b652321f"
    }

}

node "node2" {
    file { "/test1":
       ensure => absent
    }

    class { "nginx":
        ensure => 'running',
        port => '9090'
    }

    class { "jenkins_slave":
        node => "node2",
        secret => "26ae7391f3e88acec775b190671a656d08959d437743b0a9e024db1e461ad6b2"
    }

}


node "node3" {
    class { "jenkins_slave":
        node => "node3",
        secret => "353b6b43e04c864a60d05b4d72603213e6ab04a7205258574b1d40744a711a38"
    }

}