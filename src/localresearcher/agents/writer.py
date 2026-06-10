"""Writer agent - creates final structured reports."""

from localresearcher.llm.base import BaseLLMProvider


class WriterAgent:
    """Agent responsible for final report generation."""
    
    def __init__(self, llm: BaseLLMProvider):
        self.llm = llm
    
    async def write_report(
        self,
        query: str,
        plan: str,
        findings: str,
        analysis: str,
        critique: str,
    ) -> str:
        """Write a comprehensive final report."""
        system_prompt = """You are an expert technical writer. Your job is to create clear, structured, professional reports.

Your report should:
1. Have a clear executive summary
2. Present findings in a logical structure
3. Include specific evidence and examples
4. Address limitations and critiques
5. Provide actionable recommendations
6. Use proper Markdown formatting

Write in a professional but accessible tone."""
        
        prompt = f"""Original Query: {query}

Research Plan:
{plan}

Findings:
{findings}

Analysis:
{analysis}

Critical Review:
{critique}

Write a comprehensive research report in Markdown format with the following sections:
- Executive Summary
- Key Findings
- Detailed Analysis
- Limitations & Considerations
- Recommendations
- Conclusion"""
        
        report = await self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=0.7,
            max_tokens=3000,
        )
        
        return report