
add_executable(bench01 bench01.cpp)
target_include_directories(bench01 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(counter128 counter128.cpp)
target_include_directories(counter128 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(example01 example01.cpp)
target_include_directories(example01 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(test_array2array test_array2array.cpp)
target_include_directories(test_array2array PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(test_bitset2_01 test_bitset2_01.cpp)
target_include_directories(test_bitset2_01 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(test_bitset2_02 test_bitset2_02.cpp)
target_include_directories(test_bitset2_02 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(test_nonconst_constexpr01 test_nonconst_constexpr01.cpp)
target_include_directories(test_nonconst_constexpr01 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(test_ullong2array test_ullong2array.cpp)
target_include_directories(test_ullong2array PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)

add_executable(tests01 tests01.cpp)
target_include_directories(tests01 PRIVATE ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/detail)
