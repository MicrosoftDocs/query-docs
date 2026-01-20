---
description: "Learn more about: Text functions"
title: "Text functions"
ms.date: 6/9/2025
ms.topic: language-reference
ms.custom: "nonautomated-date"
---
# Text functions

These functions create and manipulate text values.

## Information

|Name|Description|
|------------|---------------|
|[Text.InferNumberType](text-infernumbertype.md)|Infers the granular number type (`Int64.Type`, `Double.Type`, and so on) of a number encoded in text.|
|[Text.Length](text-length.md)|Returns the number of characters in a text value.|

## Text Comparisons

|Name|Description|
|------------|---------------|
|[Character.FromNumber](character-fromnumber.md)|Converts a number to a text character.|
|[Character.ToNumber](character-tonumber.md)|Converts a character to a number value.|
|[Guid.From](guid-from.md) | Returns a GUID value from the given value.|
|[Json.FromValue](json-fromvalue.md) | Produces a JSON representation of a given value.|
|[Text.From](text-from.md)|Creates a text value from the given value.|
|[Text.FromBinary](text-frombinary.md)|Decodes data from a binary value in to a text value using an encoding.|
|[Text.NewGuid](text-newguid.md)|Returns a GUID value as a text value.|
|[Text.ToBinary](text-tobinary.md)|Encodes a text value into binary value using an encoding.|
|[Text.ToList](text-tolist.md)|Returns a list of characters from a text value.|
|[Value.FromText](value-fromtext.md)|Creates a strongly-typed value from a textual representation.|

## Extraction

|Name|Description|
|------------|---------------|  
|[Text.At](text-at.md)|Returns a character starting at a zero-based offset.|
|[Text.Middle](text-middle.md) | Returns the substring up to a specific length.|
|[Text.Range](text-range.md)|Returns a number of characters from a text value starting at a zero-based offset and for count number of characters.|
|[Text.Start](text-start.md)|Returns the count of characters from the start of a text value.|
|[Text.End](text-end.md)|Returns the number of characters from the end of a text value.|

## Modification

|Name|Description|
|------------|---------------|
|[Text.Insert](text-insert.md)|Inserts one text value into another at a given position.|
|[Text.Remove](text-remove.md)|Removes all occurrences of the given character or list of characters from the input text value.|
|[Text.RemoveRange](text-removerange.md)|Removes count characters at a zero-based offset from a text value.|
|[Text.Replace](text-replace.md)|Replaces all occurrences of a substring with a new text value.|
|[Text.ReplaceRange](text-replacerange.md)|Replaces length characters in a text value starting at a zero-based offset with the new text value.|
[Text.Select](text-select.md) | Selects all occurrences of the given character or list of characters from the input text value.|

## Membership

|Name|Description|
|------------|---------------|
|[Text.Contains](text-contains.md)|Returns `true` if a text value substring was found within a text value string; otherwise, `false`.|
|[Text.EndsWith](text-endswith.md)|Returns a logical value indicating whether a text value substring was found at the end of a string.|
|[Text.PositionOf](text-positionof.md)|Returns the first position of the value (-1 if not found).|
|[Text.PositionOfAny](text-positionofany.md)|Returns the first position in the text value of any listed character (-1 if not found).|
|[Text.StartsWith](text-startswith.md)|Returns a logical value indicating whether a text value substring was found at the beginning of a string.|

## Transformations

|Name|Description|
|------------|---------------|
|[Text.AfterDelimiter](text-afterdelimiter.md)|Returns the portion of text after the specified delimiter.|
|[Text.BeforeDelimiter](text-beforedelimiter.md)|Returns the portion of text before the specified delimiter.|
|[Text.BetweenDelimiters](text-betweendelimiters.md)|Returns the portion of text between the specified `startDelimiter` and `endDelimiter`.|
|[Text.Clean](text-clean.md)|Returns the original text value with non-printable characters removed.|
|[Text.Combine](text-combine.md)|Returns a text value that is the result of joining all text values with each value separated by a separator.|
|[Text.Lower](text-lower.md)|Returns the lowercase of a text value.|
|[Text.PadEnd](text-padend.md)|Returns text of a specified length by padding the end of the given text.|
|[Text.PadStart](text-padstart.md)|Returns text of a specified length by padding the start of the given text.|
|[Text.Proper](text-proper.md)|Returns a text value with first letters of all words converted to uppercase.|
|[Text.Repeat](text-repeat.md)|Returns a text value composed of the input text value repeated a number of times.|
|[Text.Reverse](text-reverse.md)|Reverses the provided text.|
|[Text.Split](text-split.md)|Returns a list containing parts of a text value that are delimited by a separator text value.|
|[Text.SplitAny](text-splitany.md)|Returns a list containing parts of a text value that are delimited by any separator text values.|
|[Text.Trim](text-trim.md)|Removes all the specified leading and trailing characters.|
|[Text.TrimEnd](text-trimend.md)|Removes all specified trailing characters.|
|[Text.TrimStart](text-trimstart.md)|Removes all specified leading characters.|
|[Text.Upper](text-upper.md)|Returns the uppercase of a text value.|
