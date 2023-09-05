#!/usr/bin/env ruby
input_string = ARGV[0]
uppercase_string = input_string.scan(/[A-Z]+/).join
puts uppercase_string
