#!/usr/bin/env ruby
#create a Ruby script that accepts one argument and pass it to a regular expression matching method
#The regular expression must match School
argument = ARGV[0]
if argument =~ /School/
  puts "The argument contains the word 'School'"
else
  puts "The argument does not contain the word 'School'"
end
