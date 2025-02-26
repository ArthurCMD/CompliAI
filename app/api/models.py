from pydantic import BaseModel, Field
from typing import List

class InputChat(BaseModel):
    SystemMessage: str | None = Field(default=None, examples=["Responde de forma educada"])
    HumamMessage: str = Field(examples=["Quem é o presidente do Brasil?"])
    
class ResponseChat(BaseModel):
    AiMessage: str = Field(examples=["Presidente do brasil é o Lula"])

class ChunkObj(BaseModel):
    chunks_id: int
    id_vector: str
    md5: str
    conteudo: str
        
class DocumentoObj(BaseModel):
    documento_id: int
    titulo: str
    descricao: str
    md5: str
    url: str | None
    chunks: List[ChunkObj]

class SessaoObj(BaseModel):
    session_id: int
    titulo: str
    criado: str
    
class InputDocumentoApi(BaseModel):
    titulo: str | None
    description: str
    url: str | None

class HistoricoObj(BaseModel):
    chathistory_id: int
    session_id: int
    mensagem: str
    tipo: int
    
class InputUser(BaseModel):
    username: str
    password: str
    
class InputUsername(BaseModel):
    username: str