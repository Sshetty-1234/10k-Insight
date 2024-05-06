# 10k-Insight


## What is 10k-Insight

It provides insights into a company's expenditure on total assets across multiple years, sourced from its 10-K reports.

Q - Why would a potential investor care about this information?

Understanding a company's overall expenditure plan is crucial because it shows a commitment to optimal resource and fund allocation. Furthermore, investors love this  approach since it shows a company's unwavering pursuit of growth and expansion, and not settling for anything less.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Choice of Tech Stack

The tech stack for 10k-Insight centers on Python, utilizing Streamlit for a sleek and user-friendly frontend. Python's strength in developing intricate LLM models and its prowess in data analysis and visualization were key factors in the decision


### A little bit more about the llm model ( RAG framework )

The model I have used for this project is called bling-1b-0.1 which is provided by llmware. I used the framework provided by LLMware which is completely free and allows you to run these llm models locally on your machine. For this project, I used the RAG (Retrieval-Augmented Generation) framework to process in the several 10K documents. By processing in the 10K files into the library and processing it - I was able to get insightful information from a company's expenditure plan.




#### How to run the app
1) After cloning the project - create a virtual environment and run "pip install -r requirements.txt." That will install all the necessary packages to run the app
2) Go on app.py and run the file and in the terminal simply type "streamlit run app.py"
