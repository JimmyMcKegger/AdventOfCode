defmodule Checksum do
  def part_one(file) do
    file
    |> make_rows
    |> check
  end

  def part_two(file) do
    file
    |> make_rows
    |> Enum.map(&find_div/1)
    |> List.flatten
    |> Enum.sum
  end

  def find_div(row) do
    for num <- row,
      other_num <- row,
      num != other_num,
      rem(num, other_num) == 0 do
        div(num, other_num)
     end
  end

  defp make_rows(file) do
    file
    |> File.read!
    |> String.split("\n")
    |> Enum.map(&map_to_ints/1)
  end

  defp map_to_ints(row) do
      row
      |> String.split
      |> Enum.map(fn x -> String.to_integer(x) end)
  end

  defp check(rows) do
    rows
    |> Enum.reduce(0, fn x, acc ->
      {min, max} = Enum.min_max(x)
      checksum = max - min
      checksum + acc
      end)
  end
end
