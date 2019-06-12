---
title: "Text functions | Microsoft Docs"
ms.date: 6/13/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text functions
 
  
## Text  

### <a name="__toc360788809"></a>Information  
  
|Function|Description|  
|------------|---------------|  
|[Text.InferNumberType](text-infernumbertype.md)|Infers granular number type (Int64.Type, Double.Type, etc.) of `text` using `culture`.|  
|[Text.Length](text-length.md)|Returns the number of characters in a text value.|  
  
### <a name="__toc360788813"></a>Text Comparisons  
  
|Function|Description|  
|------------|---------------|  
|[Character.FromNumber](character-fromnumber.md)|Returns a number to its character value.|  
|[Character.ToNumber](character-tonumber.md)|Returns a character to its number value.|  
[Guid.From](guid-from.md) | Returns a `Guid.Type` value from the given `value`.
|[Json.FromValue](json-fromvalue.md) | Produces a JSON representation of a given value.|
|[Text.From](text-from.md)|Returns the text representation of a number, date, time, datetime, datetimezone, logical, duration or binary value. If a value is null, Text.From returns null. The optional culture parameter is used to format the text value according to the given culture.|  
|[Text.FromBinary](text-frombinary.md)|Decodes data from a binary value in to a text value using an encoding.|  
|[Text.NewGuid](text-newguid.md)|Returns a Guid value as a text value.|  
|[Text.ToBinary](text-tobinary.md)|Encodes a text value into binary value using an encoding.|  
|[Text.ToList](text-tolist.md)|Returns a list of characters from a text value.|  
|[Value.FromText](value-fromtext.md)|Decodes a value from a textual representation, value, and interprets it as a value with an appropriate type. Value.FromText takes a text value and returns a number, a logical value, a null value, a DateTime value, a Duration value, or a text value. The empty text value is interpreted as a null value.|  
  
### <a name="__toc360788837"></a>Extraction  
  
|Function|Description|  
|------------|---------------|  
|[Text.At](text-at.md)|Returns a character starting at a zero-based offset.| 
|[Text.Middle](text-middle.md) | Returns the substring up to a specific length.|
|[Text.Range](text-range.md)|Returns a number of characters from a text value starting at a zero-based offset and for count number of characters.|  
|[Text.Start](text-start.md)|Returns the count of characters from the start of a text value.|  
  
|Function|Description|  
|------------|---------------|  
|[Text.End](text-end.md)|Returns the number of characters from the end of a text value.|  
  
### <a name="__toc360788852"></a>Modification  
  
|Function|Description|  
|------------|---------------|  
|[Text.Insert](text-insert.md)|Returns a text value with newValue inserted into a text value starting at a zero-based offset.|  
|[Text.Remove](text-remove.md)|Removes all occurrences of a character or list of characters from a text value. The removeChars parameter can be a character value or a list of character values.|  
|[Text.RemoveRange](text-removerange.md)|Removes count characters at a zero-based offset from a text value.|  
|[Text.Replace](text-replace.md)|Replaces all occurrences of a substring with a new text value.|  
|[Text.ReplaceRange](text-replacerange.md)|Replaces length characters in a text value starting at a zero-based offset with the new text value.| 
[Text.Select](text-select.md) | Selects all occurrences of the given character or list of characters from the input text value.| 
  
### <a name="__toc360788870"></a>Membership  
  
|Function|Description|  
|------------|---------------|  
|[Text.Contains](text-contains.md)|Returns true if a text value substring was found within a text value string; otherwise, false.|  
|[Text.EndsWith](text-endswith.md)|Returns a logical value indicating whether a text value substring was found at the end of a string.|  
|[Text.PositionOf](text-positionof.md)|Returns the first occurrence of substring in a string and returns its position starting at startOffset.|  
|[Text.PositionOfAny](text-positionofany.md)|Returns the first occurrence of a text value in list and returns its position starting at startOffset.|  
|[Text.StartsWith](text-startswith.md)|Returns a logical value indicating whether a text value substring was found at the beginning of a string.|  
  
### <a name="__toc360788887"></a>Transformations  
  
|Function|Description|  
|------------|---------------|  
|[Text.AfterDelimiter](text-afterdelimiter.md)|Returns the portion of text after the specified delimiter.| 
|[Text.BeforeDelimiter](text-beforedelimiter.md)|Returns the portion of text before the specified delimiter.|
|[Text.BetweenDelimiters](text-betweendelimiters.md)|Returns the portion of text between the specified startDelimiter and endDelimiter.|
|[Text.Clean](text-clean.md)|Returns the original text value with non-printable characters removed.|  
|[Text.Combine](text-combine.md)|Returns a text value that is the result of joining all text values with each value separated by a separator.|  
|[Text.Lower](text-lower.md)|Returns the lowercase of a text value.|  
|[Text.PadEnd](text-padend.md)|Returns a text value padded at the end with pad to make it at least length characters.|  
|[Text.PadStart](text-padstart.md)|Returns a text value padded at the beginning with pad to make it at least length characters. If pad is not specified, whitespace is used as pad.|  
|[Text.Proper](text-proper.md)|Returns a text value with first letters of all words converted to uppercase.|  
|[Text.Repeat](text-repeat.md)|Returns a text value composed of the input text value repeated a number of times.|  
|[Text.Reverse](text-reverse.md)|Reverses the provided text.|  
|[Text.Split](text-split.md)|Returns a list containing parts of a text value that are delimited by a separator text value.|  
|[Text.SplitAny](text-splitany.md)|Returns a list containing parts of a text value that are delimited by any separator text values.|  
|[Text.Trim](text-trim.md)|Removes any occurrences of characters in trimChars from text.|  
|[Text.TrimEnd](text-trimend.md)|Removes any occurrences of the characters specified in trimChars from the end of the original text value.|  
|[Text.TrimStart](text-trimstart.md)|Removes any occurrences of the characters in trimChars from the start of the original text value.|  
|[Text.Upper](text-upper.md)|Returns the uppercase of a text value.|  
  
### Parameters
|Parameter values |Description|  
|------------|---------------| 
|[Occurrence.All](occurrence-all.md) | A list of positions of all occurrences of the found values is returned.|
|[Occurrence.First](occurrence-first.md) | The position of the first occurrence of the found value is returned.|
|[Occurrence.Last](occurrence-last.md) | The position of the last occurrence of the found value is returned.| 
|[RelativePosition.FromEnd](relativeposition-fromend.md) | Indicates indexing should be done from the end of the input.|
|[RelativePosition.FromStart](relativeposition-fromstart.md) | Indicates indexing should be done from the start of the input.|
|[TextEncoding.Ascii](textencoding-ascii.md) | Use to choose the ASCII binary form.|
|[TextEncoding.BigEndianUnicode](textencoding-bigendianunicode.md) | Use to choose the UTF16 big endian binary form.|
|[TextEncoding.Unicode](textencoding-unicode.md) | Use to choose the UTF16 little endian binary form.|
|[TextEncoding.Utf8](textencoding-utf8.md) | Use to choose the UTF8 binary form.|
|[TextEncoding.Utf16](textencoding-utf16.md) | Use to choose the UTF16 little endian binary form.|
|[TextEncoding.Windows](textencoding-windows.md) | Use to choose the Windows binary form.|
