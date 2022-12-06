defmodule Cleanup do
  @moduledoc """
  Solution for Advent of Code 2022 day 4.
  """

  def part1(file) do
    file
    |> sections
    |> count_fully_overlapping
  end

  def part2(file) do
    file
    |> sections
    |> count_any_overlapping
  end

  # transform the start and end coordinates into 2 ranges
  defp count_fully_overlapping(lines) do
    Enum.reduce(lines, 0, fn l, acc ->
      {{a, b, c, d}, {r1, r2}} = l

      if (Enum.member?(r1, c) and Enum.member?(r1, d)) or
           (Enum.member?(r2, a) and Enum.member?(r2, b)) do
        acc + 1
      else
        acc
      end
    end)
  end

  defp count_any_overlapping(lines) do
    Enum.reduce(lines, 0, fn l, acc ->
      {{a, b, c, d}, {r1, r2}} = l

      if Enum.member?(r1, c) or Enum.member?(r1, d) or
           (Enum.member?(r2, a) or Enum.member?(r2, b)) do
        acc + 1
      else
        acc
      end
    end)
  end

  # take file name, return a list of start/end numbers
  defp sections(f) do
    File.read!(f)
    |> String.split("\n")
    |> Enum.map(fn line ->
      Regex.scan(~r/\d+/, line)
      |> List.flatten()
      |> Enum.map(fn c -> String.to_integer(c) end)
      |> to_range
    end)
  end

  defp to_range(line) do
    [a, b, c, d] = line

    {{a, b, c, d}, {Range.new(a, b), Range.new(c, d)}}
  end
end

p1 = Cleanup.part1("input.txt")
p2 = Cleanup.part2("input.txt")

IO.puts(~s/Part 1: #{p1}\nPart 2: #{p2}/)
