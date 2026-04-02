import platform

try:
    import psutil
except ImportError:
    psutil = None

VERSION = "0.1.0-edge"


def get_system_info():
    info = {
        "os": platform.system(),
        "cpu": platform.processor() or "Unknown",
        "cores": "N/A",
        "ram": "N/A"
    }

    if psutil:
        info["cores"] = psutil.cpu_count(logical=True)
        info["ram"] = round(psutil.virtual_memory().total / (1024**3), 2)

    return info


def show_banner():
    print(r"""
   ____                  _     ____        _   
  |  _ \ ___  __ _  ___ | |__ | __ )  ___ | |_ 
  | |_) / _ \/ _` |/ _ \| '_ \|  _ \ / _ \| __|
  |  __/  __/ (_| | (_) | | | | |_) | (_) | |_ 
  |_|   \___|\__,_|\___/|_| |_|____/ \___/ \__|

        PEACHBOT EDGE • SBC FOR BIOLOGY
    """)

    print("-" * 50)
    print("PeachBot Edge Runtime")
    print(f"Version      : {VERSION}")
    print("Mode         : Edge-native | Deterministic | Offline-first")

    info = get_system_info()

    print("\nSYSTEM INFO")
    print(f"OS           : {info['os']}")
    print(f"CPU          : {info['cpu']}")
    print(f"Cores        : {info['cores']}")
    print(f"Memory       : {info['ram']} GB")

    print("\nRUNTIME CONFIG")
    print("SBC Engine   : Active")
    print("FILA Layer   : Enabled (Metadata-only)")
    print("Execution    : Adaptive Graph Engine")

    print("\nDOMAINS")
    print("MedAI | Eco | AgriAI | Bio")

    print("-" * 50 + "\n")