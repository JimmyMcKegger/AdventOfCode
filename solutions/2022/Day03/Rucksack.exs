defmodule Rucksack do
  @moduledoc """
  Solution for Advent of Code 2022 day 3.
  """

  @spec part1(String.t()) :: integer
  def part1(file) do
    compartments(file)
    |> Enum.reduce(0, fn x, acc ->
      {str1, str2} = x
      myers = String.myers_difference(str1, str2)
      match = Keyword.get(myers, :eq)

      acc + prioritize(match)
    end)
  end

  @spec part2(String.t()) :: integer
  def part2(file) do
    threes(file)
    |> Enum.reduce(0, fn x, acc ->
      [a, b, c] = x
      base_string = String.split(a, "", trim: true)

      results =
        Enum.filter(base_string, fn x ->
          {:ok, my_pattern} = Regex.compile(x)
          Regex.match?(my_pattern, b) and Regex.match?(my_pattern, c)
        end)

      acc + prioritize(hd(results))
    end)
  end

  defp prioritize(char) do
    if char =~ ~r/[a-z]/ do
      <<num>> = char
      num - 96
    else
      <<num>> = char
      num - 38
    end
  end

  defp compartments(f) do
    File.read!(f)
    |> String.split("\n")
    |> Enum.map(fn line ->
      String.split_at(line, div(String.length(line), 2))
    end)
  end

  defp threes(f) do
    File.read!(f)
    |> String.split("\n")
    |> Enum.chunk_every(3)
  end
end

p1 = Rucksack.part1("input.txt")
p2 = Rucksack.part2("input.txt")

IO.puts(~s/Part 1: #{p1}\nPart 2: #{p2}/)
