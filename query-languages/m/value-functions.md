---
description: "Learn more about: Value functions"
title: "Value functions | Microsoft Docs"
ms.date: 5/12/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Value functions

These functions evaluate and perform operations on values.

|Function|Description|
|------------|---------------|
|[Value.Alternates](value-alternate.md)|Expresses alternate query plans.|
|[Value.Compare](value-compare.md)|Returns 1, 0, or -1 based on value1 being greater than, equal to, or less than the value2. An optional comparer function can be provided.|
|[Value.Equals](value-equals.md)|Returns whether two values are equal.|
|[Value.Expression](value-expression.md)|Returns an abstract syntax tree (AST) that represents the value's expression.|
|[Value.NativeQuery](value-nativequery.md) | Evaluates a query against a target.|
|[Value.NullableEquals](value-nullableequals.md)|Returns a logical value or null based on two values .|
|[Value.Optimize](value-optimize.md)|If value represents a query that can be optimized, returns the optimized query. Otherwise returns value.
|[Value.Type](value-type.md) | Returns the type of the given value.|

## Arithmetic operations

|Function|Description|
|------------|---------------|
|[Value.Add](value-add.md)|Returns the sum of the two values.|
|[Value.Divide](value-divide.md)|Returns the result of dividing the first value by the second.|
|[Value.Multiply](value-multiply.md)|Returns the product of the two values.|
|[Value.Subtract](value-subtract.md)|Returns the difference of the two values.|

## Parameter types

|Type|Description|
|--------|---------------|
|[Value.As](value-as.md)|Returns the value if it is compatible with the specified type.|
|[Value.Is](value-is.md)|Determines whether a value is compatible with the specified type.|
|[Value.ReplaceType](value-replacetype.md)|Replaces the value's type.|

|Implementation | Description
|-------------- | -----------
|[DirectQueryCapabilities.From](directquerycapabilities-from.md) | This function is intended for internal use only.|
|[Embedded.Value](embedded-value.md) | Accesses a value by name in an embedded mashup.|
|[Excel.ShapeTable](excel-shapetable.md) | This function is intended for internal use only.|
|[Value.Firewall](value-firewall.md) | This function is intended for internal use only.|
|[Variable.Value](variable-value.md) | This function is intended for internal use only.|
|[SqlExpression.SchemaFrom](sqlexpression-schemafrom.md) | This function is intended for internal use only.|
|[SqlExpression.ToExpression](sqlexpression-toexpression.md) | This function is intended for internal use only.|

## Metadata

|Function|Description|
|------------|---------------|
|[Value.Metadata](value-metadata.md)|Returns a record containing the input’s metadata.|
|[Value.RemoveMetadata](value-removemetadata.md)|Removes the metadata on the value and returns the original value.|
|[Value.ReplaceMetadata](value-replacemetadata.md)|Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.|

## Lineage

|Function|Description|
| ------ | --------- |
|[Graph.Nodes](graph-nodes.md)|This function is intended for internal use only.|
|[Value.Lineage](value-lineage.md)|This function is intended for internal use only.|
|[Value.Traits](value-traits.md)|This function is intended for internal use only.|
  