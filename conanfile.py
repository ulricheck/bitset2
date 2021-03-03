from conans import ConanFile, tools, CMake

class Bitset2Conan(ConanFile):
    name = "bitset2"
    version = "0.1"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "cmake/*", "detail/*", "bitset2.hpp", "tests/*", "CMakeLists.txt"

    description = "Bitset2::bitset2 is a header only library. It provides the same functionality as std::bitset with the following extentions/changes."

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.hpp", dst="include", src="detail")
        self.copy(pattern="bitset2.hpp", dst="include", src=".")

    def package_info(self):
        # self.cpp_info.libs = tools.collect_libs(self)
        pass
