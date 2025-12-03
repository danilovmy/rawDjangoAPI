## How to compile mysqlclient from Source (Fixing Linker Errors) for last version of python on Windows 10, if official whl for this version is not available.

This guide provides step-by-step instructions for successfully compiling the PyMySQL/mysqlclient package from source on Windows 10, addressing the common errors related to missing header files (mysql.h) and unresolved linker symbols (mysql_field_count, mariadbclient.lib).

This process leverages the MariaDB Connector/C as the required MySQL C client library, in additional refer to [README.md](https://github.com/PyMySQL/mysqlclient/blob/main/README.md)

Prerequisites:

Python: Python 3.last_version installed (ensure it matches the architecture of Visual Studio, usually 64-bit).

Git: Installed and configured for cloning the repository.

Visual Studio Build Tools: You need a recent version of Visual Studio (e.g., 2017, 2019, or 2022) with the Desktop development with C/C++ workload installed. This provides the necessary C/C++ compiler and linker (cl.exe, link.exe).

MariaDB Connector/C (The Fix): Download and install the **latest** MariaDB Connector/C for Windows (the official C client library).

Note: This connector is used because it provides the necessary header and library files that are often difficult to source or link correctly when relying on standard MySQL installations or older connectors.

1. Get the Source Code
Clone the mysqlclient repository and navigate into the directory.

git clone [https://github.com/PyMySQL/mysqlclient.git](https://github.com/PyMySQL/mysqlclient.git)
cd mysqlclient

2. Fix Missing Header Files (mysql.h not found)

When attempting to compile, the build process often fails because it cannot locate the core MySQL header files, typically resulting in an error like: include mysql.h not found.

To fix this, you must manually copy the header files from the MariaDB Connector/C installation directory into the src/MySQLdb folder in the mysqlclient source folder, where the C extension expects them.

Locate MariaDB Headers: Find the include folder within your MariaDB Connector/C installation.
Example Path (yours may vary): C:\Program Files\MariaDB\MariaDB Connector C\include

Copy Files: Copy all *.h files from the MariaDB Connector C and place them into the mysqlclient source folder, in  directory: src/mysqldb.

3. Fix Linking Errors (mariadbclient.lib and Symbols)

After fixing the header issue, the compilation might succeed, but the subsequent linking phase will fail. This is typically due to two common errors:

Missing Library File: fatal error LNK1181: cannot open input file 'mariadbclient.lib'
Unresolved Symbols: _mysql.obj : error LNK2001: unresolved external symbol mysql_field_count

Both issues are resolved by ensuring the linker can find the necessary library file (.lib) containing the implemented functions.

Locate MariaDB Libraries: Find the MariaDB Connector C/lib folder.

Copy all (*.lib) files from the selected MariaDB Connector C lib subdirectory and place them into the same mysqlclient source directory: src/mysqldb.

By placing mariadbclient.lib (and associated files) directly in the src/mysqldb folder, the build script will be able to find it and successfully resolve the external symbols like mysql_field_count.

Step 4: Compile and Install
Go back to the cloned mysqlclient directory.
With the necessary header and library files in place, you can now compile and install the package using pip.

Use pip to build the wheel and install it.

```pip install .```

Alternatively, you can build a distributable wheel file (.whl) first:

```pip wheel . ```

or

``` python setup.py bdist_wheel ```

Then install the generated wheel file:

``` pip install ./dist/mysqlclient-*.whl ```

The mysqlclient package should now be successfully installed on your Windows system, ready for use in your Python projects.

## One more time. This should be done ONLY if you the official whl file is not available!