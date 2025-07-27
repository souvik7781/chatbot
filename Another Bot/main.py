def welcome_message():
  
    print("----------------------------------------------------")
    print("🌿 Welcome to the Ayurvedic Medicine Advisor Chatbot 🌿")
    print("----------------------------------------------------")
    print("I can suggest a general Ayurvedic herbal remedy based on your dosha and ailment.")
    print("Disclaimer: This is not medical advice. Please consult a qualified Ayurvedic doctor before taking any medicine.")
    print()

def get_dosha():
    doshas = {
        "1": "Vata",
        "2": "Pitta",
        "3": "Kapha"
    }
    print("Please select your dominant dosha:")
    for key, value in doshas.items():
        print(f"  {key}. {value}")

    while True:
        choice = input("Enter the number for your dosha (1-3): ")
        if choice in doshas:
            return doshas[choice]
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def get_roga(dosha):
    ailments = {
        "Vata": ["Joint Pain", "Constipation", "Anxiety"],
        "Pitta": ["Acidity", "Skin Rashes", "Indigestion"],
        "Kapha": ["Cough & Cold", "Congestion", "Weight Gain"]
    }

    print(f"\nWhat ailment are you experiencing? (Common for {dosha} dosha)")
    current_ailments = ailments[dosha]
    for i, ailment in enumerate(current_ailments, 1):
        print(f"  {i}. {ailment}")

    while True:
        try:
            choice = int(input(f"Enter the number for your ailment (1-{len(current_ailments)}): "))
            if 1 <= choice <= len(current_ailments):
                return current_ailments[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_suggestion(dosha, roga):
    """
    Returns an Ayurvedic suggestion based on the dosha and roga.
    This uses a nested dictionary to store the knowledge base.
    """
    suggestions = {
        "Vata": {
            "Joint Pain": "Consider taking Ashwagandha. It helps in reducing inflammation and strengthening joints.",
            "Constipation": "Triphala churna is highly effective. Take it with warm water before bed.",
            "Anxiety": "Brahmi is known to calm the nervous system and reduce anxiety."
        },
        "Pitta": {
            "Acidity": "Amalaki (Amla) is excellent for pacifying pitta and reducing acidity. You can take it as a powder or juice.",
            "Skin Rashes": "Neem has blood-purifying and anti-inflammatory properties that are great for skin issues.",
            "Indigestion": "Try Avipattikar churna. It helps in balancing digestive fire and relieving indigestion."
        },
        "Kapha": {
            "Cough & Cold": "Trikatu (a mix of ginger, black pepper, and long pepper) is effective. You can take it with honey.",
            "Congestion": "Sitopaladi churna is a classic remedy for clearing chest and nasal congestion.",
            "Weight Gain": "Guggulu is known to boost metabolism and aid in weight management."
        }
    }
    return suggestions.get(dosha, {}).get(roga, "No suggestion found for this combination.")

def ayurvedic_bot():
    """
    Main function to run the Ayurvedic chatbot.
    """
    welcome_message()
    user_dosha = get_dosha()
    user_roga = get_roga(user_dosha)
    suggestion = get_suggestion(user_dosha, user_roga)

    print("\n------------------ Your Suggestion ------------------")
    print(f"  Dominant Dosha: {user_dosha}")
    print(f"  Ailment: {user_roga}")
    print("\n  Suggestion:")
    print(f"  > {suggestion}")
    print("-----------------------------------------------------")
    print("\nThank you for using the chatbot. Stay healthy!")


if __name__ == "__main__":
    ayurvedic_bot()
