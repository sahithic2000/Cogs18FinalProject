import string
import random
import nltk

#lists of the inputs of the customer and the outputs that the bot returns
rice = ['white','brown','no rice']
beans = ['black','pinto','no beans']
protein = ['carne', 'asada','carnitas','chicken','sofritas', 'barbacoa','steak','veggie']
salsa = ['mild','medium','hot']
additional_toppings = ['cheese','fajita','veggies','corn','lettuce','sour','cream','and']
guac = ['guac','no guac']
bot_messages = ['What kind of rice would you like: white, brown, or no rice?',
                'What kind of beans would you like: black, pinto, or no beans?',
                'What kind of protein would you like: carne asada, carnitas, chicken, sofritas, barbacoa, steak, or veggie?',
                'What salsa would you like: mild, medium, hot, and/or no salsa?',
                'What additional toppings would you like: cheese, Fajita veggies, corn, lettuce, and/or sour cream?',
                'Would you like guacamole for an additional charge: guac or no guac?',"Type 'done' to process your order."]


#keeps track of the customer's input 
userSelection = ['','','','','','','']



def remove_punctuation(customer_input): 
    """
    NOTE: This function was taken directly from the chatbot assigment. 
    The function takes the customer's input which is a string and turns
    into a string without any puncutation.

    Parameters
    ----------
    customer_input: string 
      The customer's input is stored in customer_input.
       
       
    Returns
    -------
    output: string
       The customer input without any punctuation. 
    
    """"    

    out_string = ''
    for item in customer_input:
        if item not in string.punctuation:
            out_string += item
    return out_string

def prepare_text(customer_input):
    """
    NOTE:This function was taken directly from the chatbot assigment. 
    The function takes the customer's input which is a string and turns 
    into a list with all the words in the customer's input seperated. 

    Parameters
    ----------
    customer_input: string 
        The customer's input is stored in customer_input. 
       
       
    Returns
    -------
    output: list
       The customer input is seperated into a list of words. 
    
    """"    

    temp_string = customer_input.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list


def respond(customer_input):
    """
    This function checks if the customer input is a burrito and is in 
    any of the input lists displayed above. If the customer's input is 
    not in the list, then it notifies the customer. 

    Parameters
    ----------
    customer_input: string 
      The customer's input is stored in customer_input.
       
       
    Returns
    -------
    output: integer
       An integer is returned based on the list that the customer's input is in. 
    
    """"    
    #customer has to ask for a burrito 
    if 'burrito' in prepare_text(customer_input):
        userSelection[0]='burrito'
        return 0
    for item in prepare_text(customer_input):
        if item in rice:
            return 1
        elif item in beans:
            return 2
        elif item in protein:
            return 3
        elif item in salsa:
            return 4
        elif item in additional_toppings:
            return 5
        elif item in guac:
            return 6
    else:
        print("Sorry, I did not understand that. Please tell me again.")
        return -1


def outro(customer_input):
"""NOTE:This function was modified from the chatbot assigment. This function exits the chatbot when the customer is done ordering.

       Parameters
       ----------
       customer_input: string 
      
       The customer's input is stored in customer_input.
       
       
       Returns
       -------
       output: boolean
       
       Returns True/False based on if the customer is done ordering. """"    

    
    if 'done' in customer_input:
        return True
    else: 
        return False    
    
    
def payment():
"""This function prints how much the order will cost.

       Parameters
       ----------
       There are no parameters for this function.

       
       Returns
       -------
       output: None
       
       Other than printing the string prices, the function returns None because no explicit return statement exists """"    

    #assigns the 4th customer input, the meat choice, to meat_input
    meat_input = userSelection[3]
    #assigns the 7th customer input, the guac choice, to guac_input
    guac_input = userSelection[6]
    if guac_input == 'no guac':
        if 'chicken' in meat_input:
            print("The total is $7.95.")
        elif 'sofritas' in meat_input:
            print('The total is $7.95.')
        elif 'veggie' in meat_input:
            print('The total is $7.95')
        elif 'carnitas' in meat_input:
            print('The total is $8.45.')
        elif 'barbacoa' in meat_input:
            print('The total is $8.95.')
        elif 'steak' in meat_input:
            print('The total is $8.95.')
        elif 'carne asada' in meat_input:
            print('The total is $9.70.')
    else:
        if 'chicken' in meat_input:
            print("The total is $10.15.")
        elif 'sofritas' in meat_input:
            print('The total is $10.15.')
        elif 'veggie' in meat_input:
            print('The total is $10.15.')
        elif 'carnitas' in meat_input:
            print('The total is $10.65.')
        elif 'barbacoa' in meat_input:
            print('The total is $11.15.')
        elif 'steak' in meat_input:
            print('The total is $11.15.')
        elif 'carne asada' in meat_input:
            print('The total is $11.90.')
    
    
    
class Order:
    "Main class that executes the chatbot"
    
        order = True
        
        #variable that strores last message ID to redisplay in case customer inputs wrong input 
        lastMsg = 0
        
        #variable that keeps track of the customer's input
        nextMsg = 0
        
        #intro message 
        print("Hello, I'm Chip. How may I take your order?")
        
        while(order==True):
            
            #gets the customer's input
            order_input = input('CUSTOMER :')

            #when customer is done ordering, returns price and thank you message
            if outro(order_input):
                payment()
                print('CHIP:Thank you for ordering at Chipotle! Your order will be ready in a few minutes.')
                order = False
                
            #checks if customer's input is in the input lists     
            else:
                nextMsg = respond(order_input)
                
                # input is in the input lists, so it takes in the customer input
                if nextMsg>=0:
                    lastMsg=nextMsg
                    userSelection[nextMsg]=order_input
                    
                #it repeats the last message again if not in the input lists   
                else:
                    nextMsg=lastMsg
                    
                #prints the bot's message 
                print('CHIP:' + bot_messages[nextMsg])
                
        else:
            order = False


    
    