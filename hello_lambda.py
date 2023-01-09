import json 

def tmi_evaluator(salaire:int):
    if(salaire < 10226):
        tmi = 0
    elif(salaire > 10226 and salaire < 26070):
        tmi = 11
    elif(salaire > 26070 and salaire < 74546):
        tmi = 30
    elif(salaire > 74546 and salaire < 160336):
        tmi = 41
    else:
        tmi = 45
    return tmi

def handler(event, context):
    return { "message": "Hello, World!" }

def post_handler(event, context):
    
    myname = event["Name"]
    salaire = int(event["Salaire"])
    response = tmi_evaluator(salaire)
    return { "message": myname+' a une tmi de : '+str(response) }
