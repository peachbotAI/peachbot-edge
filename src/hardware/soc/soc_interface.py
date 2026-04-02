class SoCInterface:
    """
    Hardware abstraction layer for edge device interaction.
    """

    def get_status(self) -> dict:
        return {"soc": "idle"}