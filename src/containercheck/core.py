from collections.abc import Iterable, Mapping

def validate(containers: Iterable[Mapping[str, object]]) -> list[str]:
    """Validate basic container metadata."""
    errors=[]
    for i,c in enumerate(containers):
        if not str(c.get("name","")).strip(): errors.append(f"container[{i}]: missing name")
        if not str(c.get("image","")).strip(): errors.append(f"container[{i}]: missing image")
    return errors
