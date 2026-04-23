from transformers import pipeline
import re

# Load model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

intent_labels = [
    "Navigation",
    "Climate Control",
    "Media",
    "Communication",
    "Vehicle Control"
]

def extract_entities(command):
    entities = {}

    # Destination
    location_match = re.search(r"to (.+)", command.lower())
    if location_match:
        entities["destination"] = location_match.group(1)

    # Temperature
    temp_match = re.search(r"(\d{2})", command)
    if temp_match:
        entities["temperature"] = temp_match.group(1)

    # Contact
    call_match = re.search(r"call (.+)", command.lower())
    if call_match:
        entities["contact"] = call_match.group(1)

    return entities

def map_action(intent, entities):
    if intent == "Navigation":
        return f"Start navigation to {entities.get('destination', 'unknown location')}"
    elif intent == "Climate Control":
        return f"Set temperature to {entities.get('temperature', 'default')}°C"
    elif intent == "Media":
        return "Playing requested media"
    elif intent == "Communication":
        return f"Calling {entities.get('contact', 'unknown')}"
    else:
        return "Executing vehicle command"

def process_command(command):
    result = classifier(command, intent_labels)
    intent = result['labels'][0]
    confidence = round(result['scores'][0] * 100, 1)

    entities = extract_entities(command)
    action = map_action(intent, entities)

    return {
        "command": command,
        "intent": intent,
        "confidence": confidence,
        "entities": entities,
        "action": action
    }


# CLI test
if __name__ == "__main__":
    while True:
        cmd = input("Enter command: ")
        output = process_command(cmd)

        print("\nIntent:", output["intent"])
        print("Confidence:", output["confidence"])
        print("Entities:", output["entities"])
        print("Action:", output["action"])
        print("-" * 40)
