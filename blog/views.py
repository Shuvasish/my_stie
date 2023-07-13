from datetime import date

from django.shortcuts import render

# database

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Shuvo',
        'date': date(2022, 6, 13),
        'title': 'Mountain Hiking',
        'excert': 'There\'s nothing like views. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi asperiores quisquam nisi ratione, harum non corporis delectus minus, dicta consequuntur accusamus, odit ex in quod!',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.
                    
'''
    },
    {
        'slug': 'bike-is-life',
        'image': 'woods.jpg',
        'author': 'Shuvo',
        'date': date(2023, 6, 13),
        'title': 'Bike a fun thning for me',
        'excert': 'There\'s nothing like views. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi asperiores quisquam nisi ratione, harum non corporis delectus minus, dicta consequuntur accusamus, odit ex in quod!',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.
                    
'''
    },
    {
        'slug': 'coding-make-me-keep-dreaming',
        'image': 'coding.jpg',
        'author': 'Shuvo',
        'date': date(2023, 1, 13),
        'title': 'Coding can help you to dream',
        'excert': 'There\'s nothing like views. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sequi asperiores quisquam nisi ratione, harum non corporis delectus minus, dicta consequuntur accusamus, odit ex in quod!',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis alias asperiores laborum sit. Dolores assumenda non, ab error ex veritatis accusamus quam. Autem esse amet debitis quas aliquam molestiae! Dolor.
                    
'''
    },
]

# helper functions

def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    return render(request, 'blog/index.html',{
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_details(request, slug):
    return render(request, 'blog/post-details.html')
