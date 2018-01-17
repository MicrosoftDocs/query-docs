---
title: "Type functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 4370001c-a0a9-497e-b97c-7d5449fc3824
caps.latest.revision: 11
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360789953"></a>Type  
  
|Function|Description|  
|------------|---------------|  
|[Type.AddTableKey](../PowerQuery/type-addtablekey.md)|Add a key to a table type.|  
|[Type.ClosedRecord](../PowerQuery/type-closedrecord.md)|The given type must be a record type returns a closed version of the given record type (or the same type, if it is already closed)|  
|[Type.Facets](../PowerQuery/type-facets.md) | Returns the facets of a type.|
|[Type.ForFunction](../PowerQuery/type-forfunction.md)|Creates a function type from the given .|  
|[Type.ForRecord](../PowerQuery/type-forrecord.md)|Returns a Record type from a fields record.|  
|[Type.FunctionParameters](../PowerQuery/type-functionparameters.md)|Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.|  
|[Type.FunctionRequiredParameters](../PowerQuery/type-functionrequiredparameters.md)|Returns a number indicating the minimum number of parameters required to invoke the a type of function.|  
|[Type.FunctionReturn](../PowerQuery/type-functionreturn.md)|Returns a type returned by a function type.|  
|[Type.Is](../PowerQuery/type-is.md) | Type.Is |
|[Type.IsNullable](../PowerQuery/type-isnullable.md)|Returns true if a type is a nullable type; otherwise, false.|  
|[Type.IsOpenRecord](../PowerQuery/type-isopenrecord.md)|Returns whether a record type is open.|  
|[Type.ListItem](../PowerQuery/type-listitem.md)|Returns an item type from a list type.|  
|[Type.NonNullable](../PowerQuery/type-nonnullable.md)|Returns the non nullable type from a type.|  
|[Type.OpenRecord](../PowerQuery/type-openrecord.md)|Returns an opened version of a record type, or the same type, if it is already open.|  
|[Type.RecordFields](../PowerQuery/type-recordfields.md)|Returns a record describing the fields of a record type with each field of the returned record type having a corresponding name and a value that is a record of the form [ Type = type, Opional = logical ].|  
|[Type.ReplaceFacets](../PowerQuery/type-replacefacets.md) | Replaces the facets of a type.|
|[Type.ReplaceTableKeys](../PowerQuery/type-replacetablekeys.md)|Replaces the keys in a table type.|  
|[Type.TableColumn](../PowerQuery/type-tablecolumn.md) | Returns the type of a column in a table.|
|[Type.TableKeys](../PowerQuery/type-tablekeys.md)|Returns keys from a table type.|  
|[Type.TableRow](../PowerQuery/type-tablerow.md)|Returns a row type from a table type.|
|[Type.TableSchema](../PowerQuery/type-tableschema.md) | Returns a table containing a description of the columns (i.e. the schema) of the specified table type.|  
|[Type.Union](../PowerQuery/type-union.md) | Returns the union of a list of types.| 
