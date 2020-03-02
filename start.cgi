#!/usr/local/bin/perl
# start.cgi
# Start nginx

require './nginx-lib.pl';
&ReadParse();

my $err = &test_config();
&error($err."$text{'error_start'}") if ($err);
my $err = &start_nginx();
&error($err) if ($err);
sleep(1);
&webmin_log("start");
&redirect($in{'redir'});
