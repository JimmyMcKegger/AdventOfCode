defmodule CalorieCounting do
  def part1(file) do
    file
    |> split_elves
    |> Enum.map(&sum_elves/1)
    |> Enum.max
  end
  def part2(file) do
    file
    |> split_elves
    |> Enum.map(&sum_elves/1)
    |> Enum.sort
    |> Enum.take(-3)
    |> Enum.sum
  end
  defp split_elves(file) do
    file
    |> File.read!
    |> String.split("\n\n")
  end
  defp sum_elves(elf) do
   String.split(elf, "\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum
  end
end

p1 = CalorieCounting.part1 "input.txt"
p2 = CalorieCounting.part2 "input.txt"

IO.puts ~s/Part 1: #{p1}\nPart 2: #{p2}/
