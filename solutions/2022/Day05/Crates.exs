defmodule Crates do
  def part1(file) do
    {stacks, moves} = init(file)

    Enum.reduce(moves, stacks, fn x, acc ->
      play({acc, x}, 9000)
    end)
    |> tops
  end

  def part2(file) do
    {stacks, moves} = init(file)

    Enum.reduce(moves, stacks, fn x, acc ->
      play({acc, x}, 9001)
    end)
    |> tops
  end

  def tops(input) do
    input
    |> Map.values()
    |> Enum.map(&hd/1)
    |> Enum.reduce("", fn x, acc -> acc <> x end)
  end

  def play({stacks, moves}, model) do
    [num, from, to] = moves
    start_from = Map.fetch!(stacks, from)
    {to_add_to, new_from} = Enum.split(start_from, num)

    start_to = Map.fetch!(stacks, to)
    to_add_to = reverse?(to_add_to, model)
    new_to = [to_add_to | start_to] |> List.flatten

    # update to and from stacks
    Map.put(stacks, from, new_from) |> Map.put(to, new_to)
  end

  def init(f) do
    [crates, moves] = File.read!(f) |> String.split("\n\n")

    supply_stack = zip_build(crates)

    moves =
      String.split(moves, "\n")
      |> Enum.map(fn line ->
        Regex.scan(~r/\d+/, line)
        |> List.flatten()
        |> Enum.map(fn n -> String.to_integer(n) end)
      end)

    {supply_stack, moves}
  end

  defp zip_build(stack) do
      String.split(stack, "\n")
      |> Enum.map(fn str -> String.to_charlist(str) end)
      |> Enum.drop(-1)
      |> Enum.map(fn chrs -> Enum.chunk_every(chrs, 3, 4) end)
      |> Enum.zip
      |> Enum.map(fn t ->
        Tuple.to_list(t)
        |> Enum.reject(fn x -> x == '   ' end)
        |> Enum.map(fn x ->
          str = List.to_string(x)
          hd(Regex.run(~r/\w/, str))
        end)
      end)
      |> map_maker
  end

  defp map_maker([a, b, c]), do: %{1 => a, 2 => b, 3 => c}
  defp map_maker([a, b, c, d, e, f, g, h, i]), do: %{1 => a, 2 => b, 3 => c, 4 => d, 5 => e, 6 => f, 7 => g, 8 => h, 9 => i}

  defp reverse?(c, 9000), do: Enum.reverse(c)
  defp reverse?(c, 9001), do: c

end

p1 = Crates.part1("input.txt")
p2 = Crates.part2("input.txt")

IO.puts(~s/Part 1: #{p1}\nPart 2: #{p2}/)
