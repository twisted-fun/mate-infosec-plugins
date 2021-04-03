from setuptools import setup

setup(
    name="mate-infosec-plugins",
    install_requires="mate",
    entry_points={"infosec": ["ida_calc = plug_calc", "bitwise_str_xor = plug_xor"]},
    py_modules=["plug_calc", "plug_xor"],
)
