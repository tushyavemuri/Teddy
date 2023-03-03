
def sysUtils(inCommand):
    print("Started processing input request "+inCommand)
    match inCommand:
        case "date":
            print("datetime")
        case "uptime":
            print("uptime")
        case "memory":
            print("memory")
        case "network":
            print("network")
        case "users":
            print("users")
        case "processes":
            print("processes"
            )