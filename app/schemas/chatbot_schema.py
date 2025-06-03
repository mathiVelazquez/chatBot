from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    
    
class AnswerResponse(BaseModel):
    answer: str
    
class ResetInput(BaseModel):
    reset: bool = True