import psutil

def get_disk_usage():
    return psutil.disk_usage('/')

def get_memory_usage():
    return psutil.virtual_memory()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)
