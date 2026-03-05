---
description: "Learn more about: Lines.ToBinary"
title: "Lines.ToBinary"
ms.subservice: m-source
ms.topic: reference
---
# Lines.ToBinary

## Syntax

<pre>
Lines.ToBinary(
    <b>lines</b> as list,
    optional <b>lineSeparator</b> as nullable text,
    optional <b>encoding</b> as nullable number,
    optional <b>includeByteOrderMark</b> as nullable logical
) as binary
</pre>

## About

Converts a list of text into a binary value using the specified encoding and lineSeparator.The specified lineSeparator is appended to each line. If not specified then the carriage return and line feed characters are used.
