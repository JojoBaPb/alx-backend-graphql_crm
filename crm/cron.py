import datetime

def log_crm_heartbeat():
    """Logs a heartbeat message with timestamp to confirm app health."""
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{now} CRM is alive\n")

