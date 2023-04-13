
print('''Welcome to Madlibs! ''')
print('''Madlibs is a fun game where you get to create a story by filling in the blanks with different parts of speech.''')

print('''To get started, you will be prompted to enter various words such as nouns, verbs, adjectives, and more. 
Once you have entered all the necessary words, 
Madlibs will use them to create a unique and often hilarious story that you can read and share with others.
To interact with Madlibs, you can use the command line. 
Simply run the Madlibs program and follow the prompts to enter the different parts of speech. 
After you have entered all the required words, Madlibs will generate a story and print it to the screen.

Have fun playing Madlibs!''')

input_str = input("Do you want to play Madlibs? (y/n): ")

if input_str == 'y':
    # adjective1 = input("Give us an adjective: ")
    # adjective2 = input("Give us another adjective: ")
    # name = input("Give us your name: ")
    file_path =("assets/vedio_game.txt")
    def read_template(file_path):
        with open (file_path , 'r') as file:
            content = file.read()
            return content

    def parse_template(template_txt):
        parts = []
        stripped = ""
        index = 0

        while index < len(template_txt):
            if template_txt[index] == "{":
                end_index = template_txt.find("}", index)
                parts.append(template_txt[index + 1 : end_index])
                stripped += "{}"
                index = end_index + 1
            else:
                stripped += template_txt[index]
                index += 1

        return stripped, tuple(parts)

    def merge(template, words):
        return template.format(*words)

    template_txt = read_template(file_path)
    stripped, parts = parse_template(template_txt)

    words = []
    for elment in parts:
        user_input = input(f" write {elment} here : ")
        words.append(user_input)
    
    story = merge(stripped, words)

    print(story)

    with open('madlib_cli/madlib_story.txt', 'w') as file:
        file.write(story)

    print(' Game is done :) ')
    print("Goodbye!")

elif input_str == 'n':
    print("Goodbye!")
else:
    print("Invalid input. Please try again.")

    

