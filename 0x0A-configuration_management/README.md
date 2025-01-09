# Puppet Manifests Documentation

This repository contains Puppet manifests for basic system administration tasks.

## Manifest Files

### 0-create_a_file.pp

Creates a file on the target system using Puppet's file resource type.

**Purpose:** File creation and management
**Usage:** Declare file properties like path, content, mode, and ownership

### 1-install_a_package.pp

Manages package installation using Puppet's package resource type.

**Purpose:** Software package installation
**Usage:** Specify package name and desired state (present/absent)

### 2-execute_a_command.pp

Executes commands on the target system using Puppet's exec resource type.

**Purpose:** Command execution automation
**Usage:** Define commands to run, execution conditions, and required paths

## Requirements

- Puppet installed on the system
- Appropriate permissions to execute manifests
- Root access for package installation and file creation

## Running the Manifests

Apply a manifest:

```bash
puppet apply <manifest_name>.pp
```

Example:

```bash
puppet apply 0-create_a_file.pp
```

## Best Practices

- Test manifests in a development environment first
- Review changes before applying to production
- Use version control for manifest management
