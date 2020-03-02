#!/usr/local/bin/perl
# create_server.cgi
# Create a new virtual host.

require './nginx-lib.pl';
&ReadParseMime();

my $dir = "$config{'virt_dir'}";
my $link_dir = "$config{'link_dir'}";
my $file = "$dir/$in{'newserver'}";
if (-e $file) {
	&error("$text{'error_fileexist'} $in{'newserver'}");
}

&lock_file($file);
$temp = &transname();
&copy_source_dest($file, $temp);
$in{'directives'} =~ s/\r//g;
$in{'directives'} =~ s/\s+$//;
@dirs = split(/\n/, $in{'directives'});
$lref = &read_file_lines($file);
if (!defined($start)) {
	$start = 0;
	$end = @$lref - 1;
}
splice(@$lref, $start, $end-$start+1, @dirs);
&flush_file_lines();

my $err = &test_config();
&error($err."$text{'error_conferror'}") if ($err);

unlink($temp);
&unlock_file($file);
&webmin_log("create", "nginx_server", $file, \%in);

if ($link_dir) {
	# create vhost symlink
	&create_webfile_link($file);

	if ($config{'jail_enable'} == 1) {
		my $lfile = &backquote_command("/bin/ls $link_dir/$in{'newserver'} 2>/dev/null");
		if (!$lfile) {
			&error("$text{'error_linkerr'}");
		}
	} else {
		if (!-e "$link_dir/$in{'newserver'}") {
			&error("$text{'error_linkerr'}");
		}
	}
}

&redirect("");
