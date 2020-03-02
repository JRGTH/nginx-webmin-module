#!/usr/local/bin/perl
# details.cgi
# Display list of nginx details

require './nginx-lib.pl';
&ReadParse();

&ui_print_header($title, "$text{'index_details'}", "");

while ( my ($key, $value) = each(%nginfo) ) {
	print "$key => $value<br>";
}

&ui_print_footer("$return", "nginx index");
