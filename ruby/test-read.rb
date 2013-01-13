require 'edn'

edn_content = File.read(ARGV[0])

puts edn_content

edn_data = EDN.read(edn_content)

puts edn_data