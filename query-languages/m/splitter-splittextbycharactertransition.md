---
title: "Splitter.SplitTextByCharacterTransition | Microsoft Docs"
ms.date: 11/15/2018
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Splitter.SplitTextByCharacterTransition

## Syntax

<pre>
Splitter.SplitTextByCharacterTransition(<b>before</b> as anynonnull, <b>after</b> as anynonnull) as function
</pre>

## About

Returns a function that splits text into a list of text according to a transition from one kind of character to another. The `before` and `after` parameters can either be a list of characters, or a function that takes a character and returns true/false.