for i in range(5):
    print(f"Starting loop number {i}")
    
    stop = input("Stop the loop (y/n) ?")
    if stop == "y":
        continue
    
    print(f"Ending loop number {i}")

print("Program finished")