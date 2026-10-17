#  Keep in mind that this requires that you have an OpenAI API key
# and that you have money in that account.

from openai import OpenAI

answer = input("This requires money. It will raise an error if no money is available.\n"
               "Enter 'Y' in order to proceed.")

if answer != 'Y':
    quit()

moneymaker = input("If you have the money, give me the key:")

client = OpenAI(
  api_key=moneymaker
)

messes = []
system_msg = input("What type of chatbot would you like to create?\n")
messes.append({"role": "system", "content": system_msg})

TIMES = 0
MAXIMUM = 100

print("Your new assistant is ready!\n"
      f"You can only ask {MAXIMUM - TIMES} or fewer questions.")

message = input()
while message != 'quit()':
    messes.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messes)
    reply = response.choices[0].message.content
    messes.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    TIMES += 1
    if TIMES == MAXIMUM:
        print('Thank you for using this chatbot.\n'
              f'The {TIMES} message limit has been reached.\n'
              'You can start this again or change the TIMES and MAXIMUM variables in the code.')
        break
    message = input()
