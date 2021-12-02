input = File.open("input.txt")
lines = input.read.split("\n")

position = 0
depth = 0
aim = 0

lines.each { |l|
  line = l.split(" ")
  if line[0] == "forward"
    position += line[1].to_i
    depth += (aim * line[1].to_i)
  elsif line[0] == "up"
    aim -= line[1].to_i
  elsif line[0] == "down"
    aim += line[1].to_i
  end
}

puts position * depth