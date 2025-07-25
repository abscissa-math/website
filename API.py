#
#   HEAD
#

# HEAD -> MODULES
from fastapi import FastAPI
from importlib import util
import sys
import SUG


#
#   GATEWAY
#

# GATEWAY -> DIR MOD
sys.path.append(SUG.PDR)
sys.path.append(SUG.DIR)

# GATEWAY -> APPLICATION
app = FastAPI()

# GATEWAY -> INCLUDE
def include(name: str) -> object:
    spec = util.spec_from_file_location(name, f"{SUG.DIR}/api{name}.py")
    module = util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

# GATEWAY -> SCRIPTS
for script in SUG.SCR: app.include_router(include(script).router)