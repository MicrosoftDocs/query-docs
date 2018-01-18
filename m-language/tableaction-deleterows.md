---
title: "TableAction.DeleteRows | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a0c1232c-6919-4a2e-a655-c5da114ecc17
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# TableAction.DeleteRows
<code>TableAction.DeleteRows(<b>table</b> as table) as action</code>  
## About  
Creates an action to delete the rows in <code>table</code>. The action returns a table containing the deleted rows as they appeared in <code>table</code> before the action executed. To delete a subset of the rows in <code>table</code>, use <code>Table.SelectRows</code> to apply a filter to <code>table</code> before using <code>TableAction.DeleteRows</code>. The function raises an evaluation error if <code>table</code> is not updatable. The action raises an execution error if the operation fails.   
  
<b>NOTE:</b> <code>table</code> may be left in a partially updated state if an execution error occurs.  
