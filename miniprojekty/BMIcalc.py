def get_user_input():
    """
    Prompts the user to enter their height and weight and returns the corresponding values.

    Returns:
        float: The height entered by the user.
        float: The weight entered by the user.
    """
    while True:
        try:
            wzrost = float(input("Podaj wzrost w metrach: ").replace(',', '.'))
            break
        except ValueError:
            print("Proszę podać prawidłową liczbę dla wzrostu.")

    while True:
        try:
            waga = float(input("Podaj wagę w kilogramach: ").replace(',', '.'))
            break
        except ValueError:
            print("Proszę podać prawidłową liczbę dla wagi.")
            
    return wzrost, waga

def bmi(wzrost, waga):
    """
    Calculates the BMI based on the height and weight provided.

    Args:
        wzrost (float): The height of the user in meters.
        waga (float): The weight of the user in kilograms.

    Returns:
        float: The calculated BMI.
    """
    return waga / wzrost ** 2

def interpretacja(bmi):
    """
    Interprets the BMI value and prints the corresponding message.

    Args:
        bmi (float): The calculated BMI.
    """
    if bmi < 16:
        print("Wygłodzenie")
    elif 16 <= bmi < 17:
        print("Wychudzenie")
    elif 17 <= bmi < 18.5:
        print("Niedowaga")
    elif 18.5 <= bmi < 25:
        print("Waga prawidłowa")
    elif 25 <= bmi < 30:
        print("Nadwaga")
    elif 30 <= bmi < 35:
        print("Otyłość I stopnia")
    elif 35 <= bmi < 40:
        print("Otyłość II stopnia")
    else:
        print("Otyłość III stopnia")

def good_range(wzrost):
    """
    Shows the range of kilograms for a given height that is considered healthy.

    Args:
        wzrost (float): The height of the user in meters.

    Returns:
        float: The lower bound of the healthy weight range.
        float: The upper bound of the healthy weight range.
    """
    print("Waga w granicach zdrowia to od", 18.5 * wzrost ** 2, "do", 25 * wzrost ** 2)

def main():
    """
    Main function that calls the input, bmi, and interpretacja functions.
    """
    wzrost, waga = get_user_input()
    bmi_value = bmi(wzrost, waga)
    interpretacja(bmi_value)
    good_range(wzrost)

main()