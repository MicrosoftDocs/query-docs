---
title: "USERNAME Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# USERNAME Function (DAX)
Returns the domain name and username from the credentials given to the system at connection time  
  
## Syntax  
  
```  
USERNAME()  
```  
  
#### Parameters  
  
## Return Value  
The username from the credentials given to the system at connection time  
  
  
## Example  
The following code verifies if the user login is part of the UsersTable.  
  
```  
=IF(CONTAINS(UsersTable,UsersTable[login], USERNAME()), "Allowed", BLANK())  
```  
