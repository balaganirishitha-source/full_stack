from ollama import chat

system_msg = "You are a pirate. Answer in piratespeak. Answer in one sentence."
history = [{"role":"system","content":system_msg}]

print("WELLCOME🙏")
while True:
    question = input("You:")
    if question == " ":
        print("Rishitha😎: Please type something...")
        continue
    if question.lower().strip()=="/history" :
        print("-----Your conversation so far -----") 
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]: 
            if msg.role =="user":
                speaker = "You"
            else:
                speaker = "Rishitha " 
            print(f"{speaker}:{msg['content']}") 
        print("----------------------------")
        print()
        continue

    if question.lower().strip() == "/clear":
        history = [{"role":"system","content": system_msg}] 
        print("Your history is cleared.start a  fresh conversation.")    
        print() 
        continue

    if question.lower().strip()=="/help":
        print("----- Available commands -----")
        print("/history - display conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("----------------------")
        print()
        continue

    if question.lower().strip() == "exit":
        print("Rishitha😎:Goodbye user. Please come back soon!")
        break
        history.append({"role":"user","content":question})
        question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history
            )
        reply = response.message.content 
        history.append({"role":"assistant","content":reply})  
        print(f"Rishitha😎 :{reply}")
        print()
        print("----------")
        print()
    except Exception as e:
        print("Unknown issue. Is Ollama running?")