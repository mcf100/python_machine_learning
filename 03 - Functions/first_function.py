def ask_user_status():
    response = input("How are you?: ").lower()

    if response == "ok":
        print("Excellent!")
    else:
        print("Oh no.")

ask_user_status()
