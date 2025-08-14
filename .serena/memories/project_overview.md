# Gooroom Security Status Tools - Project Overview

## Purpose
The Gooroom Security Status Tools is a GTK+3 application that provides tools to view and set the security status of the Gooroom platform. It's a desktop application for monitoring and managing security settings on Gooroom OS.

## Tech Stack
- **Language**: C
- **GUI Framework**: GTK+3 (version >= 3.20.0)
- **Build System**: Autotools (autoconf, automake)
- **Dependencies**:
  - GLib 2.0 (>= 2.44.0)
  - GIO (>= 2.58.3)
  - JSON-C for JSON handling
  - PolicyKit (>= 0.103) for privilege escalation
- **Internationalization**: gettext

## Main Application
- **Binary Name**: `gooroom-security-status-tool`
- **Desktop Entry**: Categories include GTK and Utility
- **Application ID**: `kr.gooroom.security.status.view`
- **Main Window**: SysinfoWindow class that extends GtkApplicationWindow

## Key Features
Based on the source code, the application provides:
- Security status monitoring interface
- System information display
- Resource policy dialog (RPD)
- Log filtering and calendar popover functionality
- Integration with various Gooroom security helpers and wrappers

## Architecture
- Main entry point in `src/main.c`
- Core window implementation in `src/sysinfo-window.c`
- Common utilities in `common/` directory
- UI definitions in `.ui` files
- Resource compilation via GLib's resource system