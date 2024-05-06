import os
import re
from llmware.prompts import Prompt, HumanInTheLoop
from llmware.configs import LLMWareConfig
from llmware.retrieval import Query
from llmware.library import Library


def example_4a_contract_analysis_from_library (model_name, verbose=False):

   

    '''
    To load in APPL files: 10K filing reports/APPL_PDF
    To load in DELL files: 
    '''
    
    file_path = "10K filing reports/DELL_PDF"

    # Creating a library to load and save the necessary files
    contracts_lib = Library().create_new_library("library5")
    contracts_lib.add_files(file_path)

    '''
    APPL documents:  topic : Capital Assets
                     llmquery : What was the company's capital expenditure during the year?
                     
    DELL documents: topic : Capital Commitments
                    llmquery : Can you help me find the section in the document that discusses capital expenditures, specifically focusing on spending for property, plant, and equipment, as well as funding for equipment under DFS operating leases?
    '''
    
    question_list = [{"topic": "Capital Commitments", "llm_query":"Can you help me find the section in the document that discusses capital expenditures, specifically focusing on spending for property, plant, and equipment, as well as funding for equipment under DFS operating leases?"}]

    print (f"\n > Loading model {model_name}...")

    q = Query(contracts_lib)

    # get a list of all of the unique documents in the library
    doc_list = q.list_doc_id()
    print("update: document id list - ", doc_list)

    # filename list
    fn_list = q.list_doc_fn()
    print("update: filename list - ", fn_list)

    prompter = Prompt().load_model(model_name)

    for i, doc_id in enumerate(doc_list):

        print("\nAnalyzing 10K documents: ", str(i+1), doc_id, fn_list[i])

        print("LLM Responses:")

        for question in question_list:

            query_topic = question["topic"]
            llm_question = question["llm_query"]

            doc_filter = {"doc_ID": [doc_id]}
            query_results = q.text_query_with_document_filter(query_topic,doc_filter,result_count=5,exact_mode=True)

            if verbose:
                # this will display the query results from the query above
                for j, qr in enumerate(query_results):
                    print("update: querying document - ", query_topic, j, doc_filter, qr)

            source = prompter.add_source_query_results(query_results)

            #   *** this is the call to the llm with the source packaged in the context automatically ***
            responses = prompter.prompt_with_source(llm_question, prompt_name="default_with_context", temperature=0.3)

            #   unpacking the results from the LLM
            for r, response in enumerate(responses):
                print("update: llm response -  ", llm_question, re.sub("[\n]"," ", response["llm_response"]).strip())

            prompter.clear_source_materials()

    #   Save jsonl report to jsonl to /prompt_history folder
    print("\nPrompt state saved at: ", os.path.join(LLMWareConfig.get_prompt_path(),prompter.prompt_id))
    prompter.save_state()
    
    #   Save csv report to csv to /prompt_history folder
    csv_output = HumanInTheLoop(prompter).export_current_interaction_to_csv()
    print("\nupdate: CSV output saved at - ", csv_output)

    2001

    return 0



if __name__ == "__main__":

   
    LLMWareConfig().set_active_db("sqlite")

    example_models = ["llmware/bling-1b-0.1", "llmware/bling-tiny-llama-v0", "llmware/dragon-yi-6b-gguf"]

    #list of models provided but we will be using the bling-1b-0.1
    model_name = example_models[0]

 
    example_4a_contract_analysis_from_library(model_name)
