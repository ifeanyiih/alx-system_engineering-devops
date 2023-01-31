#!/usr/bin/env ruby
#Script contains the regular expression that will match a case(s)
puts ARGV[0].scan(/hbt{2,5}n/).join
