---
description: "Learn more about: Type functions"
title: "Type functions | Microsoft Docs"
ms.date: 5/16/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Type functions

These functions create and manipulate type values.

|Name|Description|
|------------|---------------|
|[Type.AddTableKey](type-addtablekey.md)|Add a key to a table type.|
|[Type.ClosedRecord](type-closedrecord.md)|The given type must be a record type returns a closed version of the given record type (or the same type, if it is already closed)|
|[Type.Facets](type-facets.md) | Returns the facets of a type.|
|[Type.ForFunction](type-forfunction.md)|Creates a function type from the given .|
|[Type.ForRecord](type-forrecord.md)|Returns a Record type from a fields record.|
|[Type.FunctionParameters](type-functionparameters.md)|Returns a record with field values set to the name of the parameters of a function type, and their values set to their corresponding types.|
|[Type.FunctionRequiredParameters](type-functionrequiredparameters.md)|Returns a number indicating the minimum number of parameters required to invoke the a type of function.|
|[Type.FunctionReturn](type-functionreturn.md)|Returns a type returned by a function type.|
|[Type.Is](type-is.md) |Determines if a value of the first type is always compatible with the second type.|
|[Type.IsNullable](type-isnullable.md)|Returns true if a type is a nullable type; otherwise, false.|
|[Type.IsOpenRecord](type-isopenrecord.md)|Returns whether a record type is open.|
|[Type.ListItem](type-listitem.md)|Returns an item type from a list type.|
|[Type.NonNullable](type-nonnullable.md)|Returns the non nullable type from a type.|
|[Type.OpenRecord](type-openrecord.md)|Returns an opened version of a record type, or the same type, if it is already open.|
|[Type.RecordFields](type-recordfields.md)|Returns a record describing the fields of a record type with each field of the returned record type having a corresponding name and a value that is a record of the form `[ Type = type, Optional = logical ]`.|
|[Type.ReplaceFacets](type-replacefacets.md) | Replaces the facets of a type.|
|[Type.ReplaceTableKeys](type-replacetablekeys.md)|Replaces the keys in a table type.|
|[Type.TableColumn](type-tablecolumn.md) | Returns the type of a column in a table.|
|[Type.TableKeys](type-tablekeys.md)|Returns keys from a table type.|
|[Type.TableRow](type-tablerow.md)|Returns a row type from a table type.|
|[Type.TableSchema](type-tableschema.md) | Returns a table containing a description of the columns (i.e. the schema) of the specified table type.|
|[Type.Union](type-union.md) | Returns the union of a list of types.|
