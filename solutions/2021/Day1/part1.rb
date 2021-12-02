#day 1, part 1

depths = File.open("input.txt")

depth_data = depths.read.split("\n")

counter = 0

i = 1

while i <=depth_data.length
  if depth_data[i].to_i > depth_data[i-1].to_i
    counter += 1
  end
  i+=1
end

puts counter



