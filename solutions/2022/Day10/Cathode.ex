defmodule Cathode do
  # part 1
  def part1(f) do
    File.read!(f)
    |> String.split("\n")
    |> Enum.reduce({1, 1, 0}, &cycle(&1, &2))
  end

  def cycle(line, {i, x, signal_sum}) do
    signal_sum = signal_sum + ss_finder(i, x)

    continue =
      if line == "noop" do
        {i + 1, x, signal_sum}
      else
        n_to_add =
          line
          |> String.split()
          |> List.last()
          |> String.to_integer()

        signal_sum = signal_sum + ss_finder(i + 1, x)

        {i + 2, x + n_to_add, signal_sum}
      end

    continue
  end

  def ss_finder(20, x), do: 20 * x
  def ss_finder(60, x), do: 60 * x
  def ss_finder(100, x), do: 100 * x
  def ss_finder(140, x), do: 140 * x
  def ss_finder(180, x), do: 180 * x
  def ss_finder(220, x), do: 220 * x
  def ss_finder(_, _), do: 0
end
