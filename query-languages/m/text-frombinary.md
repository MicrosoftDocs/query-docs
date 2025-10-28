---
description: "Learn more about: Text.FromBinary"
title: "Text.FromBinary"
ms.subservice: m-source
---
# Text.FromBinary

## Syntax

<pre>
Text.FromBinary(<b>binary</b> as nullable binary, optional <b>encoding</b> as nullable number) as nullable text
</pre>

## About

Decodes data from a binary value to a text value using the specified encoding type.

* `binary`: The binary data to be decoded.
* `encoding`: (Optional) The encoding used to convert the binary to text. Use [BinaryEncoding.Type](binaryencoding-type.md) to specify the type of encoding. If this value isn't specified, the default value is `BinaryEncoding.Utf8`.

## Example 1

Encode text to binary, produce a viewable Base64 string, then decode it back to text.

**Usage**

```powerquery-m
let
    originalText = "Testing 1-2-3",

    // Default UTF-8 binary
    binaryData = Text.ToBinary(originalText),

    // Convert binary to viewable Base64 string
    encodedText = Binary.ToText(binaryData, BinaryEncoding.Base64),

    // Decode back to text
    decodedText = Text.FromBinary(binaryData),

    result = [
        OriginalText = originalText,
        BinaryBase64 = encodedText,
        DecodedText = decodedText
    ]
in
    result
```

**Output**

```powerquery-m
[
    OriginalText = "Testing 1-2-3",
    BinaryEncoded = "VGVzdGluZyAxLTItMw==",
    DecodedText = "Testing 1-2-3"
]
```

## Example 2

Encode text to binary with a Byte Order Mark (BOM), produce a viewable hexadecimal string, then decode it back to text.

**Usage**


```powerquery-m
let
    originalText = "Testing 1-2-3",

    // Convert to binary with BOM
    binaryData = Text.ToBinary(originalText, TextEncoding.Utf16, true),

    // Show binary as hex to demonstrate presence of BOM (fffe)
    binaryAsHex = Binary.ToText(binaryData, BinaryEncoding.Hex),

    // Decode back to text
    decodedText = Text.FromBinary(binaryData, TextEncoding.Utf16),

    // Compare original text and decoded text
    isIdentical = originalText = decodedText,

    result = [
        OriginalText = originalText,
        BinaryHex = binaryAsHex,
        DecodedText = decodedText,
        IsIdentical = isIdentical
    ]
in
    result
```

**Output**

```powerquery-m
[
    OriginalText = "Testing 1-2-3", 
    DecodedText = "fffe540065007300740069006e006700200031002d0032002d003300",
    DecodedText = "Testing 1-2-3", 
    IsIdentical = true
]
```
