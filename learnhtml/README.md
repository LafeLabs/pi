## [../](../)

#  HTML

 [codeserver/](codeserver/)

 [codeserver/code/index.html](codeserver/code/index.html)

## Goals

1. learn to use code server to make a local web
2. fork code servers to make more webs, build whole internal web on one server
2. Learn to make a self-replicating web pages and propagate them on the open web
3. Learn the basic elements of HTML, how they are used, how to copy/paste them to make HTML do what you want
4. learn how HTML files are put together, how to read them
5. learn how standard HTML files are made with Geometron
6. learn to make and use your own favicons
7. use unicode to put in emoji and other non standard characters, find the unicode you want
8. learn where to learn more, use online reference materials effectively
9. put up web pages on a paid domain, a free hosting service, on github.io, and over local network

## Elements

1. link
2. header
3. paragraph, div, span
5. break(BR)
6. unicode
4. style
5. script
6. img
7. input
8. textarea
9. form
9. ul, li, ol
10. pre
11. table, tr, td
12. canvas, svg
13. head
14. body
15. meta
16. link
17. html
18. doctype

## Code

```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
      <h1>biggest heading size</h1>
      <h2>next biggest heading size</h2>
      <a href = "../../">a stands for "anchor" which means hyperlink</a>
      <div>division, just a box with no specific properties, displayed "block" by default</div>
      <span>like a "div", but inline(no newline)</span>
      <img src = "../iconsymbols/chaos.svg" alt "alt text describes image"/>
<ul>
    <li>un-ordered list item 1</li>
    <li>un-ordered list item 2</li>
</ul>      
<ol>
    <li>ordered list item 1</li>
    <li>ordered list item 2</li>
</ol>      
<pre>
    //here we put code-looking things 
    void loop(){
      supid.c.derived.language();
      break;
    }
</pre>
<br>
break with br manually
<p>
    paragraph is p.  somewhat anachronistic.
</p>
<textarea></textarea>
<input/>
<table>
    <tr>
        <td>element11</td>
        <td>element12</td>
    </tr>
    <tr>
        <td>element21</td>
        <td>element22</td>
    </tr>
</table>

<h4>hexidecimal value of UNICODE, ACE OF SPADES:</h4>
<span style  = "font-size:4em">&#x2660;A</span>
<span style  = "font-size:4em;transform:rotate(180deg);position:absolute">&#x2660;A</span>

<h4>base 10 smiling poop emoji UNICODE:</h4>
<span style = "font-size:4em">&#128169;</span>
    <script>
     //javascript goes in scripts
     console.log("print this on console, you can see using developer mode on your browser");
    </script>
      <style>
      /*
      "style" contains CSS code to decide how things look
      this turns links(anchors) a color
      */
          a{
              color:purple;
          }
          td,tr,table{
              border:solid;
          }
      </style>
  </body>
</html>
```
