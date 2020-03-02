#!/usr/local/bin/perl
# reload.cgi
# reload nginx config file or restart nginx

require './nginx-lib.pl';
&ReadParse();

my $err = &test_config();
&error($err."$text{'error_reload'}") if ($err);
my $err = &reload_nginx();
&error($err) if ($err);
sleep(1);
&webmin_log("apply");
&redirect($in{'redir'});
