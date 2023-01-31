#!/usr/bin/env ruby
#Script matches a regular expression
puts ARGV[0].scan(/^hb.*n$/).join
