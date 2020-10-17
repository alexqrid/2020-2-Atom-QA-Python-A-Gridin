define pkg ($version = undef) {
  $base_versions = lookup('versions', Data, 'hash')
  if ($version) {
    $ensure = $version
  }
  else {
    $ensure = $base_versions[$name]
  }

  package { $name :
      provider => yum,
      ensure => $ensure,
  }
}
