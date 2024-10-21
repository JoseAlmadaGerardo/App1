# Title and description
st.title("Manufacturing: Use Case #5​")
st.subheader("Factory Asset Effectiveness.​")
st.write("📄 Answers to questions about .TX, .MD, and .PDF documents. Upload a document below and ask a question about it – GPT will answer!")
st.write("Note: To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys).")

# Access the OpenAI API key from the secrets file
api_key = st.secrets["OpenAI_key"]

if not api_key:
    st.info("Please enter your OpenAI API key to continue.", icon="🗝️")
else:
    # Set the OpenAI API key
    openai.api_key = api_key

    # Allow the user to upload a file
    uploaded_file = st.file_uploader("Upload a document (.txt or .md)", type=("txt", "md"))

    # Ask the user to input a question
    question = st.text_area(
        "Ask a question about the document!",
        placeholder="Can you give me a brief summary?",
        disabled=not uploaded_file,
    )

    # If both a file is uploaded and a question is asked
    if uploaded_file and question:
        # Read the uploaded document
        document = uploaded_file.read().decode()

        # Prepare the messages for OpenAI
        messages = [
            {
                "role": "user",
                "content": f"Here is a document: {document} \n\n---\n\n {question}",
            }
        ]

        # Generate a response using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )

        # Display the response
        for chunk in response:
            st.write(chunk['choices'][0]['delta']['content'])
