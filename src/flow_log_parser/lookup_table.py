from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class LookupTable:
    """
    Represents a CSV lookup table
    """
    columns: List[str]
    rows: List[Dict[str, Any]]

    def __post_init__(self):
        if not isinstance(self.columns, List):
            raise TypeError(f"Invalid lookup table columns: {self.columns}. Expected 'List'.")
        
        for column in self.columns:
            if not isinstance(column, str):
                raise TypeError(f"'{column}' is not a valid lookup table column. Expected string.")
        
        if not isinstance(self.rows, List):
            raise TypeError(f"Expected a list of lookup table rows, received: {self.columns}.")

        for row in self.rows:
            if not isinstance(row, Dict):
                raise TypeError(f"'{column}' is not a valid lookup table row. Expected 'Dict[str, Any]'.")