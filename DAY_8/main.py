from ascii_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(direction , text , shift):
        
        if direction == "decode":
            shift *= -1
        output_text = ""
        for char in text:
            if char not in alphabet:
                 output_text += char
            elif char in alphabet:
                char_index = alphabet.index(char)
                char_index += shift
                indexed_letter = alphabet[char_index % len(alphabet)]
                output_text += indexed_letter
        print(f"Here is your {direction}d text, {output_text}")

should_continue = True

while should_continue != False:
      direction = input("Type \'encode' to encrypt, \'decode' to decypt.\n").lower()
      text = input("Type your message.\n").lower()
      shift = int(input("Type your shift number.\n"))

      caesar(direction , text , shift)

      restart = input("Type \'yes' if you want to go again, otherwise type \'no'.\n").lower()

      if restart == "no":
           should_continue = False
           print("GOODBYE!")