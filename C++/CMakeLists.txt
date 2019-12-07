cmake_minimum_required(VERSION 3.6.2)
project(TheProject VERSION 1.0)
enable_language(CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_SYSTEM_NAME Linux)
#set(CMAKE_SYSTEM_PROCESSOR arm)


#set(triple x86_64-pc-win32) https://stackoverflow.com/questions/23248989/clang-c-cross-compiler-generating-windows-executable-from-mac-os-x

#set(triple x86_64-redhat-linux)
set(triple x86_64-unknown-linux-gnu)
set(CMAKE_C_COMPILER clang)
set(CMAKE_C_COMPILER_TARGET ${triple})
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_COMPILER_TARGET ${triple})
set(CMAKE_INSTALL_PREFIX .)

if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()

# add the executable
#set(MAIN "${PROJECT_SOURCE_DIR}/src/TheProject.cpp")

add_subdirectory(src)
add_executable(TheProject $<TARGET_OBJECTS:src>)
target_include_directories(TheProject PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}/include")
set_target_properties(TheProject PROPERTIES LINKER_LANGUAGE CXX)
set_property(TARGET TheProject PROPERTY CXX_STANDARD 14)
#target_link_libraries(TheProject PRIVATE ${src})


install(TARGETS TheProject# mySharedLib myStaticLib
        RUNTIME DESTINATION bin)
        #LIBRARY DESTINATION lib
        #ARCHIVE DESTINATION lib/static)
#install(TARGETS mySharedLib DESTINATION /some/full/path)

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
