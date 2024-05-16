# системи самодіагностування стану людини в умовах надзвичайних ситуацій

def main():
    
    print ("Welcome to Nastya's self-diagnosis app")
    print("Answer the following questions to get a basic diagnosis.")

    symptoms = {}

    # Collecting symptoms
    symptoms['chest_pain'] = input("Do you have chest pain? (yes/no): ").strip().lower() == 'yes'
    symptoms['breathing_difficulty'] = input("Do you have difficulty breathing? (yes/no): ").strip().lower() == 'yes'
    symptoms['bleeding'] = input("Are you experiencing severe bleeding? (yes/no): ").strip().lower() == 'yes'
    symptoms['unconscious'] = input("Is the person unconscious? (yes/no): ").strip().lower() == 'yes'
    symptoms['severe_headache'] = input("Are you experiencing a severe headache? (yes/no): ").strip().lower() == 'yes'
    symptoms['fever'] = input("Do you have a high fever? (yes/no): ").strip().lower() == 'yes'
    symptoms['rash'] = input("Do you have a rash? (yes/no): ").strip().lower() == 'yes'
    symptoms['vomiting'] = input("Are you vomiting? (yes/no): ").strip().lower() == 'yes'
    symptoms['confusion'] = input("Are you feeling confused or disoriented? (yes/no): ").strip().lower() == 'yes'

    # Basic Diagnosis
    if symptoms['chest_pain'] and symptoms['breathing_difficulty']:
        print("\nYou may be experiencing a heart attack. Call emergency services immediately!")
    elif symptoms['unconscious']:
        print("\nThe person is unconscious. Call emergency services immediately!")
    elif symptoms['bleeding']:
        print("\nSevere bleeding detected. Apply pressure to the wound and call emergency services immediately!")
    elif symptoms['severe_headache'] and symptoms['confusion']:
        print("\nYou may be experiencing a stroke or another serious condition. Call emergency services immediately!")
    elif symptoms['fever'] and symptoms['rash']:
        print("\nYou may have an infectious disease. Seek medical attention as soon as possible.")
    elif symptoms['vomiting']:
        print("\nPersistent vomiting can lead to dehydration. Seek medical advice.")
    else:
        print("\nYour symptoms do not match any critical conditions we check for.")
        print("If you are feeling unwell, please consult a healthcare professional for further advice.")
    
    print("\nStay safe and take care.")

if __name__ == "__main__":
    main()
