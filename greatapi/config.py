from pathlib import Path

ROOT_PACKAGE_PATH = Path(__file__).parent

GREATAPI_ADMIN_STATIC_PATH = ROOT_PACKAGE_PATH.joinpath("static")
GREATAPI_ADMIN_TEMPLATE_PATH = ROOT_PACKAGE_PATH.joinpath("templates", "admin")
