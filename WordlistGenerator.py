import itertools

def signature():
    signature = """
    __  _______  __
    \\ \\/ /   \\ \\/ /
     \\  / /| |\\  /
     / / ___ |/ /
    /_/_/  |_/_/
    """
    print(signature)

def create_wordlist(file_name, output_file_name):
    
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    combination_count = 0
    for r in range(2, len(lines) + 1):
        combination_count += len(list(itertools.permutations(lines, r)))
    
    print(f"A total of {combination_count} different combinations can be created.")
    
    answer = input("Do you want to create a wordlist? (Y/n): ").strip().lower()

    if answer == 'y':
        
        with open(output_file_name, 'w') as f:
            for r in range(2, len(lines) + 1):
                combinations = itertools.permutations(lines, r)
                for combination in combinations:
                    f.write(''.join(combination) + '\n')

        print(f"The new wordlist has been created as '{output_file_name}'.")
    else:
        print("Wordlist creation process has been canceled.")

signature()
file_name = input("Enter the name of the pre-prepared .txt file: ")
output_file_name = input("Output wordlist file name (e.g., new_wordlist.txt): ")
create_wordlist(file_name, output_file_name)
