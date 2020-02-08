Use framework [selene](https://github.com/yashaka/selene) (python selenium wrapper)

# Precondition

* [Python 3.6+](https://www.python.org/)
* Browser [Chrome](https://www.google.com/chrome/)
* [ChromeDriver](https://chromedriver.chromium.org/)

Chrome is set up as default, but it is possible to change by `--browser` agrument to ie, firefox, safari 

Note: you need to have drivers for the above browsers in `PATH` 


# Installation

Install dependencies `pip3 install -r requirements.txt`

# Start tests

Linux example
```
$ pytest --browser chrome --base_url https://example.com
```

Same for Windows  

# Test Framework Architecture  

Tests have fake locators and test data since it is just an example  

- `locators.py` store page locators  
- `pages.py` store page methods  
- `tests.py` store test cases  
- `conftest.py` store preconditions 
- `data.py` store test data  
- `requirements.txt` store libraries that necessary to install  