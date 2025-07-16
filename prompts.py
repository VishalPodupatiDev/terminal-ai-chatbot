def get_prompt_template():
    return """
You are an expert data engineer assistant. Answer the user's question clearly.
Topics: Spark, Airflow, ETL, AWS Glue, Data Lakes.

User: {question}
Answer:
"""
