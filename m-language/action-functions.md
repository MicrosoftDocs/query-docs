---
title: "Action functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 3475f7c7-8339-4d7a-8f7d-b88e4826c292
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Action functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## Action  
  
### <a name="__toc360788690"></a>Constants  
  
|Action|Description|  
|------------|---------------|  
|[Action.Donothing](../PowerQuery/action-donothing.md)|An action that performs no action when executed and returns <code>null</code> as its result.|  
|[Action.Return](../PowerQuery/action-return.md)|Creates an action that performs no action when executed and returns <code>value</code> as its result.|
|[Action.Sequence](../PowerQuery/action-sequence.md)|Creates an action that executes the sequence of elements in actions in order.|  
|[Action.Try](../PowerQuery/action-try.md)|Creates an action that executes action, catches any errors that occur while executing the action, and returns a record containing a HasError field and either a Value or Error field depending on whether the action executed successfully.|  
|[TableAction.DeleteRows](../PowerQuery/tableaction-deleterows.md)|Creates an action to delete rows from a table.|
|[TableAction.InsertRows](../PowerQuery/tableaction-insertrows.md)|Creates an action to insert rows into a table.|
|[TableAction.UpdateRows](../PowerQuery/tableaction-updaterows.md)|Creates an action to update rows in a table.|
|[ValueAction.NativeStatement](../PowerQuery/valueaction-nativestatement.md)|Creates an action to execute a statement against a target.|
|[ValueAction.Replace](../PowerQuery/valueaction-replace.md)|Creates an action that replaces the content of a value with the specified value.|
|[WebAction.Request](../PowerQuery/webaction-request.md)|Creates an action that, when executed, will return the results of performing an HTTP request as a binary value.|


