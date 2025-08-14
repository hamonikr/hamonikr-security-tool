# Code Style and Conventions

## General C Style
- **Header Guards**: Use traditional `#ifndef/_define_/#endif` pattern
- **Naming Convention**: 
  - Snake_case for functions and variables
  - PascalCase for type names (e.g., `SysinfoWindow`)
  - ALL_CAPS for constants and macros
- **File Extensions**: `.c` for implementation, `.h` for headers

## GObject/GTK+ Conventions
- **Type Definitions**: Follow GObject pattern with type macros:
  ```c
  #define SYSINFO_TYPE_WINDOW            (sysinfo_window_get_type ())
  #define SYSINFO_WINDOW(obj)            (G_TYPE_CHECK_INSTANCE_CAST (...))
  ```
- **Class Structure**: Separate public and private structures
- **Function Naming**: Prefix with class name (e.g., `sysinfo_window_new`)

## Header Structure
- Standard copyright header with GPL license
- Include guards
- Proper `G_BEGIN_DECLS`/`G_END_DECLS` for C++ compatibility
- Logical grouping of includes

## Code Organization
- Common utilities in `common/` directory
- UI files (.ui) for Glade/interface definitions
- Resource files managed via GLib resource system
- Separate header and implementation files

## Documentation
- License headers on all files
- Minimal inline comments (focused on functionality)
- No excessive documentation requirements observed