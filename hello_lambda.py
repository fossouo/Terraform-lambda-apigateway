import json 
#{
#  "Name": "HeLium",
#  "Salaire": "0",
#  "fiscalite": {
#    "pacse": "false",
#    "maries": "true",
#    "nb_enfants": "4"
#  }
#}
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

def nb_part_fiscales(nb_enfants:int,maries:str,pacse:str):
    if(maries==True or pacse==True):
        if(nb_enfants<3):
            nb_part_fiscales = 2+nb_enfants*0.5
        else:
            nb_part_fiscales = 2+(nb_enfants-2)*1 + 1
    else:
        if(nb_enfants<3):
            nb_part_fiscales = 2+nb_enfants*0.5
        else:
            nb_part_fiscales = 2+(nb_enfants-2)*1 + 1
    return nb_part_fiscales

def handler(event, context):
    return { "message": "Hello, World!" }

def post_handler(event, context):
    
    myname = event["Name"]
    salaire = int(event["Salaire"])
    response_tmi = tmi_evaluator(salaire)
    pacse = str(event["fiscalite"]["pacse"])
    maries = str(event["fiscalite"]["maries"])
    nb_enfants = int(event["fiscalite"]["nb_enfants"])
    response_fiscale = nb_part_fiscales(nb_enfants,maries,pacse)
    return { "message": myname+' a une tmi de : '+str(response_tmi)+' . '+str(response_fiscale)+' parts' }
