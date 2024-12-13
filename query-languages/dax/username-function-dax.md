---
description: "Learn more about: USERNAME"
title: "USERNAME function (DAX)"
---
# USERNAME

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the domain name and username from the credentials given to the system at connection time.  
  
## Syntax  
  
```dax
USERNAME()  
```
  
### Parameters  

This expression has no parameters.
  
## Return value

The username from the credentials given to the system at connection time  
  
## Example

The following formula verifies if the user login is part of the UsersTable.  
  
```dax
= IF(CONTAINS(UsersTable,UsersTable[login], USERNAME()), "Allowed", BLANK())  
```
