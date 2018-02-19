
try:
    with open("config.txt", "w") as file:

        print("Configuring ReactorBot!")
        lines = ['~ Specify users on a new line with format <username>~<emoji (do not include :: qualifiers) \n']

        while True:
            name = input("Type the name of the person to react to!")
            emoji = input("Type the name of the emoji to react with!")
            lines.append("{}~{}".format(name, emoji))

            if input("continue? y/n\n") is "n":
                break

        file.writelines(lines)

except FileNotFoundError:
    print("Config.txt not found, exiting.")