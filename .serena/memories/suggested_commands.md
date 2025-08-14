# Suggested Commands for Development

## Build System Commands
```bash
# Initialize build system (requires gnome-common)
./autogen.sh

# Configure the build
./configure

# Build the project
make

# Install the application
make install

# Clean build artifacts
make clean
make distclean
```

## Development Workflow
```bash
# Check if build dependencies are available
which gnome-autogen.sh

# Full build from scratch
./autogen.sh && make

# Run the application (after build)
./src/gooroom-security-status-tool
```

## System Commands (Linux)
```bash
# File operations
ls -la
find . -name "*.c" -o -name "*.h"
grep -r "pattern" src/

# Git operations
git status
git add .
git commit -m "message"
git log --oneline

# Package management (if needed for dependencies)
apt install libgtk-3-dev libglib2.0-dev libjson-c-dev libpolkit-gobject-1-dev
```

## Resource Compilation
The project uses GLib's resource system. Resources are automatically compiled during build via rules in Makefile.am:
```bash
# Resources are built automatically, but manually:
glib-compile-resources --generate-source gresource.xml
glib-compile-resources --generate-header gresource.xml
```

## Testing/Running
```bash
# Run the built application
./src/gooroom-security-status-tool

# Check desktop file
desktop-file-validate src/gooroom-security-status-tool.desktop
```