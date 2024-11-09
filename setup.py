from cx_Freeze import setup, Executable

setup(
    name="MyPygame",
    version="1.0",
    description="My Pygame Game",
    executables=[Executable("main.py")]
)
