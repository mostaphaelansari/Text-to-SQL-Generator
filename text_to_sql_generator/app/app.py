from text_to_sql_generator.src.models.dummy_model import DummyTextToSQLModel
import gradio as gr

# Instantiate dummy model
model = DummyTextToSQLModel()

# Create a custom chat interface using Blocks
with gr.Blocks(theme="soft") as chat_blocks:
    gr.Markdown("# Text-to-SQL Generator")
    gr.Markdown("Enter a natural language question and get SQL output")
    
    chatbot = gr.Chatbot(label="Conversation")
    msg = gr.Textbox(label="Your question", placeholder="Enter your question here...")
    
    def user_input(message, history):
        # Add user message to history
        history.append((message, ""))
        return "", history
    
    def bot_response(history):
        # Get last user message
        user_message = history[-1][0]
        
        # Generate SQL query
        sql_query = model.predict(user_message)
        
        # Update history with bot 
        if len(user_message) == 0 :
            yield "query is empety "
        else :
            history[-1] = (user_message, sql_query)
            return history
    
    msg.submit(
        user_input, 
        [msg, chatbot], 
        [msg, chatbot],
        queue=False
    ).then(
        bot_response,
        chatbot,
        chatbot
    )
    
    # Add example questions
    examples = gr.Examples(
        examples=["Show me all customers from New York", 
                 "What are the total sales for each product?", 
                 "List employees hired after 2020"],
        inputs=msg
    )

if __name__ == "__main__":
    chat_blocks.launch()
