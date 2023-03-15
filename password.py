def password():
    password = input("Choose a password ")
    
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    spe = ["&", "#", "@", "+", "=", "-", "_", "$", "¤", "£", "€"]
    min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    if len(password) >= 8 : 
        for lettre in password:
            for chiffre in num:
                if lettre == chiffre:
                    for lettre in password:
                        for minimum in min:
                            if lettre == minimum:
                                for lettre in password:
                                    for punctuation in spe:
                                        if lettre == punctuation:
                                            for lettre in password:
                                                for maximum in maj:
                                                    if lettre == maximum:
                                                        print("Password saved")
                                                        return True

    print("Restart and change your password ")
    return False
        
password()