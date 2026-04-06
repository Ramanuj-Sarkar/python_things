#  Keep in mind that this requires that you have an OpenAI API key
# and that you have money in that account.

from openai import OpenAI

answer = input("This requires money. It will raise an error if no money is available.\n"
               "Enter 'Y' in order to proceed.")

if answer != 'Y':
    quit()

moneymaker = input("So do you have the money?")

client = OpenAI(
  api_key=moneymaker
)

messes = []
system_msg = input("What type of chatbot would you like to create?\n")
messes.append({"role": "system", "content": system_msg})

times = 0

print("Your new assistant is ready!\n"
      f"You can only ask {100 - times} or fewer questions.")

message = input()
while times < 100 and message != 'quit()':
    messes.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messes)
    reply = response.choices[0].message.content
    messes.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    times += 1
    message = input()
    if times == 100:
        print('Thank you for using this chatbot.\n'
              f'The {times} message limit has been reached.\n'
              'You can try again or change the "times" variable in the code.')
