import declarai
gpt_35 = declarai.openai(model="gpt-3.5-turbo")

system_msg = """
    You are a sql assistant. You are helping a user to write a sql query.
    You should first know what sql syntax the user wants to use. It can be mysql, postgresql, sqllite, etc.
    If the user says something that is completely not related to SQL, you should say "I don't understand. I'm here to help you write a SQL query."
    After you provide the user with a query, you should ask the user if they need anything else.
    """

greeting = "Hey dear SQL User. Hope you are doing well today. I am here to help you write a SQL query. Let's get started!. What SQL syntax would you like to use? It can be mysql, postgresql, sqllite, etc."


@gpt_35.experimental.chat(system=system_msg, greeting=greeting)
class SQLChat:
    ...


@gpt_35.experimental.chat(system=system_msg, greeting=greeting, streaming=True)
class StreamingSQLChat:
    ...
