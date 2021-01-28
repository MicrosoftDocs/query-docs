---
description: "Learn more about: Value functions"
title: "Value functions | Microsoft Docs"
ms.date: 4/7/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Value functions

These functions evaluate and perform operations on values.
  
## <a name="__toc360789732"></a>Values  
  
|Function|Description|  
|------------|---------------|
|[Value.Alternate](value-alternate.md)|Expresses alternate query plans.|
|[Value.Compare](value-compare.md)|Returns 1, 0, or -1 based on value1 being greater than, equal to, or less than the value2. An optional comparer function can be provided.|  
|[Value.Equals](value-equals.md)|Returns whether two values are equal.|  
|[Value.Expression](value-expression.md)|Returns an AST that represents the value's expression.|
|[Value.NativeQuery](value-nativequery.md) | Evaluates a query against a target.|
|[Value.NullableEquals](value-nullableequals.md)|Returns a logical value or null based on two values .| 
|[Value.Optimize](value-optimize.md)|If value represents a query that can be optimized, returns the optimized query. Otherwise returns value.
|[Value.Type](value-type.md) | Returns the type of the given value.| 
  
### <a name="__toc360789742"></a>Arithmetic operations  
  
|Function|Description|  
|------------|---------------|  
|[Value.Add](value-add.md)|Returns the sum of the two values.|  
|[Value.Divide](value-divide.md)|Returns the result of dividing the first value by the second.|
|[Value.Multiply](value-multiply.md)|Returns the product of the two values.|
|[Value.Subtract](value-subtract.md)|Returns the difference of the two values.|  

### Arithmetic parameters

|Function|Description|  
|------------|---------------|  
|[Precision.Double](precision-double.md)|An optional parameter for the built-in arthimetic operators to specify double precision.|  
|[Precision.Decimal](precision-decimal.md)|An optional parameter for the built-in arthimetic operators to specify decimal precision.|
   
  
### <a name="__toc360789751"></a>Parameter types  
  
|Type|Description|  
|--------|---------------|  
|[Value.As](value-as.md)|Value.As is the function corresponding to the as operator in the formula language. The expression value as type asserts that the value of a value argument is compatible with type as per the is operator. If it is not compatible, an error is raised.|  
|[Value.Is](value-is.md)|Value.Is is the function corresponding to the is operator in the formula language. The expression value is type returns true if the ascribed type of vlaue is compatible with type, and returns false if the ascribed type of value is incompatible with type.|  
|[Value.ReplaceType](value-replacetype.md)|A value may be ascribed a type using Value.ReplaceType. Value.ReplaceType either returns a new value with the type ascribed or raises an error if the new type is incompatible with the value’s native primitive type. In particular, the function raises an error when an attempt is made to ascribe an abstract type, such as any. When replacing a the type of a record, the new type must have the same number of fields, and the new fields replace the old fields by ordinal position, not by name. Similarly, when replacing the type of a table, the new type must have the same number of columns, and the new columns replace the old columns by ordinal position.|  

Implementation | Description
-------------- | -----------
[DirectQueryCapabilities.From](directquerycapabilities-from.md) | DirectQueryCapabilities.From
[Embedded.Value](embedded-value.md) | Accesses a value by name in an embedded mashup.
[Value.Firewall](value-firewall.md) | Value.Firewall
[Variable.Value](variable-value.md) | Variable.Value
[SqlExpression.SchemaFrom](sqlexpression-schemafrom.md) | SqlExpression.SchemaFrom
[SqlExpression.ToExpression](sqlexpression-toexpression.md) | SqlExpression.ToExpression  

  
## <a name="__toc360789761"></a>Metadata  
  
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
  
