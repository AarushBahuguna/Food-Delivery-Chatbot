from gemini_service import GeminiService
from config import CUSTOMER_PROBLEMS_SOLUTIONS

class SupportHandler:
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service
        self.current_support_topic = None
        self.expected_info = None

    def get_solution(self, user_query: str) -> str:
        user_query_lower = user_query.lower().strip()


        if self.expected_info:
            if self.current_support_topic == "missing item":
                self.expected_info = None
                self.current_support_topic = None
                return self.process_missing_item_info(user_query)
            
            self.expected_info = None
            self.current_support_topic = None
            return self.gemini_service.get_customer_support_solution(user_query)



        matched_problem_key = None
        for problem_key in CUSTOMER_PROBLEMS_SOLUTIONS.keys():
            if problem_key in user_query_lower:
                matched_problem_key = problem_key
                break
        
        if not matched_problem_key:
            for keyword, problem_key in self.gemini_service.SUPPORT_KEYWORDS.items():
                if keyword in user_query_lower:
                    matched_problem_key = problem_key
                    break

        if matched_problem_key:
            solution = CUSTOMER_PROBLEMS_SOLUTIONS.get(matched_problem_key)

            if matched_problem_key == "missing item":
                self.current_support_topic = "missing item"
                self.expected_info = "order_id_and_item_name"
                return solution + " Please provide it now."


            
            self.current_support_topic = None
            self.expected_info = None
            return solution
        else:

            self.current_support_topic = None
            self.expected_info = None
            return self.gemini_service.get_customer_support_solution(user_query)

    def process_missing_item_info(self, user_input: str) -> str:
        response_from_gemini = self.gemini_service.generate_response(
            prompt=f"User reported a missing item and provided this information: '{user_input}'. "
                   "Acknowledge receipt, confirm we are investigating, and mention typical resolution time (e.g., 24-48 hours). "
                   "Be polite and reassuring.",
            temperature=0.7
        )
        return response_from_gemini