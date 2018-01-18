---
title: "Value functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 9a16c827-8733-441e-ad4e-6912ef407e22
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360789732"></a>Values  
  
|Function|Description|  
|------------|---------------|  
|[Value.Compare](../PowerQuery/value-compare.md)|Returns 1, 0, or -1 based on value1 being greater than, equal to, or less than the value2. An optional comparer function can be provided.|  
|[Value.Equals](../PowerQuery/value-equals.md)|Returns whether two values are equal.|  
|[Value.NativeQuery](../PowerQuery/value-nativequery.md) | Evaluates a query against a target.|
|[Value.NullableEquals](../PowerQuery/value-nullableequals.md)|Returns a logical value or null based on two values .| 
|[Value.Type](../PowerQuery/value-type.md) | Returns the type of the given value.| 
  
### <a name="__toc360789742"></a>Arithmetic operations  
  
|Function|Description|  
|------------|---------------|  
|[Value.Add](../PowerQuery/value-add.md)|Returns the sum of the two values.|  
|[Value.Divide](../PowerQuery/value-divide.md)|Returns the result of dividing the first value by the second.|
|[Value.Multiply](../PowerQuery/value-multiply.md)|Returns the product of the two values.|
|[Value.Subtract](../PowerQuery/value-subtract.md)|Returns the difference of the two values.|  
   
  
### <a name="__toc360789751"></a>Parameter types  
  
|Type|Description|  
|--------|---------------|  
|[Value.As](../PowerQuery/value-as.md)|Value.As is the function corresponding to the as operator in the formula language. The expression value as type asserts that the value of a value argument is compatible with type as per the is operator. If it is not compatible, an error is raised.|  
|[Value.Is](../PowerQuery/value-is.md)|Value.Is is the function corresponding to the is operator in the formula language. The expression value is type returns true if the ascribed type of vlaue is compatible with type, and returns false if the ascribed type of value is incompatible with type.|  
|[Value.ReplaceType](../PowerQuery/value-replacetype.md)|A value may be ascribed a type using Value.ReplaceType. Value.ReplaceType either returns a new value with the type ascribed or raises an error if the new type is incompatible with the value?s native primitive type. In particular, the function raises an error when an attempt is made to ascribe an abstract type, such as any. When replacing a the type of a record, the new type must have the same number of fields, and the new fields replace the old fields by ordinal position, not by name. Similarly, when replacing the type of a table, the new type must have the same number of columns, and the new columns replace the old columns by ordinal position.|  

Implementation | Description
-------------- | -----------
[DirectQueryCapabilities.From](../PowerQuery/directquerycapabilities-from.md) | DirectQueryCapabilities.From
[Embedded.Value](../PowerQuery/embedded-value.md) | Accesses a value by name in an embedded mashup.
[Value.Firewall](../PowerQuery/value-firewall.md) | Value.Firewall
[Variable.Value](../PowerQuery/variable-value.md) | Variable.Value
[SqlExpression.SchemaFrom](../PowerQuery/sqlexpression-schemafrom.md) | SqlExpression.SchemaFrom
[SqlExpression.ToExpression](../PowerQuery/sqlexpression-toexpression.md) | SqlExpression.ToExpression  

  
## <a name="__toc360789761"></a>Metadata  
  
|Function|Description|  
|------------|---------------|  
|[Value.Metadata](../PowerQuery/value-metadata.md)|Returns a record containing the input?s metadata.|  
|[Value.RemoveMetadata](../PowerQuery/value-removemetadata.md)|Removes the metadata on the value and returns the original value.|  
|[Value.ReplaceMetadata](../PowerQuery/value-replacemetadata.md)|Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.|  
  
