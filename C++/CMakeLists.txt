cmake_minimum_required(VERSION 3.6.2)
project(TheProject VERSION 1.0)

# add the executable
#set(MAIN "${PROJECT_SOURCE_DIR}/src/TheProject.cpp")

add_subdirectory(src)
add_executable(TheProject $<TARGET_OBJECTS:src>)
target_include_directories(TheProject PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}/include")
set_target_properties(TheProject PROPERTIES LINKER_LANGUAGE CXX)
#target_link_libraries(TheProject PRIVATE ${src})

# This is probably not good, more of a compile everything and then link it as a library.
# subdirectories
# add_subdirectory(src)
# target_link_libraries(TheProject src)

# install the binary
install(TARGETS TheProject DESTINATION "${PROJECT_SOURCE_DIR}/bin")

configure_file("${PROJECT_SOURCE_DIR}/include/TheProject.h.in" "${PROJECT_SOURCE_DIR}/include/TheProject.h")


# specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
