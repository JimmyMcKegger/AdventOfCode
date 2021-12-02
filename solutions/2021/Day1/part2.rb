

example = File.open("example.txt")
example_data = example.read.split("\n").map(&:to_i)

depths = File.open("input.txt")
depth_data = depths.read.split("\n").map(&:to_i)

window = []

i = 0

while i < depth_data.length-2
  sum = depth_data[i] + depth_data[i+1] + depth_data[i+2]
  window.push(sum)
  i+=1
end

counter = 0

j = 1

while j <=window.length
  if window[j].to_i > window[j-1].to_i
    counter += 1
  end
  j+=1
end

puts counter