
#set(pwd "${CMAKE_CURRENT_SOURCE_DIR}/")

include_directories("${CMAKE_CURRENT_SOURCE_DIR}/../include")
file(GLOB files *.cpp)

#add_library(src OBJECT "${pwd}" )
add_library(src OBJECT "${files}")
#target_sources(src1 PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/Bicycle.cpp")
message("files: " "${files}")

#target_sources(TheProject PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/Bicycle.cpp")
#target_sources(TheProject PRIVATE InnerClassIdiom.cpp)


#set(src "BANAN")


#message("SOURCES " "${SOURCES}")

#set(SOURCE ${SOURCE} ${CMAKE_CURRENT_SOURCE_DIR}/......
#file(GLOB src_sources *.cpp)
#add_library(src ${src_sources})
