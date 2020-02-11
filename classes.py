from dataclasses import dataclass


@dataclass(frozen=True)
class Topic:
    topic_id: str
    wikilink: str
    score: float
    wikidata_id: str = None


@dataclass(frozen=True)
class Category:
    category_id: str
    label: str
    score: float
