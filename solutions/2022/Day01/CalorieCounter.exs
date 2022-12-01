defmodule CalorieCounting do

  @spec part1(String.t) :: integer
  def part1(file) do
    file
    |> split_elves
    |> Enum.map(&sum_elves/1)
    |> Enum.max
  end

  @spec part2(String.t) :: integer
  def part2(file) do
    file
    |> split_elves
    |> Enum.map(&sum_elves/1)
    |> Enum.sort
    |> Enum.take(-3)
    |> Enum.sum
  end

  @spec split_elves(String.t) :: [String.t]
  defp split_elves(file) do
    file
    |> File.read!
    |> String.split("\n\n")
  end

  @spec sum_elves(String.t) :: integer
  defp sum_elves(elf) do
   String.split(elf, "\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum
  end

end

p1 = CalorieCounting.part1 "input.txt"
p2 = CalorieCounting.part2 "input.txt"

IO.puts ~s/Part 1: #{p1}\nPart 2: #{p2}/
