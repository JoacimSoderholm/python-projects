file(REMOVE_RECURSE
  "TheProject.pdb"
  "TheProject"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/TheProject.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
