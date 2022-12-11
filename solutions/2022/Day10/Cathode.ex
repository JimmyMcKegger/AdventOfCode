defmodule Cathode do
  
  def solve(f) do
    f
    |> File.read!
    |> String.split("\n")
    |> Enum.reduce({1, 1, 0, ""}, &cycle(&1, &2))
    |> IO.inspect(label: "part one")
    |> pixel_print
  end

  def cycle(line, {i, x, signal_sum, pixel_string}) do
    signal_sum = signal_sum + ss_finder(i, x)

    pixel_string = pixel_string <> pixelator(i, x)

    continue =
      if line == "noop" do
        {i + 1, x, signal_sum, pixel_string}
      else
        n_to_add =
          line
          |> String.split()
          |> List.last()
          |> String.to_integer()

        signal_sum = signal_sum + ss_finder(i + 1, x)
        pixel_string = pixel_string <> pixelator(i + 1, x)

        {i + 2, x + n_to_add, signal_sum, pixel_string}
      end

    continue
  end

  def pixel_print({_i, _x, _signal_sum, pixel_string}) do
    for <<char::binary-40 <- pixel_string>>, do: char
  end

  def pixelator(i, x) do
    sprite = x-1..x+1

    if rem(i,40) - 1 in sprite do
      "#"
    else
      "."
    end
  end

  def ss_finder(20, x), do: 20 * x
  def ss_finder(60, x), do: 60 * x
  def ss_finder(100, x), do: 100 * x
  def ss_finder(140, x), do: 140 * x
  def ss_finder(180, x), do: 180 * x
  def ss_finder(220, x), do: 220 * x
  def ss_finder(_, _), do: 0
end
