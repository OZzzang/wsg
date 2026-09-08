from dataclasses import dataclass, field

@dataclass
class Config:
    '''
    Configuration class for the WSG application.
    '''
    url: str
    method: str = "GET"
    total_requests: int = 100
    concurrency: int = 10
    headers: dict[str, str] = field(default_factory=dict)
    body: str | None = None
    timeout: float = 10.0
    output_path: str = "results.png"