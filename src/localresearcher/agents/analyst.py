"""Analyst agent - interprets and analyzes research findings."""

from localresearcher.llm.base import BaseLLMProvider


class AnalystAgent:
    """Agent responsible for analysis and interpretation."""
    
    def __init__(self, llm: BaseLLMProvider):
        self.llm = llm
    
    async def analyze(self, query: str, plan: str, findings: str) -> str:
        """Analyze research findings."""
        system_prompt = """You are an expert analyst. Your job is to interpret research findings and extract insights.

Your analysis should:
1. Identify key patterns and trends
2. Draw meaningful conclusions
3. Highlight important implications
4. Connect findings to the original query
5. Provide actionable insights

Be objective and evidence-based."""
        
        prompt = f"""Original Query: {query}

Research Plan:
{plan}

Research Findings:
{findings}

Analyze these findings and provide deep insights."""
        
        analysis = await self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.6,
            max_tokens=2000,
        )
        
        return analysis