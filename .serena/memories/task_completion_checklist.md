# Task Completion Checklist

## Before Committing Changes
1. **Build Check**: Ensure the project builds successfully
   ```bash
   make clean && make
   ```

2. **Code Style**: Verify code follows project conventions
   - Check header guards and includes
   - Verify GObject/GTK+ patterns are followed
   - Ensure proper naming conventions

3. **Resource Compilation**: Ensure UI resources compile properly
   ```bash
   # Resources should build automatically with make
   # Check for any gresource compilation errors
   ```

4. **Desktop Integration**: Validate desktop file if modified
   ```bash
   desktop-file-validate src/gooroom-security-status-tool.desktop
   ```

## No Automated Testing
- This project does not appear to have automated unit tests
- Manual testing by running the application is required
- Test the built application: `./src/gooroom-security-status-tool`

## Build System Verification
- Ensure Makefile.am files are updated if new files are added
- Check that configure.ac dependencies are correct
- Verify internationalization files (po/) if strings are modified

## Quality Checks
- **Memory Management**: Ensure proper GObject reference counting
- **Error Handling**: Check for proper error handling in new code
- **Security**: Be mindful of privilege escalation code (PolicyKit usage)

## Note
Since this is a system security tool, extra care should be taken with:
- Input validation
- Privilege handling
- Security-related functionality