def mod_power():
    base = int(input("Enter the base number : "))
    exp = int(input("Enter exponent value : "))
    no_mod = int(input("Enter the number to do mod operation : "))

    return (base**exp) % no_mod


print(mod_power())
