from agents import build_reader_agent,build_search_agent,writer_chain,critic_chain

def run_research_pipeline(topic:str) ->dict:
    state={}
    #search engine working
    print("\n"+"-"*75)
    print("Step 1 - Search Agent is working...")
    print("-"*75)

    search_agent=build_search_agent()
    search_result=search_agent.invoke({
        "messages":[("user",f"Find recent, reliable and detailed information about: {topic}")]
    })

    state["search_results"]=search_result['messages'][-1].content

    print("\n Search result ",state["search_results"])

    #step 2 for Reader agent
    print("\n"+"-"*75)
    print("Step 1 - Reader Agent is working...")
    print("-"*75)

    reader_agent=build_reader_agent()
    reader_result=reader_agent.invoke({
        "messages":[("user",f"Based on the following search result about '{topic}',"
                     f"pick the most relevent URL and scrape it for deeper content.\n\n"
                     f"Search results:\n {state['search_results'][:800]}"
                     
        )]
    })

    state['scraped_content']=reader_result['messages'][-1].content

    print("\n Scraped content result",state["scraped_content"])

    #Step 3 Writer chain
    print("\n"+"-"*75)
    print("Step 3 - Writing a draft report")
    print("-"*75)

    research_combined=(
        f"SEARCH RESULT :\n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT:\n {state["scraped_content"]}\n\n"
    )

    state["report"]=writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })
    
    print("\n Final Report\n",state["report"])

    print("\n"+"-"*75)
    print("Step 4 - Critic Report")
    print("-"*75)

    state["critic_report"]=critic_chain.invoke({"report":state["report"]})

    print("\n Critic Report\n",state["critic_report"])

    return state



if __name__ == "__main__":
    topic=input("Enter a reserch topic: ")
    state=run_research_pipeline(topic)