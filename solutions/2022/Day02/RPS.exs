defmodule RPS do
  @elf %{"A" => :rock, "B" => :paper, "C" => :scissors}
  @player %{"X" => :rock, "Y" => :paper, "Z" => :scissors}
  @shape_value %{rock: 1, paper: 2, scissors: 3}

  def part1(file) do
    file
    |> readlines
    |> Enum.reduce(0, fn round, acc ->
      [choice, guess] = round
      acc + @shape_value[@player[guess]] + score(@elf[choice], @player[guess])
    end)
  end

  def part2(file) do
    file
    |> readlines
    |> Enum.reduce(0, fn round, acc ->
      [choice, strategy] = round
      my_pick = find_my_pick(@elf[choice], strategy)
      acc + @shape_value[my_pick] + score(@elf[choice], my_pick)
    end)
  end

  defp readlines(file) do
    file
    |> File.read!()
    |> String.split("\n")
    |> Enum.map(fn row ->
      String.split(row, " ")
    end)
  end

  defp find_my_pick(ec, "Y"), do: ec
  defp find_my_pick(ec, "X") when ec == :rock, do: :scissors
  defp find_my_pick(ec, "X") when ec == :paper, do: :rock
  defp find_my_pick(ec, "X") when ec == :scissors, do: :paper
  defp find_my_pick(ec, "Z") when ec == :rock, do: :paper
  defp find_my_pick(ec, "Z") when ec == :paper, do: :scissors
  defp find_my_pick(ec, "Z") when ec == :scissors, do: :rock

  defp score(opp, pl) when opp == pl, do: 3
  defp score(:rock, :paper), do: 6
  defp score(:rock, :scissors), do: 0
  defp score(:paper, :rock), do: 0
  defp score(:paper, :scissors), do: 6
  defp score(:scissors, :rock), do: 6
  defp score(:scissors, :paper), do: 0
end

p1 = RPS.part1 "input.txt"
p2 = RPS.part2 "input.txt"

IO.puts ~s/Part 1: #{p1}\nPart 2: #{p2}/
