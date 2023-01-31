#!/usr/bin/env ruby
#Script matches a regular expression
print ARGV[0].scan(/from:([^\]]*\b)/).join
print ','
print ARGV[0].scan(/to:([^\]]*\b)/).join
print ','
print ARGV[0].scan(/flags:([^\]]*\b)/).join
puts
