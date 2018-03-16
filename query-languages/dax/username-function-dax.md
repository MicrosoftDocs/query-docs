---
title: "USERNAME Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql.as.daxref.USERNAME.f1"
ms.assetid: 22dddc4b-1648-4c89-8c93-f1151162b93f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
