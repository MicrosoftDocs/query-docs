---
description: "Learn more about: Record functions"
title: "Record functions"
ms.date: 6/19/2025
ms.topic: language-reference
ms.custom: "nonautomated-date"
---
# Record functions

These functions create and manipulate record values.
  
## Information

|Name|Description|
|------------|---------------|
|[Record.FieldCount](record-fieldcount.md)|Returns the number of fields in a record.|
|[Record.HasFields](record-hasfields.md)|Returns true if the field name or field names are present in a record.|

## Transformations

|Name|Description|
|------------|---------------|
|[Geography.FromWellKnownText](geography-fromwellknowntext.md)|Translates text representing a geographic value in Well-Known Text (WKT) format into a structured record.|
|[Geography.ToWellKnownText](geography-towellknowntext.md)|Translates a structured geographic point value into its Well-Known Text (WKT) representation.|
|[GeographyPoint.From](geographypoint-from.md)|Creates a record representing a geographic point from parts.|
|[Geometry.FromWellKnownText](geometry-fromwellknowntext.md)|Translates text representing a geometric value in Well-Known Text (WKT) format into a structured record.|
|[Geometry.ToWellKnownText](geometry-towellknowntext.md)|Translates a structured geometric point value into its Well-Known Text (WKT) representation.|
|[GeometryPoint.From](geometrypoint-from.md)|Creates a record representing a geometric point from parts.|
|[Record.AddField](record-addfield.md)|Adds a field from a field name and value.|
|[Record.Combine](record-combine.md)|Combines the records in a list.|
|[Record.RemoveFields](record-removefields.md)|Removes the specified field(s) from the input record.|
|[Record.RenameFields](record-renamefields.md)|Returns a new record that renames the fields specified. The resultant fields will retain their original order. This function supports swapping and chaining field names. However, all target names plus remaining field names must constitute a unique set or an error will occur.|
|[Record.ReorderFields](record-reorderfields.md)|Reorders record fields to match the order of a list of field names.|
|[Record.TransformFields](record-transformfields.md)|Transforms fields by applying transformOperations. For more more information about values supported by transformOperations, go to [Parameter Values](#parameter-values).|

## Selection

|Name|Description|
|------------|---------------|
|[Record.Field](record-field.md)|Returns the value of the given field. This function can be used to dynamically create field lookup syntax for a given record. In that way it is a dynamic version of the record[field] syntax.|
|[Record.FieldNames](record-fieldnames.md)|Returns a list of field names in order of the record's fields.|
|[Record.FieldOrDefault](record-fieldordefault.md)|Returns the value of a field from a record, or the default value if the field does not exist.|
|[Record.FieldValues](record-fieldvalues.md)|Returns a list of field values in order of the record's fields.|
|[Record.SelectFields](record-selectfields.md)|Returns a new record that contains the fields selected from the input record. The original order of the fields is maintained.|

## Serialization

|Name|Description|
|------------|---------------|
|[Record.FromList](record-fromlist.md)|Returns a record given a list of field values and a set of fields.|
|[Record.FromTable](record-fromtable.md)|Returns a record from a table of records containing field names and values.|
|[Record.ToList](record-tolist.md)|Returns a list of values containing the field values of the input record.|
|[Record.ToTable](record-totable.md)|Returns a table of records containing field names and values from an input record.|

## Parameter Values

The following type definitions are used to describe the parameter values that are referenced in the Record functions above.

|Type Definition|Description|
|-|-|
|**MissingField** option|More information: [MissingField.Type](missingfield-type.md)|
|Transform operations|Transform operations can be specified by either of the following values:<br /><br />&#8226;&nbsp;&nbsp;A list value of two items, first item being the field name and the second item being the transformation function applied to that field to produce a new value.<br /><br />&#8226;&nbsp;&nbsp;A list of transformations can be provided by providing a list value, and each item being the list value of 2 items as described above.<br /><br />For examples, go to the description of [Record.TransformFields](record-transformfields.md)|
|Rename operations|Rename operations for a record can be specified as either of:<br /><br />A single rename operation, which is represented by a list of two field names, old and new.<br /><br />For examples, go to the description of [Record.RenameFields](record-renamefields.md).|
