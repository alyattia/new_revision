from flask import Flask, render_template, request, redirect
# to make python work as javascript document
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# you have to define you app at first
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("homepage.html", pagetitle="home")

@app.route("/ali")
def ali_page():
  return "this is the ali page"

# checks if this page is running directly not imported
# if __name__ == "__main__":
#   app.run(debug=True, port=8000)


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://moodle.jku.at/jku/my/courses.php")

# will search in the search box in elzero home page for "front-end development"
# browser.find_element_by_css_selector(".search-field").send_keys("front-end development")
# browser.find_element_by_css_selector(".search-submit").click()