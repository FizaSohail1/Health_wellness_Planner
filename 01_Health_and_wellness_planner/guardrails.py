from pydantic import BaseModel, Field
from agents import (
    Agent, 
    set_tracing_disabled,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    input_guardrail,
    Runner,
    OutputGuardrailTripwireTriggered,
    output_guardrail,
)
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
from usefull_agents.guardrail_agent import guardrail_agent

load_dotenv()

class MessageOutput(BaseModel): 
    response: str   
    
@input_guardrail
async def input_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str):
    input_text = input if isinstance(input, str) else input[0].get("content", "")

    if len(input_text) < 5:
        print("❌ Input too short:", input_text)
        return GuardrailFunctionOutput(
            output_info="Input must be at least 5 characters long.",
            tripwire_triggered=True
        )

    elif len(input_text) > 300:
        print("❌ Input too long:", input_text)
        return GuardrailFunctionOutput(
            output_info="Input must be less than 300 characters.",
            tripwire_triggered=True
        )

    result = await Runner.run(guardrail_agent, input, context=ctx)

    is_triggered = bool(result.final_output.is_unrelated_query)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=is_triggered
    )


@output_guardrail
async def output_guardrail(ctx:RunContextWrapper, agent:Agent, text:MessageOutput) -> GuardrailFunctionOutput:
      print("✅ Output Guardrail Triggered")
     
      return GuardrailFunctionOutput(
        output_info=None,
        tripwire_triggered= False
    )   

