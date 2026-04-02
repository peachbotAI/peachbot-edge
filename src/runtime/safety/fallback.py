from typing import Dict, Any


class FallbackHandler:
    """
    Provides safe fallback response.
    """

    def handle(self, node_name: str, error: str) -> Dict[str, Any]:
        return {
            "data": {
                "error": True,
                "node": node_name,
                "message": error
            },
            "status": "failed"
        }