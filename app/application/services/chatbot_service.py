from app.schemas.chatbot_schema import QuestionRequest, AnswerResponse

def post_chatbot_message(message: str) -> str:
    #response = get_response_by_question(message)
    return "Post Realizado"


def question_chatbot(message: str) -> str:
    return f"La pregunta realizada es: {message}"
    return {"answer": f"La pregunta realizada es: {message}"}