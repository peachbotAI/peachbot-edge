import psutil


class HardwareProfile:
    """
    Captures device capabilities.
    """

    def get(self):
        return {
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory_percent": psutil.virtual_memory().percent,
            "cores": psutil.cpu_count(logical=True)
        }