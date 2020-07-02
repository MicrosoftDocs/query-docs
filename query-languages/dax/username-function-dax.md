---
title: "USERNAME function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# USERNAME

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
=IF(CONTAINS(UsersTable,UsersTable[login], USERNAME()), "Allowed", BLANK())  
```
