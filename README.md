<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://media.istockphoto.com/id/1250715834/vector/oil-barrel-icon-design-vector-template.jpg?s=612x612&w=0&k=20&c=W6t5ZWRbqaNOwkAojPz7fR1NQIxsoQgW9VuD0-6cx5M=" alt="Oil Barrell Image" width="80" height="80">
  </a>

  <h3 align="center">Oil Conversion</h3>
  <h6 align="center">Class: CST205<br> Team: <br>Colin Steele<br>Carlos Guizar<br>Sergio Zavala<br>Riley Claunch<br>Darius Cuevas</h6>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Petrodollars are U.S. dollars paid to an oil-exporting country and they are the source of revenue when selling oil. 
Our project aims to help make the process of purchasing oil less steps for consumers that use a different currency by providing the most recent price of oil and letting the user choose a currency of their choice for the current price to be converted into.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.com]][Python-url]
* ![HTML.com][HTML]
* ![JS][JavaScript]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

### Installation

1. Get a free API Key at [https://www.eia.gov/opendata/register.php](https://www.eia.gov/opendata/register.php) [Oil API]
2. Install requests
   ```sh
   pip install requests
   ```
4. Install the converter
   ```sh
   pip install forex-python
   ```
5. Install Pyside6
   ```sh
   pip install PySide6
   ```
6. Install Flask
   ```sh
   pip install Flask
   ```
7. Install Bootstrap
   ```sh
   pip install Flask-Bootstrap
   ```
8. Install Pillow
   ```sh
   pip install pillow
   ```
9. Install numpy
    ```sh
    pip install numpy
    ```
10. Clone the repo
   ```sh
   git clone https://github.com/Barl0s4/CST205-Final-Project.git
   ```
11. Enter your API in `FinalWebsite.py`
   ```js
   api_key = 'Enter API Key'
   ```
12. For bootstrap to work, create a file in your repository called "templates" and store index.html inside.
13. Create a folder called "static", a folder called "images" inside that, and store the USA image inside that folder.
<img width="478" alt="example" src="https://github.com/sezavala/CST205-Final-Project/assets/106635253/d85afe43-ac28-4ca1-914b-f801d8ab283f">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
<p>When using the website, you are provided with the current oil price, a graph of how the price has fluctuated throughout the years, and our currency converter.</p>
<img width="1511" alt="Untitled" src="https://github.com/Barl0s4/CST205-Final-Project/assets/106635253/9103d27c-38e5-47a5-a5f5-5a6729f3acad">
<p>To use the converter, you would just have to select any of the available currencies and click the button to display the converted the displayed price of oil.</p>
<img width="1512" alt="iother" src="https://github.com/Barl0s4/CST205-Final-Project/assets/106635253/996c3880-ca0e-411f-b510-9421b8658c8a">
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[HTML]: https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white
[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
