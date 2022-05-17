# Fibonacci Rabbits

> Everyone loves rabbits!
> 
> http://46.101.107.117:2201
> 
> Note: The service is restarted every hour at x:00.

Visiting this site shows multiple rabbits. The HTML is empty of scripts:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fibonacci Rabbits</title>
    <link rel="stylesheet" href="style.css" />
    <script>
        if (document.location.search.match(/type=embed/gi)) {
            window.parent.postMessage("resize", "*");
        }
    </script>
</head>
<body translate="no">
    <h1>Fibonacci Rabbits</h1>
    <div id="gallery">
        <div><img src="images/rabbit-17711.jpg" /><a href="#">Petal</a></div>
        <div><img src="images/rabbit-75025.jpg" /><a href="#">Harley</a></div>
        <div><img src="images/rabbit-34.jpg" /><a href="#">Rosie</a></div>
        <div><img src="images/rabbit-987.jpg" /><a href="#">Petunia</a></div>
        <div><img src="images/rabbit-8.jpg" /><a href="#">Mortimer</a></div>
        <div><img src="images/rabbit-1.jpg" /><a href="#">Henry</a></div>
        <div><img src="images/rabbit-144.jpg" /><a href="#">Miffy</a></div>
        <div><img src="images/rabbit-2584.jpg" /><a href="#">E.B.</a></div>
        <div><img src="images/rabbit-89.jpg" /><a href="#">Baxter</a></div>
        <div><img src="images/rabbit-55.jpg" /><a href="#">Archie</a></div>
        <div><img src="images/rabbit-5.jpg" /><a href="#">Murphy</a></div>
        <div><img src="images/rabbit-317811.jpg" /><a href="#">Doc</a></div>
        <div><img src="images/rabbit-2.jpg" /><a href="#">Hopper</a></div>
        <div><img src="images/rabbit-6765.jpg" /><a href="#">Fluffy</a></div>
        <div><img src="images/rabbit-46368.jpg" /><a href="#">Daffodil</a></div>
        <div><img src="images/rabbit-28657.jpg" /><a href="#">Buttons</a></div>
        <div><img src="images/rabbit-233.jpg" /><a href="#">Freddie</a></div>
        <div><img src="images/rabbit-1597.jpg" /><a href="#">Roger</a></div>
        <div><img src="images/rabbit-514229.jpg" /><a href="#">Bucky</a></div>
        <div><img src="images/rabbit-4181.jpg" /><a href="#">Oliver</a></div>
        <div><img src="images/rabbit-13.jpg" /><a href="#">Olive</a></div>
        <div><img src="images/rabbit-3.jpg" /><a href="#">Bugs</a></div>
        <div><img src="images/rabbit-377.jpg" /><a href="#">Flower</a></div>
        <div><img src="images/rabbit-10946.jpg" /><a href="#">Chester</a></div>
        <div><img src="images/rabbit-610.jpg" /><a href="#">Bubbles</a></div>
        <div><img src="images/rabbit-121393.jpg" /><a href="#">Coco</a></div>
        <div><img src="images/rabbit-21.jpg" /><a href="#">Clover</a></div>
    </div>
</body>
</html>
```

Judging from the title of the level, and the file names, we are looking for
something related to Fibonacci numbers. Pasting the URLs into a text editor and
checking them against the Fibonacci series reveals that one entry is missing.
Visiting that image (in this case rabbit-196418.jpg) gives us the flag:

![6_rabbit-196418.jpg](img/6_rabbit-196418.jpg)

`he2022{th1z_41nT_4_r4bB1T!}`

