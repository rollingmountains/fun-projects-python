def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


def mad_libs():
    print("Welcome to Mad Libs game!")
    noun = get_input("noun")
    adjective = get_input("adjective")
    verb = get_input("verb")
    
    
    story = f"{noun} is a {adjective} man. He loves to {verb} all day long."
    
    print(story)
    
mad_libs()