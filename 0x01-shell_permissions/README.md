# Shell Permissions

This project contains scripts that demonstrate various aspects of file permissions and ownership in Unix-like operating systems.

## Scripts and Their Functions

0. **0-iam_betty**: Switches the current user to the user betty.
1. **1-who_am_i**: Prints the effective username of the current user.
2. **2-groups**: Prints all the groups the current user is part of.
3. **3-new_owner**: Changes the owner of the file hello to the user betty.
4. **4-empty**: Creates an empty file called hello.
5. **5-execute**: Adds execute permission to the owner of the file hello.
6. **6-multiple_permissions**: Adds execute permission to the owner and group owner, and read permission to other users, to the file hello.
7. **7-everybody**: Adds execution permission to the owner, group owner and other users, to the file hello.
8. **8-James_Bond**: Sets the permission to the file hello as follows:
   - Owner: no permission at all
   - Group: no permission at all
   - Other users: all the permissions
9. **9-John_Doe**: Sets the mode of the file hello to: -rwxr-x-wx
10. **10-mirror_permissions**: Sets the mode of the file hello the same as olleh's mode.
11. **11-directories_permissions**: Adds execute permission to all subdirectories of the current directory for the owner, group owner and all other users.
12. **12-directory_permissions**: Creates a directory called my_dir with permissions 751 in the working directory.
13. **13-change_group**: Changes the group owner to school for the file hello.
14. **100-change_owner_and_group**: Changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
15. **101-symbolic_link_permissions**: Changes the owner and the group owner of \_hello to vincent and staff respectively.
16. **102-if_only**: Changes the owner of the file hello to betty only if it is owned by the user guillaume.
17. **103-Star_Wars**: Plays the StarWars IV episode in the terminal.

## Usage

To use these scripts, make sure they have execute permissions. You can add execute permissions to a script using:

```bash
chmod +x script_name
```
