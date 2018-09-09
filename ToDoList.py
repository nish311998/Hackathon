import speech_recogntion as sr

arraydata = []

def add(storage):
    response = input("Would you like to write or say something for me to add to your to do list")

    while True:
        while True:
    
            if(response == "write" || response  == "Write"):
                add = input("Please type what you want to be added to your to do list")
                break
        

            elif(response == "say" || response == "Say"):
                #Say what you want me to add to your to do list
                break

            else:
                response = input("I did not catch that. Would you like to write or say something for me to add to your to do list")
        arraydata.append(add)

        
add(arraydata)


    
