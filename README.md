 ->Cognitive Routing & RAG Project

 Overview

This project implements a simple system where different bots respond to a post based on their personality. It first selects relevant bots, then generates content, and finally handles replies using conversation context.

 ->Approach

The system is divided into three parts:

1. Routing: Bot personas are converted into embeddings and matched with incoming posts using FAISS to select relevant bots.
2. Content Generation: A LangGraph workflow decides a topic, fetches mock context, and generates a short post in JSON format.
3. Reply System: The bot uses full conversation context to generate replies and ignores any attempt to override its behavior.

=> Tech Stack

Python, LangGraph, FAISS, Sentence Transformers

-> Conclusion

This project demonstrates how routing, workflow-based generation, and context-aware responses can be combined to build a basic AI system.

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

