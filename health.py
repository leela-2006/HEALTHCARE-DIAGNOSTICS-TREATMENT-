def diagnose(symptoms):
    symptoms = [s.lower() for s in symptoms]
    if "fever" in symptoms and "cough" in symptoms and "fatigue" in symptoms:
        return "possible condition: Flu\nRecommended Treatment: Rest, stay hydrated, and paracetamol."
    elif"headache" in symptoms and"sensitivity to light" in symptoms:
        return "possible condition: migraine\nrecommendedtreatment: rest in a dark room,avoid triggers,and consider ibuprofen."
    elif"sore throat" in symptoms and"runnyy nose" in symptoms: 
        return "possible condition: common cold\nrecommended treatment:warm fluids,lozenges,rest."
    elif "chest pain" in symptoms and "shortness of breath" in symtoms:
        return "possible condition:heart problem\nrecommended action: seek emergency medical attention."
    else:
        return "condition unknown\nplease consult a healthcare provider for a detailed diagnosis."
def main():
    print("welcome to the health diagnostician!")
    user_input = input("Enter your symptoms separated by commas(e.g., fever, cough):")
    symptoms = user_input.split(',')
    diagnosis = diagnose(symptoms)
    print("\n" + diagnosis)

    
if__name__== "__main__":
    main()
    
