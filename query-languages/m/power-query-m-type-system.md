---
title: "Power Query M type system | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---

# Types in the Power Query M formula language

The Power Query M Formula Language is a useful and expressive data mashup language. But it does have some limitations. For example, there is no strong enforcement of the type system. In some cases, a more rigorous validation is needed. Fortunately, M provides a built-in library with support for types to make stronger validation feasible.

Developers should have a thorough understanding of the type system in-order to do this with any generality. And, while the Power Query M language specification explains the type system well, it does leave a few surprises. For example, validation of function instances requires a way to compare types for compatibility.

By exploring the M type system more carefully, many of these issues can be clarified, and developers will be empowered to craft the solutions they need.

Knowledge of predicate calculus and na&#239;ve set theory should be adequate to understand the notation used.
 
## PRELIMINARIES

(1) B  := { true; false }<br/>
B is the typical set of Boolean values

(2) N  := { valid M identifiers }<br/>
N is the set of all valid names in M. This is defined elsewhere.

(3) P  := &#10216;B,T&#10217;<br/>
P is the set of function parameters. Each one is possibly optional, and has a type. Parameter names are irrelevant.

(4) P<sup>n</sup>  := &#8899; <sub><sub>0&#8804;i&#8804;n</sub></sub>  &#10216;_i_&#10217;, P<sup>i</sup><br/>
Pn is the set of all ordered sequences of n function parameters.

(5) P<sup>\*</sup> := &#8899;  <sub><sub>0&#8804;i&#8804;&#8734;</sub></sub>  P<sup>i</sup><br/> 	 	 	 
P* is the set of all possible sequences of function parameters, from length 0 on up.

(6) F  := &#10216;B, N, T&#10217;<br/>
F is the set of all record fields. Each field is possibly optional, has a name, and a type.

(7) F<sup>n</sup>  :=<font size="5">&#8719;</font><sub>0&#8804;i&#8804;<sub>n</sub></sub> F<br/>
Fn is the set of all sets of n record fields.

(8) F<sup>\*</sup> :=<font size="5">( &#8899;</font> <sub><sub>0&#8804;i&#8804;&#8734;</sub></sub> <font size="5">F<sup><em>i</em></sup> )</font> &#8726; { <em>F</em> | &#10216; <em>b</em><sub>1</sub>, <em>n</em><sub>1</sub>, <em>t</em><sub>1</sub> &#10217;, &#10216; <em>b</em><sub>2</sub>, <em>n</em><sub>2</sub>, <em>t</em><sub>2</sub> &#10217; &#8712; <em>F</em> &#8896; <em>n</em><sub>1</sub> = <em>n</em><sub>2</sub><br/>
F is the set of all sets (of any length) of record fields, except for the sets where more than one field has the same name.
 
(9) C  := &#10216;N,T&#10217;<br/>
C is the set of column types, for tables. Each column has a name and a type.

(10) C<sup>n</sup>  &#8834; <font size="5">&#8899;</font> <font size="3"><sub><sub>0&#8804;i&#8804;&#8734;</sub></sub></font> &#10216;<em>i</em>, C&#10217;<br/>
C<sup>n</sup> is the set of all ordered sequences of n column types.
 
(11) C<sup>\*</sup> :=<font size="5">( &#8899;</font> <font size="3"><sub><sub>0&#8804;i&#8804;&#8734;</sub></sub></font> <font size="5">C<sup><em>i</em></sup> )</font> &#8726; { <em>C<sup>m</sup></em> | &#10216; <em>a</em>, &#10216; <em>n</em><sub>1</sub>, <em>t</em><sub>1</sub> &#10217;&#10217;, &#10216; <em>b</em> &#10216; <em>n</em><sub>2</sub>, <em>t</em><sub>2</sub> &#10217;&#10217; &#8712; <em>C<sup>m</sup></em> &#8896; <em>n</em><sub>1</sub> = <em>n</em><sub>2</sub> }<br/>
C<sup>\*</sup> is the set of all combinations (of any length) of column types, except for those where more than one column has the same name.

## M TYPES

(12) T<sub>F</sub> := &#10216;P, P&#10217;<br/>
A Function Type consists of a return type, and an ordered list of zero-or-more function parameters.

(13) T<sub>L</sub> :=&#12310;T&#12311;<br/>
A List type is indicated by a given type (called the "item type") wrapped in curly braces.

Since curly braces are used in the metalanguage, &#12310; &#12311; brackets are used in this document.

(14) T<sub>R</sub> := &#10216;<em>B</em>, <em>F</em><sup>\*</sup>&#10217;<br/>
A Record Type has a flag indicating whether it's "open", and zero-or-more unordered record fields. 

(15) <em>T<sub>R<sup>o</sup></sub></em>:= &#10216;<em>true, F</em>&#10217;  

(16) <em>T<sub>R<sup>&#x2022;</sup></sub></em> := &#10216;<em>false, F</em>&#10217;<br/>
<em>T<sub>R<sup>o</sup></sub></em> and <em>T<sub>R<sup>&#x2022;</sup></sub></em> are notational shortcuts for open and closed record types, respectively.

(17) T<sub>T</sub> := <em>C</em><sup>\*</sup><br/>
A Table Type is an ordered sequence of zero-or-more column types, where there are no name collisions.

(18) T<sub>P</sub> := { any; none; null; logical; number; time; date; datetime; datetimezone;  duration; text; binary; type; list; record; table; function; anynonnull  }<br/>
A Primitive Type is one from this list of M keywords.

(19) T<sub>N</sub> := `{`<em>t<sub>n</sub></em>,u &#8712; `T |` <em>t<sub>n</sub></em>`=u + null } = nullable t`<br/>
Any type can additionally be marked as being nullable, by using the "nullable" keyword. 
 
(20) T := T<sub>F</sub> &#8746; T<sub>L</sub> &#8746; T<sub>R</sub> &#8746; T<sub>T</sub> &#8746; T<sub>P</sub> &#8746; T<sub>N</sub><br/>
The set of all M types is the union of these six sets of types:  
Function Types, List Types, Record Types, Table Types, Primitive Types, and Nullable Types. 

## FUNCTIONS

One function needs to be defined: NonNullable : T &#8592; T<br/>
This function takes a type, and returns a type that is equivalent except it does not conform with the null value.

## IDENTITIES

Some identities are needed to define some special cases, and may also help elucidate the above.

(21) nullable any = any<br/>
(22) nullable anynonnull = any<br/>
(23) nullable null = null<br/>
(24) nullable none = null<br/>
(25) nullable nullable <em>t</em>&#8712; T = nullable <em>t</em><br/>
(26) <em>NonNullable</em>(nullable <em>t</em>&#8712; T) = <em>NonNullable</em>(<em>t</em>)</br>
(27) <em>NonNullable</em><sup>(any)</sup> = anynonnull<br/>
 
## TYPE COMPATIBILITY

As defined elsewhere, an M type is compatable with another M type if and only if all values that conform to the first type also conform to the second type.

Here is defined a compatability relation that does not depend on conforming values, and is based on the properties of the types themselves. It is anticiplated that this relation, as defined in this document, is completely equivalent to the original semantic definition.

The "is compatible with" relation : &#8804; : B &#8592; T &#215; T<br/> 
In the below section, a lowercase t will always represent an M Type, an element of T. 

A &#934; will represent a subset of <em>F</em><sup>\*</sup>, or of <em>C</em><sup>\*</sup>.

(28) <em>t</em> &#8804; t<br/>
This relation is reflexive.

(29) <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em> &#8743; <em>t<sub>b</sub></em> &#8804; <em>t<sub>c</sub></em> &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>c</sub></em><br/>
This relation is transitive.

(30) none &#8804; <em>t</em> &#8804; any<br/>
M types form a lattice over this relation; none is the bottom, and any is the top.

(31) <em>t<sub>a</sub></em>, <em>t<sub>b</sub></em> &#8712; <em>T<sub>N</sub></em> &#8743; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em> &#8594; <em>NonNullable</em>(<em>t<sub>a</sub></em>) &#8804; <em>NonNullable</em>(<em>t<sub>b</sub></em>)<br/>
If two types are compatible, then the NonNullable equivalents are also compatible.

(32) null &#8804; <em>t</em> &#8712; <em>T<sub>N</sub></em><br/>
The primitive type null is compatible with all nullable types.

(33) <em>t</em> &#8713; <em>T<sub>N</sub></em> &#8804; anynonnull<br/>
All nonnullable types are compatible with anynonnull.

(34) <em>NonNullable</em>(<em>t</em>) &#8804; <em>t</em><br/>
A NonNullible type is compatible with the nullable equivalent.

(35) <em>t</em> &#8712; <em>T<sub>F</sub></em> &#8594; <em>t</em> &#8804; function<br/>
All function types are compatible with function.

(36) <em>t</em> &#8712; <em>T<sub>L</sub></em> &#8594; <em>t</em> &#8804; list<br/>
All list types are compatible with list.

(37) <em>t</em> &#8712; <em>T<sub>R</sub></em> &#8594; <em>t</em> &#8804;  record<br/>
All record types are compatible with record.

(38) <em>t</em> &#8712; <em>T<sub>T</sub></em> &#8594; <em>t</em> &#8804; table<br/>
All table types are compatible with table.

(39) <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em> &#8596; &#12310;<em>t<sub>a</sub></em>&#12311; &#8804; &#12310;<em>t<sub>b</sub></em>&#12311;<br/>
A list type is compaible with another list type if the item types are compatible, and vice-versa.

(40) <em>t<sub>a</sub></em> &#8712; <em>T<sub>F</sub></em> = &#10216; <em>p<sub>a</sub></em>, <em>p<sup>\*</sup></em> &#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>F</sub></em> = &#10216; <em>p<sub>b</sub></em>, <em>p<sup>\*</sup></em> &#10217; &#8743; <em>p<sub>a</sub></em> &#8804; <em>p<sub>b</sub></em> &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
A function type is compatible with another function type if the return types are compatible, and the parameter lists are identical.
 
(41) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em>, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R<sup>&#x2022;</sup></sub></em> &#8594; <em>t<sub>a</sub></em> &#8816; <em>t<sub>b</sub></em><br/>
An open record type is never compatible with a closed record type.
 
 
(42) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R<sup>&#x2022;</sup></sub></em> = &#10216;<em>false</em>, &#934;&#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em> = &#10216;<em>true</em>, &#934;&#10217; &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
A closed record type is compatible with an otherwise identical open record type.

(43) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em> = &#10216;<em>true</em>, (&#934;, &#10216;<em>true</em>, <em>n</em>, <em>any</em>&#10217;)&#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em> = &#10216;<em>true</em>, &#934;&#10217;  &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em> &#8743; <em>t<sub>b</sub></em> &#8804; <em>t<sub>a</sub></em><br/>
An optional field with the type any may be ignored when comparing two open record types.

(44) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>&#946;</em>, <em>n</em>, <em>u<sub>a</sub></em>&#10217;)&#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, &#934;, &#10216;<em>&#946;</em>, <em>n</em>, <em>u<sub>b</sub></em>&#10217;)&#10217; &#8743; <em>u<sub>a</sub></em> &#8804; <em>u<sub>b</sub></em> &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
Two record types that differ only by one field are compatible if the name and optionality of the field are identical, and the types of said field are compatible.

(45) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>false</em>, <em>n</em>, <em>u</em>&#10217;)&#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>true</em>, <em>n</em>, <em>u</em>&#10217;)&#10217; &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
A record type with a non-optional field is compatible with a record type identical but for that field being optional.

(46) <em>t<sub>a</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em> = &#10216;<em>true</em>, (&#934;, &#10216;<em>b</em>, <em>n</em>, <em>u</em>&#10217;)&#10217;, <em>t<sub>b</sub></em> &#8712; <em>T<sub>R<sup>o</sup></sub></em> = &#10216;<em>true</em>, &#934;&#10217;  &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
An open record type is compatible with another open record type with one fewer field.
 
(47) <em>t<sub>a</sub></em> &#8712; <em>T<sub>T</sub></em> = (&#934;, &#10216;<em>i</em>, &#10216;<em>n</em>, <em>u<sub>a</sub></em>&#10217;&#10217;), <em>t<sub>b</sub></em> &#8712; <em>T<sub>T</sub></em> = (&#934;, &#10216;<em>i</em>, &#10216;<em>n</em>, <em>u<sub>b</sub></em>&#10217;&#10217;) &#8743; <em>u<sub>a</sub></em> &#8804; <em>u<sub>b</sub></em> &#8594; <em>t<sub>a</sub></em> &#8804; <em>t<sub>b</sub></em><br/>
A table type is compatible with a second table type, which is identical but for one column having a differing type, when the types for that column are compatible.

## REFERENCES

Microsoft Corporation (2015 August)<br/>
Microsoft Power Query for Excel Formula Language Specification [PDF]<br/>
Retrieved from https://msdn.microsoft.com/library/mt807488.aspx

Microsoft Corporation (n.d.)<br/>
Power Query M function reference [web page]<br/>
Retrieved from https://msdn.microsoft.com/library/mt779182.aspx


