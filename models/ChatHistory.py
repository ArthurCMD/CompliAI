import peewee
import os

db = peewee.SqliteDatabase('example.db')

if "POSTGRES_HOST" in os.environ:
    db = peewee.PostgresqlDatabase(os.environ['POSTGRES_DATASE'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'])
    

class ChatHistory(peewee.Model):
    """
    Classe que representa o historico das mensagens
    """
    chathistory_id = peewee.AutoField(primary_key=True)
    session_id = peewee.IntegerField()
    mensagem = peewee.CharField()
    tipo = peewee.IntegerField(constraints=[peewee.Check('tipo in (0,1,2)')]) # 0 = SystemMessage / 1 = HumamMessage / 2 = AiMessage
    class Meta:
        database = db