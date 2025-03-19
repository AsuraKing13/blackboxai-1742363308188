import random

class SarawakTourismChatbot:
    def __init__(self):
        self.clusters = {
            "Homestays": [
                "Explore the beautiful homestays in the heart of Sarawak.",
                "Experience the local culture by staying with a host family."
            ],
            "Food & Beverages": [
                "Try the famous Sarawak Laksa and Kolo Mee.",
                "Don't miss out on the local delicacies at the food markets."
            ],
            "Fashion": [
                "Discover traditional Sarawakian attire and modern fashion.",
                "Visit local boutiques for unique fashion pieces."
            ],
            "Traditional Crafts": [
                "Learn about the intricate beadwork and weaving techniques.",
                "Support local artisans by purchasing handmade crafts."
            ],
            "Heritage Attractions": [
                "Visit the Sarawak Cultural Village to learn about local heritage.",
                "Explore historical sites like Fort Margherita."
            ],
            "Performing Arts": [
                "Enjoy traditional dance performances at local festivals.",
                "Attend cultural shows showcasing Sarawak's rich heritage."
            ]
        }

    def get_recommendation(self, cluster):
        if cluster in self.clusters:
            return random.choice(self.clusters[cluster])
        else:
            return "I'm sorry, I don't have information on that topic."

    def chat(self):
        print("Welcome to the Sarawak Tourism Chatbot!")
        while True:
            user_input = input("Ask me about tourism in Sarawak (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Thank you for chatting! Have a great day!")
                break
            response = self.get_recommendation(user_input)
            print(response)

if __name__ == "__main__":
    chatbot = SarawakTourismChatbot()
    chatbot.chat()