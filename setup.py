import os
from sys import platform as _platform
from setuptools import Extension, setup

cflags = []

if _platform == "darwin":
    os.environ["CC"] = "xcrun --sdk macosx clang"
    os.environ["CXX"] = "xcrun --sdk macosx clang"
    cflags += ['-stdlib=libc++', '-mmacosx-version-min=10.7']

setup(
    ext_modules=[
        Extension(
            name="lnt.testing.profile.cPerf",
            sources=["lnt/testing/profile/cPerf.cpp"],
            extra_compile_args=['-std=c++11'] + cflags,
        ),
    ]
)
