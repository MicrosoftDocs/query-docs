---
description: "Learn more about: PATH"
title: "PATH function (DAX) | Microsoft Docs"
---
# PATH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a delimited text string with the identifiers of all the parents of the current identifier, starting with the oldest and continuing until current.  
  
## Syntax  
  
```dax
PATH(<ID_columnName>, <parent_columnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|  ID_columnName  |  The name of an existing column containing the unique identifier for rows in the table. This cannot be an expression. The data type of the value in *ID_columnName* must be text or integer, and must also be the same data type as the column referenced in *parent_columnName*.|  
| parent_columnName | The name of an existing column containing the unique identifier for the parent of the current row. This cannot be an expression. The data type of the value in *parent_columnName* data type must be text or integer, and must be the same data type as the value in *ID_columnName*.   |
  
## Return value

A delimited text string containing the identifiers of all the parents to the current identifier.  
  
## Remarks

- This function is used in tables that have some kind of internal hierarchy, to return the items that are related to the current row value. For example, in an Employees table that contains employees, the managers of employees, and the managers of the managers, you can return the path that connects an employee to his or her manager.  
  
- The path is not constrained to a single level of parent-child relationships; it can return related rows that are several levels up from the specified starting row.  
  - The delimiter used to separate the ascendants is the vertical bar, '|'.  
  - The values in *ID_columnName* and *parent_columnName* must have the same data type, text or integer.  
  - Values in *parent_columnName* must be present in *ID_columnName*. That is, you cannot look up a parent if there is no value at the child level.  
  - If *parent_columnName* is BLANK then PATH() returns *ID_columnName* value.  In other words, if you look for the manager of an employee but the *parent_columnName* column has no data, the PATH function returns just the employee ID.  
  - If *ID_columnName* has duplicates and *parent_columnName* is the same for those duplicates then PATH() returns the common *parent_columnName* value; however, if *parent_columnName* value is different for those duplicates then PATH() returns an error. In other words, if you have two listings for the same employee ID and they have the same manager ID, the PATH function returns the ID for that manager. However, if there are two identical employee IDs that have different manager IDs, the PATH function returns an error.  
  - If *ID_columnName* is BLANK then PATH() returns BLANK.  
  - If *ID_columnName* contains a vertical bar '|' then PATH() returns an error.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example

The following example creates a calculated column that lists all the managers for each employee.  
  
```dax
= PATH(Employee[EmployeeKey], Employee[ParentEmployeeKey])  
```
