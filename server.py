from bottle import request, run, get, post
import classify_image as CIMG

@get("/")
def index():
    return '''
        <form action="/classify" method="post">
            Image url: <input name="image_url" type="text" />
            <input value="Classify" type="submit" />
        </form>
    '''

@post("/classify")
def hello():
    image_url = request.forms.get('image_url')
    returnStr = ""
    for i in CIMG.classify_image(image_url):
        returnStr += i + "<br />"
    return returnStr + "<br />" + "<img src=" + image_url + ">"

run(host='0.0.0.0', port=8080, debug=True)
