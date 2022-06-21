---
description: "Learn more about: Splitter.SplitTextByCharacterTransition"
title: "Splitter.SplitTextByCharacterTransition | Microsoft Docs"
ms.date: 3/16/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Splitter.SplitTextByCharacterTransition

## Syntax

<pre>
Splitter.SplitTextByCharacterTransition(<b>before</b> as anynonnull, <b>after</b> as anynonnull) as function
</pre>

## About

Returns a function that splits text into a list of text according to a transition from one kind of character to another. The `before` and `after` parameters can either be a list of characters, or a function that takes a character and returns true/false.

## Example 1

Split the input whenever an upper or lowercase letter is followed by a digit.

**Usage**

```powerquery-m
Splitter.SplitTextByCharacterTransition({"A".."Z", "a".."z"}, {"0".."9"})("Abc123")
```

**Output**

`{"Abc", "123"}`
