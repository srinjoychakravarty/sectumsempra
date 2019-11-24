
![INFO6105 17944 Data Sci Eng Methods SEC 04 Fall 2019 [BOS-2-TR]](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/784d0639-1f78-48f4-9fab-a74b29c0c9a3/dc4k4ur-a33c690e-085b-40e1-92e7-a0260fc32b4d.jpg/v1/fill/w_1024,h_873,q_75,strp/sectumsempra___severus_snape_by_nikunikupro_dc4k4ur-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODczIiwicGF0aCI6IlwvZlwvNzg0ZDA2MzktMWY3OC00OGY0LTlmYWItYTc0YjI5YzBjOWEzXC9kYzRrNHVyLWEzM2M2OTBlLTA4NWItNDBlMS05MmU3LWEwMjYwZmMzMmI0ZC5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.JBalubjAkGwNSGNKbpY8MgxwkdsF_Q_4CptuKYu1oJc)

# Welcome to Sectumsempra! 

Here we navigate the Harry Potter world from a Slytherin perspective! We use the power of **Data Science** to gain insights that have never been uncovered before. Once you have finished with running our code, you will have gained a new appreciation for the noble **House of Salazar Slytherin** and hopefully learnt some Machine Learning along the way.

# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```

