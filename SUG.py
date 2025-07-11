#
#   HANDLER
#

# HANDLER -> LOAD
from website import *


#
#   REQUEST SUPERGLOBALS
#

# REQUEST SUPERGLOBALS -> CONTAINER
REQ = threading.local()

# REQUEST SUPERGLOBALS -> SESSION ID
REQ.SID = None

# REQUEST SUPERGLOBALS -> IP
REQ.SIP = None

# REQUEST SUPERGLOBALS -> POST
REQ.PST = None

# REQUEST SUPERGLOBALS -> RESPONSE
REQ.RES = None


#
#   THREAD SUPERGLOBALS
#

# THREAD SUPERGLOBALS -> CONTAINER
THR = threading.local()


#
#   MASTER SUPERGLOBALS
#

# MASTER SUPERGLOBALS -> DATABASE CREDENTIALS
DBC = {
    "HOST": "localhost",
    "USER": "phpmyadmin",
    "PASSWORD": "orangepi",
    "DATABASE": "abscissa"
}


# MASTER SUPERGLOBALS -> DIRECTORY
DIR = str(os.path.dirname(os.path.abspath(__file__))) + "/"

# MASTER SUPERGLOBALS -> REGEX PATTERNS
PAT = {
    "Cprocess": {
        "content", 
        "duration"
    },
    "Kde": r"^.{8,64}$",
    "Ken": r"^.{8,64}$",
    "Kes": r"^.{8,64}$",
    "Kid": r"^\d+$",
    "Oid": r"^\d+$",
    "Oname": r'^[a-zA-Z0-9_-]{4,32}$',
    "Pdataen": {
        "editor",
        "instructions",
        "svg"
    },
    "Pdataes": {
        "editor",
        "instructions",
        "svg"
    },
    "Pdatade": {
        "editor",
        "instructions",
        "svg"
    },
    "Pid": r'^[A-Z0-9]{8}$',
    "Pmeta":{
        "calculator",
        "postResult",
        "preResult"
    },
    "Psolution": {
        "numericalResult",
        "result"
    },
    "Rlang": r"^(en|es|de)$",
    "Rlink": r"^.{8,255}$",
    "Rvideo": r"^(True|False)$",
    "Uemail": r'^[A-Za-z0-9._%\-]{8,64}@gmail\.com$',
    "Uhashpass": r"^.{8,64}$",
    "Uid": r"^\d+$",
    "Uname": r'^[a-zA-Z0-9_-]{4,32}$'
}

# MASTER SUPERGLOBALS -> PERMISSIONS
PER = {
    "concept": {
        "create": 255
    },
    "organisation": {
        "create": 1,
        "join": 0
    },
    "problem": {
        "create": 255
    },
    "resource": {
        "create": 1
    },
    "session": {
        "refresh": 0
    },
    "user": {
        "delete": 0,
        "ban": 255
    }
}

# MASTER SUPERGLOBALS -> ERROR CODES
ERR = [
    500,
    400,
    400,
    403
]