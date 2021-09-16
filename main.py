from meetGenerator import Generator
from meetGenerator import Color


generator = Generator()
my_username = """
   ____  _ _                  _ 
  / __ \| (_)                | |
 | |  | | |___   _____ _ __  | |
 | |  | | | \ \ / / _ \ '__| | |
 | |__| | | |\ V /  __/ |    |_|
  \____/|_|_| \_/ \___|_|    (_)
"""
print(Color.BOLD + Color.WARNING + my_username + Color.END_C)
print(Color.BOLD + Color.OK_CYAN + "\nWelcome to my Stupid program!,\n"
                   "ENTER HOW MANY RANDOM GOOGLE MEET CLASSES YOU WANT TO GENERATE" +
      Color.END_C + "\n")

while True:
    try:
        times = int(input(Color.BOLD + "Times: " + Color.END_C))
        break
    except ValueError:
        print("Number, not a string or something else :D")

print(Color.BOLD + Color.OK_GREEN + "\nRESULT: " + Color.END_C)
print(generator.generate(times))



