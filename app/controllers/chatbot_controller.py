from fastapi import APIRouter, HTTPException
from app.application.services import chatbot_service
from app.schemas.chatbot_schema import QuestionRequest, ResetInput


router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/chatbot/question", response_model=str)
async def ask_pregunta(payload: QuestionRequest):
    respuesta = chatbot_service.question_chatbot(payload.question)
    return respuesta
    return {"answer": respuesta["answer"]}



@router.post("/reset")
async def reset_conversation(reset_input: ResetInput):
    """
    Endpoint para resetear la conversación
    """
    try:
        chatbot_service.reset_conversation_history()
        return {"message": "Conversación reiniciada correctamente"}
    except Exception as e:
       raise HTTPException(
           status_code=500, detail=f"Error al resetear la conversación: {str(e)}"
       )
