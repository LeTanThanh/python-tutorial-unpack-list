if __name__ == "__main__":
  # Introduction to the list unpacking

  colors = ["red", "green", "blue"]

  red = colors[0]
  green = colors[1]
  blue = colors[2]
  print(red, green, blue)

  red, green, blue = colors
  print(red, green, blue)

  # red, green = colors
  # ValueError

  # Unpacking and packing

  colors = ["red", "green", "blue"]
  red, green, *other = colors
  print(red)
  print(green)
  print(other)

  colors = ["cyan", "magenta", "yellow", "black"]
  cyan, magenta, *other = colors
  print(cyan)
  print(magenta)
  print(other)
