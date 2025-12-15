from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title='My Home Page')

@app.route('/about')
def about():
    title='About Page'
    name='Sirawit Suwakai'
    email='zxzxdua@gmail.com'
    phone='0981546575'
    return render_template('about.html',title=title,name=name,email=email,phone=phone)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods Page'
    foods = ['ผัดผัก','กะเพราหมูกรอบ','ไก่ย่าง','ไข่เจียวหมูสับ','หมูทอดกระเทียมพริกไทย','ผัดเปรี้ยวหวาน']
    return render_template('fav_foods.html',title=title,foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title = 'Favorite Sports Page'
    sports = ['เปตอง','ปิงปอง','ฟุตบอล']
    return render_template('fav_sports.html',title=title,sports=sports)

@app.route('/greeting/<username>')
def greeting(username):
    title = 'Welcome Page'
    return render_template('welcome.html',title=title,username=username)

@app.route('/favorite/movies')
def favorite_movies():
    title = 'Favorite Movies Page'
    movies = ['13 ชม. ทหารลับแห่งเบนกาซี','ยุทธการดับจอมอหังการ์อินทรีเหล็ก','พยัคฆ์ร้าย ศูนย์ ศูนย์ ก๊าก สายลับกลับมาป่วน','วีรบุรุษสมรภูมิปาฏิหาริย์','วันปฐพีเดือด']
    return render_template('fav_movies.html',title=title,movies=movies)