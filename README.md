LangGraph Design

For content generation, I used a simple 3-step workflow using LangGraph. First, the system decides a topic, then it fetches some related context using a mock search function, and finally it generates a post based on the bot’s personality and that context. The flow is sequential (decide → search → generate), which keeps the logic easy to follow and modify.

Prompt Injection Defense

To handle prompt injection, I added clear rules inside the prompt so the bot does not change its behavior. It is instructed to stick to its persona and ignore any attempts to override instructions. I also pass the full conversation (parent post, previous replies, and user input) so the response stays consistent and grounded in context.

-> Architecture Diagram

        user post
            |
            |
            +    
 Sentence Transformer(Embedding Model )
            |
            |
            +
        FAISS Vector DB 
        (Bot Personas)
            |
            |
            +
    Routing(Select Relevant Bots)
            |
            |
            +
     __________________________   
    |                          │
 Bot A                     Bot B                   
     |                         |
     |                         |
     +   LangGraph Workflow    +
     |                         |                     
     |   1.Decide Topic        |                           
     |   2.Mock Search(Context)|                        
     |   3.Generate JSONoutput |              
     +           |             +
                 |
                 +
           Generated Posts                                      
                  |
                  |
                  +
         RAG Reply System
                  |
                  |
                  +
            Bot Response

