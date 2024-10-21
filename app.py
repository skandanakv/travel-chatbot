# from flask import Flask, render_template, request, jsonify
# import random

# app = Flask(__name__)

# # Sample responses for the travel assistant
# responses = {
#     "greeting": [
#         "Hello! How can I assist you with your travel plans?",
#         "Hi there! Looking to plan a trip?"
#     ],
#     "destination_query": [
#         "Where would you like to go?",
#         "What is your dream destination?"
#     ],
#     "destinations": {
#         "paris": {
#             "suggestions": [
#                 "How about visiting the Eiffel Tower?",
#                 "You could take a Seine River cruise!",
#                 "Don't miss the Louvre Museum."
#             ],
#             "activities": [
#                 "Enjoy a day in Montmartre.",
#                 "Try authentic French cuisine at a local bistro."
#             ],
#             "weather": "The current weather in Paris is 18°C with light rain."
#         },
#         "bali": {
#             "suggestions": [
#                 "You could explore the beaches of Bali!",
#                 "How about a visit to Ubud's rice terraces?",
#                 "Don't forget to try snorkeling at Amed."
#             ],
#             "activities": [
#                 "Attend a traditional Balinese dance performance.",
#                 "Visit the Sacred Monkey Forest."
#             ],
#             "weather": "The current weather in Bali is 30°C and sunny."
#         },
#         "tokyo": {
#             "suggestions": [
#                 "Consider visiting the Tokyo Tower.",
#                 "Explore the bustling streets of Shibuya!",
#                 "Don't miss the cherry blossoms in spring."
#             ],
#             "activities": [
#                 "Experience the unique food scene in Tsukiji.",
#                 "Visit Akihabara for electronics and anime."
#             ],
#             "weather": "The current weather in Tokyo is 25°C with clear skies."
#         }
#     },
#     "farewell": [
#         "Safe travels! Let me know if you need anything else.",
#         "Happy travels! Feel free to ask if you have more questions."
#     ]
# }

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/ask", methods=["POST"])
# def ask():
#     user_input = request.form["user_input"].lower()
#     response = ""

#     # Greeting Response
#     if "hi" in user_input or "hello" in user_input:
#         response = random.choice(responses["greeting"]) + " " + random.choice(responses["destination_query"])

#     # Destination Query
#     elif any(destination in user_input for destination in responses["destinations"].keys()):
#         destination = next(dest for dest in responses["destinations"] if dest in user_input)
#         suggestions = responses["destinations"][destination]["suggestions"]
#         response = random.choice(suggestions) + " Would you like to know some activities to do there or the current weather?"

#     # Activities Inquiry
#     elif "activities" in user_input:
#         destination = next(dest for dest in responses["destinations"] if dest in user_input)
#         if destination:
#             activities = responses["destinations"][destination]["activities"]
#             response = random.choice(activities) if activities else "I don't have any specific activities listed."
#         else:
#             response = "Which destination are you asking about?"

#     # Weather Inquiry
#     elif "weather" in user_input:
#         destination = next(dest for dest in responses["destinations"] if dest in user_input)
#         if destination:
#             weather = responses["destinations"][destination]["weather"]
#             response = weather
#         else:
#             response = "Which destination's weather would you like to know?"

#     # Farewell Response
#     elif "bye" in user_input or "thank you" in user_input:
#         response = random.choice(responses["farewell"])

#     # General Response for unrecognized input
#     else:
#         response = "I'm sorry, I didn't understand that. Can you please rephrase?"

#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample responses for the travel assistant
responses = {
    "greeting": [
        "Hello! How can I assist you with your travel plans?",
        "Hi there! Looking to plan a trip?"
    ],
    "destination_query": [
        "Where would you like to go?",
        "What is your dream destination?"
    ],
    "destinations": {
        "paris": {
            "suggestions": [
                "How about visiting the Eiffel Tower?",
                "You could take a Seine River cruise!",
                "Don't miss the Louvre Museum."
            ],
            "activities": [
                "Enjoy a day in Montmartre.",
                "Try authentic French cuisine at a local bistro."
            ],
            "weather":[ "The current weather in Paris is 18°C with light rain."]
        },
        "bali": {
            "suggestions": [
                "You could explore the beaches of Bali!",
                "How about a visit to Ubud's rice terraces?",
                "Don't forget to try snorkeling at Amed."
            ],
            "activities": [
                "Attend a traditional Balinese dance performance.",
                "Visit the Sacred Monkey Forest."
            ],
            "weather": "The current weather in Bali is 30°C and sunny."
        },
        "tokyo": {
            "suggestions": [
                "Consider visiting the Tokyo Tower.",
                "Explore the bustling streets of Shibuya!",
                "Don't miss the cherry blossoms in spring."
            ],
            "activities": [
                "Experience the unique food scene in Tsukiji.",
                "Visit Akihabara for electronics and anime."
            ],
            "weather": "The current weather in Tokyo is 25°C with clear skies."
        }
    },
    "farewell": [
        "Safe travels! Let me know if you need anything else.",
        "Happy travels! Feel free to ask if you have more questions."
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form["user_input"].lower()
    response = ""
    current_destination = None

    # Check if there's a destination in the user input
    for destination in responses["destinations"].keys():
        if destination in user_input:
            current_destination = destination
            break

    # Greeting Response
    if "hi" in user_input or "hello" in user_input:
        response = random.choice(responses["greeting"]) + " " + random.choice(responses["destination_query"])

    # Destination Query
    elif current_destination:
        suggestions = responses["destinations"][current_destination]["suggestions"]
        response = random.choice(suggestions) + " Would you like to know some activities to do there or the current weather?"

    # Activities Inquiry
    elif "activities" in user_input:
        if current_destination:
            activities = responses["destinations"][current_destination]["activities"]
            response = random.choice(activities) if activities else "I don't have any specific activities listed."
        else:
            response = "Which destination are you asking about?"

    # Weather Inquiry
    elif "weather" in user_input:
        if current_destination:
            weather = responses["destinations"][current_destination]["weather"]
            response = weather
        else:
            response = "Which destination's weather would you like to know?"

    # Farewell Response
    elif "bye" in user_input or "thank you" in user_input:
        response = random.choice(responses["farewell"])

    # General Response for unrecognized input
    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)