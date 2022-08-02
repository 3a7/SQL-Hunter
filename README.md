# SQL Hunter 
SQL Hunter v1 is a URL SQL injection checker for multiple pages at once!

<h2> The program is suitable for all different OS</h2>

> On Linux distribution, Windows 10 and 11, Android (Termux App on any app that runs python files) and IPhone (Pythonista)

![2022-08-02 15_21_32-Window](https://user-images.githubusercontent.com/58238467/182385361-f9326062-0ded-4bd9-9b23-a4905b5b4f7c.png)

![2022-08-02 15_25_54-Window](https://user-images.githubusercontent.com/58238467/182386333-bbb86799-f8a7-4115-8759-4e0bf304e753.png)

![photo_2022-08-02_15-40-38](https://user-images.githubusercontent.com/58238467/182389347-69c5795f-566b-4c58-83d8-e1bd3da047c2.jpg)

<h2> How the program works</h2>

**The program has two modes:**


- `Check pages' vulnerability` (Check if the page gets an error if you try and change the SQL query in the URL)
- `Check pages' existence`     (Check if the page is alive 'exists' on the internet)


## Start the program
1. Clone the repository using `git clone` or copy the code if you prefer
2. Download the wanted libraries in the `requirements.txt`
3. Open the terminal or the command prompt and navigate to the folder you downloaded the repo
4. Make sure you have python 3 installed and run this command `python "SQL Hunter v1.py"`
> It's better to NOT use proxies if you don't have paid ones. The program works perfectly without proxies.

> NOTE: You can get pages for a specific domain using other programs like [GAU](https://github.com/lc/gau) or [Hakrawler](https://github.com/hakluke/hakrawler) and when you find an injectable page it's recommended to use sqlmap to enumerate and dump the database

<h3> Check pages' vulnerability </h3>
In this mode the program simply adds an apostrophe (') in the end of the URL and checks if the page responses with an error or not. If the page responses with an error then the program sends another request to the original page without the apostrophe, if there's no error in the page the program counts the page as vulnerable.
<br>
<br>
<h3> Check pages' existence </h3>
In this mode the program sends a single request to the URL and if the status code was 200 it counts it as it exists.
<br>


