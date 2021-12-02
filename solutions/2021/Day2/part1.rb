input = File.open("input.txt")
lines = input.read.split("\n")

position = 0
depth = 0

lines.each { |l|
  line = l.split(" ")
  if line[0] == "forward"
    position += line[1].to_i
  elsif line[0] == "up"
    depth -= line[1].to_i
  elsif line[0] == "down"
    depth += line[1].to_i
  end
}

puts position * depth