defmodule Tuning do
  @moduledoc """
  Solution for Advent of Code 2022 day 6.
  """

  def part1(file),
    do:
      file
      |> tune
      |> find_frequency

  def part2(file),
    do:
      file
      |> tune
      |> find_message

  def find_message({_chars, len}, n) when len < n + 14, do: nil
  def find_message({chars, len}, n \\ 0) do
    set = Enum.slice(chars, n, 14)

    if Enum.count(Enum.uniq(set)) == 14 do
      n + 14
    else
      find_message({chars, len}, n + 1)
    end
  end

  def find_frequency({_chars, len}, n) when len < n + 4, do: nil
  def find_frequency({chars, len}, n \\ 0) do
    set = Enum.slice(chars, n, 4)

    if Enum.count(Enum.uniq(set)) == 4 do
      n + 4
    else
      find_frequency({chars, len}, n + 1)
    end
  end

  defp tune(f) do
    chrs =
      File.read!(f)
      |> to_charlist

    {chrs, Enum.count(chrs)}
  end
end
