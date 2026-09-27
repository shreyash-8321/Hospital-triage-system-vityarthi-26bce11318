import json

# load patients from the json file
def load_patients():
    try:
        f = open('patient_records.json', 'r')
        data = json.load(f)
        f.close()
        return data
    except:
        return {}

#saves patient info
def save_patients( dic ):
    out = open("patient_records.json", 'w')
    json.dump(dic, out, indent=4)
    out.close()

#find suggested meds
def load_meds():
    file = open( "medicine_data.json" , 'r')
    return json.load(file)