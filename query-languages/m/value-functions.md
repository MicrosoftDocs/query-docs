---
description: "Learn more about: Value functions"
title: "Value functions"
ms.date: 7/16/2025
ms.custom: "nonautomated-date"
---
# Value functions

These functions evaluate and perform operations on values.

|Name|Description|
|------------|---------------|
|[Value.Alternates](value-alternates.md)|Expresses alternate query plans.|
|[Value.Compare](value-compare.md)|Returns -1, 0, or 1 based on whether the first value is less than, equal to, or greater than the second.|
|[Value.Equals](value-equals.md)|Returns whether two values are equal.|
|[Value.Expression](value-expression.md)|Returns an abstract syntax tree (AST) that represents the value's expression.|
|[Value.VersionIdentity](value-versionidentity.md)|Returns the version identity of a value.|
|[Value.Versions](value-versions.md)|Returns a navigation table containing the available versions of a value.|
|[Value.NativeQuery](value-nativequery.md) | Evaluates a query against a target.|
|[Value.NullableEquals](value-nullableequals.md)|Returns a logical value or null based on two values.|
|[Value.Optimize](value-optimize.md)|If value represents a query that can be optimized, returns the optimized query. Otherwise returns value.|
|[Value.Type](value-type.md) | Returns the type of the given value.|

## Arithmetic operations

|Name|Description|
|------------|---------------|
|[Value.Add](value-add.md)|Returns the sum of the two values.|
|[Value.Divide](value-divide.md)|Returns the result of dividing the first value by the second.|
|[Value.Multiply](value-multiply.md)|Returns the product of the two values.|
|[Value.Subtract](value-subtract.md)|Returns the difference of the two values.|

## Parameter types

|Name|Description|
|--------|---------------|
|[Value.As](value-as.md)|Returns the value if it is compatible with the specified type.|
|[Value.Is](value-is.md)|Determines whether a value is compatible with the specified type.|
|[Value.ReplaceType](value-replacetype.md)|Replaces the value's type.|

|Implementation | Description |
|-------------- | ----------- |
|[Action.WithErrorContext](action-witherrorcontext.md) | This function is intended for internal use only.|
|[DirectQueryCapabilities.From](directquerycapabilities-from.md) | This function is intended for internal use only.|
|[Embedded.Value](embedded-value.md) | Accesses a value by name in an embedded mashup.|
|[Excel.ShapeTable](excel-shapetable.md) | This function is intended for internal use only.|
|[Module.Versions](module-versions.md) | Returns a record of module versions for the current module and its dependencies.|
|[Progress.DataSourceProgress](progress-datasourceprogress.md) | This function is intended for internal use only. |
|[SqlExpression.SchemaFrom](sqlexpression-schemafrom.md) | This function is intended for internal use only.|
|[SqlExpression.ToExpression](sqlexpression-toexpression.md) | This function is intended for internal use only.|
|[Value.Firewall](value-firewall.md) | This function is intended for internal use only.|
|[Value.ViewError](value-viewerror.md) | This function is intended for internal use only.|
|[Value.ViewFunction](value-viewfunction.md) | This function is intended for internal use only.|
|[Variable.Value](variable-value.md) | Returns the value of the specified identifier, or an error if the identifier is not defined.|
|[Variable.ValueOrDefault](variable-valueordefault.md) | Returns the value of the specified identifier, or the optional default value if the identifier is not defined.|

## Metadata

|Name|Description|
|------------|---------------|
|[Value.Metadata](value-metadata.md)|Returns a record containing the input’s metadata.|
|[Value.RemoveMetadata](value-removemetadata.md)|Removes the metadata on the value and returns the original value.|
|[Value.ReplaceMetadata](value-replacemetadata.md)|Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.|

## Lineage

|Name|Description|
| ------ | --------- |
|[Graph.Nodes](graph-nodes.md)|This function is intended for internal use only.|
|[Value.Lineage](value-lineage.md)|This function is intended for internal use only.|
|[Value.Traits](value-traits.md)|This function is intended for internal use only.|
  