# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_FiveDoF_Moveit_config_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED FiveDoF_Moveit_config_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(FiveDoF_Moveit_config_FOUND FALSE)
  elseif(NOT FiveDoF_Moveit_config_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(FiveDoF_Moveit_config_FOUND FALSE)
  endif()
  return()
endif()
set(_FiveDoF_Moveit_config_CONFIG_INCLUDED TRUE)

# output package information
if(NOT FiveDoF_Moveit_config_FIND_QUIETLY)
  message(STATUS "Found FiveDoF_Moveit_config: 0.3.0 (${FiveDoF_Moveit_config_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'FiveDoF_Moveit_config' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${FiveDoF_Moveit_config_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(FiveDoF_Moveit_config_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${FiveDoF_Moveit_config_DIR}/${_extra}")
endforeach()
