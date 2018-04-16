---
title: "Record functions | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record functions
 
  
## <a name="__toc360789143"></a>Record  
  
### <a name="__toc360789144"></a>Information  
  
|Function|Description|  
|------------|---------------|  
|[Record.FieldCount](record-fieldcount.md)|Returns the number of fields in a record.|  
|[Record.HasFields](record-hasfields.md)|Returns true if the field name or field names are present in a record.|  
  
### <a name="__toc360789151"></a>Transformations  
  
|Function|Description|  
|------------|---------------|  
|[Record.AddField](record-addfield.md)|Adds a field from a field name and value.|  
|[Record.Combine](record-combine.md)|Combines the records in a list.|  
|[Record.RemoveFields](record-removefields.md)|Returns a new record that reorders the given fields with respect to each other. Any fields not specified remain in their original locations.|
|[Record.RenameFields](record-renamefields.md)|Returns a new record that renames the fields specified. The resultant fields will retain their original order. This function supports swapping and chaining field names. However, all target names plus remaining field names must constitute a unique set or an error will occur.|
|[Record.ReorderFields](record-reorderfields.md)|Returns a new record that reorders fields relative to each other. Any fields not specified remain in their original locations. Requires two or more fields.|  
|[Record.TransformFields](record-transformfields.md)|Transforms fields by applying transformOperations. For more more information about values supported by transformOperations, see Parameter Values.|
  
### <a name="__toc360789172"></a>Selection  
  
|Function|Description|  
|------------|---------------|  
|[Record.Field](record-field.md)|Returns the value of the given field. This function can be used to dynamically create field lookup syntax for a given record. In that way it is a dynamic verison of the record[field] syntax.|  
|[Record.FieldNames](record-fieldnames.md)|Returns a list of field names in order of the record's fields.|
|[Record.FieldOrDefault](record-fieldordefault.md)|Returns the value of a field from a record, or the default value if the field does not exist.|
|[Record.FieldValues](record-fieldvalues.md)|Returns a list of field values in order of the record's fields.|  
|[Record.SelectFields](record-selectfields.md)|Returns a new record that contains the fields selected from the input record. The original order of the fields is maintained.|  
  
### <a name="__toc286150819"></a>Serialization  
  
|Function|Description|  
|------------|---------------|  
|[Record.FromList](record-fromlist.md)|Returns a record given a list of field values and a set of fields.|
|[Record.FromTable](record-fromtable.md)|Returns a record from a table of records containing field names and values.|
|[Record.ToList](record-tolist.md)|Returns a list of values containing the field values of the input record.|
|[Record.ToTable](record-totable.md)|Returns a table of records containing field names and values from an input record.|
  
  
  
### Parameter Values  
The following type definitions are used to describe the parameter values that are referenced in Record functions above.  
  
|||  
|-|-|  
|MissingField option|MissingField.Error = 0;<br /><br />MissingField.Ignore = 1;<br /><br />MissingField.UseNull = 2;|  
|Transform operations|Transform operations can be specified by either of the following values:<br /><br />A list value of two items, first item being the field name and the second item being the transformation function applied to that field to produce a new value.<br /><br />A list of transformations can be provided by providing a list value, and each item being the list value of 2 items as described above.<br /><br />For examples, see description of [Record.TransformFields](record-transformfields.md)|  
|Rename operations|Rename operations for a record can be specified as either of:<br /><br />A single rename operation, which is represented by a list of two field names, old and new.<br /><br /><br /><br />For examples, see description of [Record.RenameFields](record-renamefields.md).|  
  
