"""Core data schemas for LocalResearcherAI."""

from enum import Enum
from typing import Any
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class AgentStep(str, Enum):
    """Agent execution steps."""
    
    PLANNING = "planning"
    RESEARCHING = "researching"
    ANALYZING = "analyzing"
    CRITIQUING = "critiquing"
    WRITING = "writing"


class TaskStatus(str, Enum):
    """Task execution status."""
    
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class Document(BaseModel):
    """Document metadata."""
    
    id: UUID = Field(default_factory=uuid4)
    path: str
    content: str
    file_type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: dict[str, Any] = Field(default_factory=dict)


class Task(BaseModel):
    """Research task."""
    
    id: UUID = Field(default_factory=uuid4)
    query: str
    documents: list[Document] = Field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class AgentOutput(BaseModel):
    """Output from an agent."""
    
    step: AgentStep
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class WorkflowState(BaseModel):
    """State of the workflow execution."""
    
    task: Task
    plan: str = ""
    research_findings: str = ""
    analysis: str = ""
    critique: str = ""
    final_report: str = ""
    current_step: AgentStep = AgentStep.PLANNING
    outputs: list[AgentOutput] = Field(default_factory=list)


class Report(BaseModel):
    """Final research report."""
    
    id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    title: str
    content: str
    format: str = "markdown"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: dict[str, Any] = Field(default_factory=dict)