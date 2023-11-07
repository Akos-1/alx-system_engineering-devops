#!/usr/bin/env bash
## Installs Nginx with puppet with the following configurations:
#Returns a page containing "Hello World!" when queried  at the root with a curl GET request.
#Configures /redirect_me as a "301 Moved Permanently".
#a custom 404 page containing "Ceci n'est pas une page". is included
#the HTTP header's value is the hostname of the running server.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html index.htm;
      location /redirect_me {
        return 301 https//youtube.com/;
      }
      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
      }
    }
  ',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
