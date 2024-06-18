import os
import autogen
from langchain.tools.shell.tool import ShellTool
from autogen import GroupChat, GroupChatManager, ConversableAgent
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent


shell_tool = ShellTool()

config_list_gpt4_preview = autogen.config_list_from_json(
    "./OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-3.5-turbo"]
    }
)

project_structure = """
Project structure is
    /project
    |-- /node_modules
    |-- /html
    |   |-- index.html
    |-- /css
    |   |-- /styles.css                
    |-- /js
    |   |-- index.js
    |   |-- addTodo.js
    |   |-- deleteTodo.js
    |   |-- markTodoAsComplete.js
    |-- /tests
    |   |-- addTodo.test.js
    |   |-- deleteTodo.test.js
    |   |-- markTodoAsComplete.test.js
    |-- package.json
    |-- package-lock.json
    |-- README.md
"""

# Start logging
logging_session_id = autogen.runtime_logging.start(config={"dbname": "execution_logs.db"})

print("Logging session ID: " + str(logging_session_id))

tools = [
            {
            "type": "function",
            "function": {
            "name": "terminal",
            "description": "Run shell commands on this Linux machine.",
            "parameters": {
                "type": "object",
                "properties": {
                "commands": {
                    "title": "Commands",
                    "description": "List of shell commands to run. Deserialized using json.loads",
                    "anyOf": [
                    { "type": "string" },
                    { "type": "array", "items": { "type": "string" } }
                    ]
                }
                },
                "required": ["commands"]
            }
            }
        }
]

manager = ConversableAgent(
    name="Product_Manager",
    system_message="You are Managing a team of JS developers and testers. You're goal is to get software built based on given requirements",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

programmer1 = GPTAssistantAgent(
    name="Tester",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are tester, who writes tests in jest. Following the Test driven development approach. 
    You donot execute the tests, just write them. You dont implement the actual functionalities as well, just write the tests
    Use jest to setup the project. You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Run every command only after cd into the project directory /workspaces/autogen/project
    Follow the standard project structure and write the tests at particular location, keeping in mind that in future there might be more tests written.
    {project_structure}
    """,
)

programmer1.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)

programmer2 = GPTAssistantAgent(
    name="Tester",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are tester, who writes tests in jest. Following the Test driven development approach. 
    You donot execute the tests, just write them. You dont implement the actual functionalities as well, just write the tests
    Use jest to setup the project. You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Run every command only after cd into the project directory /workspaces/autogen/project
    Follow the standard project structure and write the tests at particular location, keeping in mind that in future there might be more tests written.
    {project_structure}
    """,
)

programmer2.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)

programmer3 = GPTAssistantAgent(
    name="JS_developer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are a JS developer who implements functionalities. Run the generated code against the tests written and make them pass. 
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Run every command only after cd into the project directory /workspaces/autogen/project
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,
)

programmer3.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)

programmer4 = GPTAssistantAgent(
    name="JS_developer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are a JS developer who implements functionalities. Run the generated code against the tests written and make them pass. 
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,)


programmer4.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)


programmer5 = GPTAssistantAgent(
    name="html_css_js_developer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are a developer who is skilled in html, css and js who integrates the functionalities with UI.
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,)


programmer5.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)


programmer6 = GPTAssistantAgent(
    name="html_css_js_developer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are a developer who is skilled in html, css and js who integrates the functionalities with UI.
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,)


programmer6.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)


project_maintainer1 = GPTAssistantAgent(
    name="project_maintainer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are this projects representative. You document the steps needed to run this project in README.md file.
    Then you zip all the required files, and save the .zip in project directory
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,)


project_maintainer1.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)


project_maintainer2 = GPTAssistantAgent(
    name="project_maintainer",
    llm_config={
        "tools": tools,
        "config_list": config_list_gpt4_preview
    },
    instructions=f"""
    You are this projects representative. You document the steps needed to run this project in README.md file.
    Then you zip all the required files, and save the .zip in project directory
    You have access to shell tool to run shell commands. Use shell tool to save the generated files in the project directory
    Follow proper Project structure, and write the functionalities keeping in mind that additional functionalities will be added in future. 
    {project_structure}
    """,)

project_maintainer2.register_function(
    function_map={
        shell_tool.name: shell_tool._run
    }
)


testers_group = GroupChat(
    agents=[programmer1, programmer2],
    messages=[],
    max_round=6,
    send_introductions=True,
        speaker_selection_method="round_robin",

)

    
testers_group_manager = GroupChatManager(
    groupchat=testers_group,
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

programmers_group = GroupChat(
    agents=[programmer3, programmer4],
    messages=[],
    max_round=6,
    send_introductions=True,
    speaker_selection_method="round_robin",
)


programmers_group_manager = GroupChatManager(
    groupchat=programmers_group,
    llm_config={"config_list": [{"model": "gpt-4-1106-preview", "api_key": os.environ["OPENAI_API_KEY"]}]},
)


chat_result = manager.initiate_chats(
    [
        {
            "recipient": testers_group_manager,
            "message": """
            Write tests for add todo functionality. Add all the code in structured format in /workspaces/autogen/project. 
            Make sure to write the tests completely, donot leave the tests empty or incomplete
            """,
            "summary_method": "reflection_with_llm",
        },
        {
            "recipient": programmers_group_manager,
            "message": """
            Write the code based on the add todo tests written, make sure the code passes the tests.
            Before proceeding to the next step, run the code against the tests and check if the tests pass, if not make sure the tests pass
            Refer and Add all the code in structured format Pin /workspaces/autogen/project
            """,
            "summary_method": "reflection_with_llm",
        },
        # {
        #     "recipient": testers_group_manager,
        #     "message": """
        #     Write tests for delete todo functionality. Add all the code in structured format in /workspaces/autogen/project. 
        #     Make sure to write the tests completely, donot leave the tests empty or incomplete
        #     """,
        #     "summary_method": "reflection_with_llm",
        # },
        # {
        #     "recipient": programmers_group_manager,
        #     "message": """
        #     Write the code based on the delete todo tests written, make sure the code passes the tests.
        #     Before proceeding to the next step, run the code against the tests and check if the tests pass, if not make sure the tests pass
        #     Refer and Add all the code in structured format in /workspaces/autogen/project
        #     """,
        #     "summary_method": "reflection_with_llm",
        # },
        # {
        #     "recipient": testers_group_manager,
        #     "message": """
        #     Write tests for marking todo as complete functionality. Add all the code in structured format in /workspaces/autogen/project. 
        #     Make sure to write the tests completely, donot leave the tests empty or incomplete
        #     """,
        #     "summary_method": "reflection_with_llm",
        # },
        # {
        #     "recipient": programmers_group_manager,
        #     "message": """
        #     Write the code based on the marking todo as complete tests written, make sure the code passes the tests.
        #     Before proceeding to the next step, run the code against the tests and check if the tests pass, if not make sure the tests pass
        #     Refer and Add all the code in structured format in /workspaces/autogen/project
        #     """,
        #     "summary_method": "reflection_with_llm",
        # }
    ]
)

autogen.runtime_logging.stop()
