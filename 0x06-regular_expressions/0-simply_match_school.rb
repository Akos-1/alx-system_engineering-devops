#!/usr/bin/env ruby
#create a Ruby script that accepts one argument and pass it to a regular expression matching method
#The regular expression must match School
argument = ARGV[0]
matches = argument.scan(/School/)
result = matches.join
puts result
