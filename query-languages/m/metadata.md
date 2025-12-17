---
description: "Learn more about: Metadata"
title: "Metadata"
ms.topic: language-reference
ms.date: 8/28/2024
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Metadata

**Metadata** is information about a value that is associated with a value. **Metadata** is represented as a record value, called a metadata record. The fields of a **metadata record** can be used to store the metadata for a value. Every value has a metadata record. If the value of the metadata record hasn't been specified, then the metadata record is empty (has no fields). Associating a metadata record with a value doesn't change the value’s behavior in evaluations except for those that explicitly inspect metadata records.

## Metadata records

A metadata record value is associated with a value x using the syntax value meta [record]. For example, the following associates a metadata record with Rating and Tags fields with the text value "Mozart":

```powerquery-m
"Mozart" meta [ Rating = 5,
Tags = {"Classical"} ]
```

A metadata record can be accessed for a value using the [Value.Metadata](value-metadata.md) function. In the following example, the expression in the ComposerRating field accesses the metadata record of the value in the Composer field, and then accesses the Rating field of the metadata record.

```powerquery-m
[  
    Composer = "Mozart" meta [ Rating = 5, Tags = {"Classical"} ],
    ComposerRating = Value.Metadata(Composer)[Rating]   // 5
]  
```

Metadata records aren't preserved when a value is used with an operator or function that constructs a new value. For example, if two text values are concatenated using the &amp; operator, the metadata of the resulting text value is an empty record [].

The standard library functions [Value.RemoveMetadata](value-removemetadata.md) and [Value.ReplaceMetadata](value-replacemetadata.md) can be used to remove all metadata from a value and to replace a value's metadata.

## Limitations

Some hosts that use Power Query to transform or move data don't support storing custom metadata into storage. The following hosts don't support storing the custom metadata:

* Power BI dataflows
* Fabric Dataflow Gen2
* Power Platform dataflows
