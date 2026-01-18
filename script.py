#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS 
from urllib.parse import urljoin

url = "https://www.learncpp.com/cpp-tutorial/introduction-to-these-tutorials/"
start_url = url

articles = []

page_counter = 1

while True:

        print(f"Scraping: {start_url}")

        html = requests.get(start_url).text

        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find("article")      # extract only the article section of webpage
        
        if not article:
            break

        articles.append(str(article))

        next_link = soup.select_one("div.prevnext-inline a.nav-link:has(.nav-button-next)") # move to next webpage 

        if not next_link:
            break

        href = next_link.get("href")

        if href == "#" or href is None: # if next-page href is '#', it means we have reached the end of learncpp
            break

        start_url = urljoin(start_url, href)  

#  create a final pdf with some css overriding  and joining all arcticles which we scraped together

final_html = '''<html><body><head>
<meta charset="utf-8">
<title>LearnCPP Book</title>
</head><body>'''
final_html += "<div style='page-break-after: always'></div>".join(articles)
final_html += "</body></html>"

# HTML(string=final_html, base_url=url).write_pdf("output.pdf")   #pdf without css overriding(looks ugly :\)
HTML(string=final_html, base_url=url).write_pdf("learncpp.pdf", stylesheets=[
CSS(string="""
        @page {
            @bottom-right {
                content: counter(page);
                font-size: 6pt;
                color: #666;
            }
        }

        html, body{
            line-height: 1.4;
            word-spacing: normal;
            font-size: 0.8em;
        }

        /*Code blocks*/

        pre {
            background: #ffffff !important;
            padding: 12px;
            border-radius: 6px;
            border: 1px solid #ddd;
            word-wrap: break-word;
            white-space: pre-wrap;
            word-break: break-word;
        }

        /*Blue table*/

        .cpp-table{
            width: 100%;
            max-width: 100%;
            table-layout: fixed;
            margin-top: 20px, 0;
            padding: 20px;
            border-radius: 6px;
            border: 2px solid #64A6F5 !important;
            box-shadow: 0 2px 0 0 #64A6F5;
            background-color: #edf5ff;
            page-break-inside: avoid;
        }
        
        /*Titles for every topic*/
        .cpp-section{
            font-size : 1.5em;
            font-weight : bold;
        }

        /* Quiz Show Solution and Hide Solution, hints*/

        div.quiz a{
            display: none;
        }

        a:link{
            text-decoration: none;
            pointer-events: none;
        }

        .wpsolution{
            display: block !important;
            visibility : visible !important;
            border-left : 2px solid #39348F;
            padding : 10px;
        }

        /* all images in learncpp */

        .cpp_image_wrapper{
            margin: 10px, 5px; 
            width : 80%;
        }

        img{
            display: block;
            max-width: 100%;
            page-break-inside: avoid;
        }

        /* Warnings, Key Insights, Best practices.....etc */

        .cpp-note{
            border-top: 1px solid #666;
            border-bottom: 1px solid #666;
            margin: 10px 0;
        }

        p.cpp-note-title{
            font-weight: bold;
            font-size : 1em;
            color: #540863;
        }

        /*Things that were messing with pdf formatting, so i js removed them from pdf*/

        div.code-block, .prevnext, .cf_monitor{
            display:none;
        }

    """)
])