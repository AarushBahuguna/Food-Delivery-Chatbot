
import json
from gemini_service import GeminiService
from config import FOOD_MENU

class FoodRecommender:
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    def get_recommendations_for_user(self, user_preference_query: str):
        menu_for_prompt = []
        for item_id, details in FOOD_MENU.items():
            tags = ", ".join(details.get('tags', []))
            menu_for_prompt.append(f"ID: {item_id}, Name: {details['name']}, Price: {details['price']:.2f}, Tags: [{tags}]")
        
        menu_as_string = "\n".join(menu_for_prompt)


        prompt = (
            f"You are an intelligent food ordering assistant. A customer said: '{user_preference_query}'.\n"
            f"Analyze their request. Your goal is to fulfill it completely.\n"
            f"If they ask you to create a cart, find the best combination of items from the menu below that fits their criteria (like budget, cuisine, health preferences).\n\n"
            f"MENU:\n{menu_as_string}\n\n"
            f"Based on the user's request, decide on an action. Respond ONLY with a JSON object in the following format:\n"
            f'{{"action": "add_to_cart", "items_to_add": ["item_id_1", "item_id_2", ...], "reasoning": "A brief explanation of your choices."}}\n'
            f"If you are only recommending, use action 'recommend' and put your text in 'reasoning'.\n"
            f"If you cannot fulfill the request, use action 'cannot_fulfill' and explain why in 'reasoning'."
        )


        
        try:
            response_text = self.gemini_service.generate_response(prompt)
            cleaned_response = response_text.strip().replace("```json", "").replace("```", "")
            return json.loads(cleaned_response)
        except (json.JSONDecodeError, TypeError):
            return {"action": "recommend", "reasoning": "I can suggest some items for you: Salad Bowl, Biryani, and Momos are great options!"}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"action": "cannot_fulfill", "reasoning": "I'm having a bit of trouble thinking right now. Could you try asking in a simpler way?"}

    def get_recommendations_for_item(self, item_name: str) -> str:
        menu_as_string = "\n".join([f"- {item['name']}" for item in FOOD_MENU.values()])
        
        prompt = (f"A customer just added '{item_name}' to their cart. "
                  f"Based on the following menu, what are 2-3 other items (like sides, drinks, or desserts) that would pair well with it? "
                  f"Keep the suggestions brief and enticing.\n\n"
                  f"Here is the menu:\n{menu_as_string}")

        try:
            recommendations = self.gemini_service.generate_response(prompt)
            if recommendations and "sorry" not in recommendations.lower():
                return recommendations
            return ""
        except Exception:
            return ""