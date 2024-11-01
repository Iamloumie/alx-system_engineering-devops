# Process Management Project

This repository contains a collection of shell scripts and C programs focused on Linux process management, signals, and PID handling.

## File Descriptions

### Basic Process Operations

- `0-what-is-my-pid` - Script that displays its own Process ID (PID)
- `1-list_your_processes` - Displays a list of currently running processes with hierarchy
- `2-show_your_bash_pid` - Script to display lines containing the word "bash" from process list
- `3-show_your_bash_pid_made_easy` - A simplified version to find and display bash process PID
- `4-to_infinity_and_beyond` - Demonstrates an infinite loop process

### Process Control and Signals

- `5-dont_stop_me_now` - Script showcasing process termination using signals
- `6-stop_me_if_you_can` - Alternative implementation of process termination
- `7-highlander` - Process that demonstrates signal handling and immortality
- `8-beheaded_process` - Script to forcefully terminate a process

### Advanced Process Management

- `100-process_and_pid_file` - Creates PID file and handles multiple signals
- `101-manage_my_process` - Process management script with start/stop/restart functionality
- `manage_my_process` - Backend script managed by 101-manage_my_process

### Process Programming

- `102-zombie.c` - C program that creates zombie processes for demonstration

## Requirements

- All scripts are tested on Ubuntu 20.04 LTS
- All Bash scripts must pass Shellcheck without any errors
- All Bash scripts must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- A README.md file at the root of the directory is mandatory

## Usage Examples

### Running Basic Process Scripts

```bash
./0-what-is-my-pid
./1-list_your_processes
```

### Managing Processes

```bash
./101-manage_my_process start
./101-manage_my_process stop
./101-manage_my_process restart
```

### Compiling and Running C Programs

```bash
gcc 102-zombie.c -o zombie
./zombie
```

## Testing

Verify that all scripts have appropriate permissions:

```bash
chmod +x *.bash
```

Run shellcheck on all bash scripts:

```bash
shellcheck *.bash
```
