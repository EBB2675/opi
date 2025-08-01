from pydantic import Field, FiniteFloat, NonNegativeInt, PositiveInt, Strict
from typing_extensions import Annotated

StrictPositiveInt = Annotated[PositiveInt, Strict()]

StrictNonNegativeInt = Annotated[NonNegativeInt, Strict()]

StrictFiniteFloat = Annotated[FiniteFloat, Strict()]

StrictPositiveFloat = Annotated[FiniteFloat, Strict(), Field(gt=0)]

StrictNonNegativeFloat = Annotated[FiniteFloat, Strict(), Field(ge=0)]

StrictNegativeFloat = Annotated[FiniteFloat, Strict(), Field(lt=0)]
