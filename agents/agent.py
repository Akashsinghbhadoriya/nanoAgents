from agents.step_trace import StepTrace
from agents.state import AgentState
from agents.react_prompt import build_react_prompt
from agents.react_parser import parse_response
from agents.action import Action
from agents.observation import Observation
from agents.tool_call import ToolCall
import json

class Agent:

    def __init__(self, registry, llm, memory, factmemory):
        self.registry = registry
        self.llm = llm
        self.memory = memory
        self.facts = factmemory.get_all_facts()

    def run(self, query, context):
        Max_steps = 5

        state = AgentState(user_query=query)
        tool_descriptions = self.registry.tool_descriptions()
        past_memory = self.memory.get_context()
        self.memory.add("user", query)

        for step in range(Max_steps):
            prompt = build_react_prompt(
                state.user_query, 
                state.actions, 
                state.observations, 
                tool_descriptions,
                past_memory,
                self.facts,
                context
            )
            
            response = self.llm.generate(prompt)

            parsed = parse_response(response)
            if parsed["type"] == "finish":
                self.memory.add("assistant", parsed["answer"])
                return parsed["answer"]
            
            action = Action(
                tool=parsed["tool"],
                args=parsed["args"]
            )
            state.actions.append(action)
            
            result = self.registry.execute(
                ToolCall(
                    tool=action.tool,
                    args=action.args
                    )
            )
            observation = Observation(content=str(result))
            state.observations.append(observation)

            steptrace = StepTrace(
                step=step,
                query=query,
                prompt=prompt,
                llm_response=parsed,
                action=str(action),
                observation=str(observation)
            )
            print(json.dumps(steptrace.__dict__, indent=4, default=str))

        