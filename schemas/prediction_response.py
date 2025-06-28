from pydantic import BaseModel, Field
from typing import Dict

class PredictResponse(BaseModel):
  predicted_category: str = Field(
    ...,
    description="The predicted insurance premium category based on user input.",
    example="high"
  )
  confidence: float = Field(
    ...,
    description="Confidence level of the prediction, ranging from 0 to 1.",
    example=0.85
  )
  class_probabilities: Dict[str, float] = Field(
    ...,
    description="Probabilities of each class label.",
    example={
      "low": 0.1,
      "medium": 0.3,
      "high": 0.6
    }
  )