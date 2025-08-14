# Codebase Structure

## Directory Layout
```
gooroom-security-status-tools/
├── src/                    # Main application source code
├── common/                 # Shared utilities and common code
├── data/                   # Data files, helpers, and resources
├── po/                     # Internationalization files
├── debian/                 # Debian packaging files
├── configure.ac            # Autoconf configuration
├── Makefile.am            # Automake configuration
├── autogen.sh             # Build system initialization
└── README                 # Project description
```

## Source Code (src/)
- **main.c**: Application entry point and GTK application setup
- **sysinfo-window.h/.c**: Main application window implementation
- **rpd-dialog.h/.c**: Resource Policy Dialog
- **calendar-popover.h/.c**: Calendar popup component
- **logfilter-popover.h/.c**: Log filtering popup component
- **stack-list.h**: Stack list utilities
- **gresource.xml**: Resource definition file
- **Makefile.am**: Build configuration for source

## Common Code (common/)
- **common.h/.c**: Shared utility functions and definitions
- **gooroom-systemd-control-helper.c**: SystemD service control helper
- **Makefile.am**: Build configuration for common library

## Data Files (data/)
- **Helper scripts**: Various wrapper scripts for system operations
- **gooroom-update-checker**: Update checking utility
- **gooroom-iptables-wrapper**: Firewall management wrapper
- **style.css**: Application styling
- **icons/**: Application icons
- **PolicyKit files**: Security policy definitions

## Key Files
- **Desktop Entry**: `src/gooroom-security-status-tool.desktop.in`
- **GSettings Schema**: `src/apps.gooroom-security-status-tool.gschema.xml`
- **UI Definitions**: `src/*.ui` files for interface layouts

## Build Artifacts
- Generated resource files: `sysinfo-resources.c/.h`
- Compiled desktop file: `gooroom-security-status-tool.desktop`
- Final binary: `gooroom-security-status-tool`