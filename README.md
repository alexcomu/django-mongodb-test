# MongoDB & Django TEST

A quick and durty example on how to use Django and MongoDB together.

## Requirements

First of all, create a new **virtualenv** called envDJ inside the root folder

    virtualenv envDJ
    source envDJ/bin/activate
    
Now, install the requirements:

    bash install.sh 
    
Be sure to have MongoDB installed and up&running!

## Test it!

Inside the project you'll find a Django application called **app**. In the **model** file I've declared 3 collections:

    Post: a simple container of title / text / tags / comments list
    Comment: text and author info
    Author: a very simple collection with only a text field
    
To try how it works, connect to django terminal:

    python manage.py shell
    
Now import the models and create post / comment and author.

    from app.models import Post, Comment, Author
    
    # create author
    author = Author.objects.create(name='alexcomu')
    author.save()
    
    # create comment
    comment = Comment.objects.create(author=author, text='Bla Bla Bla!')
    comment.save()
    
    # create post
    post = Post.objects.create(title='Post title', text='Hello world', tags=['mongodb', 'python', 'django'], comments=[comment])
    post.save()

So, we've created a Post with title, text, tags and a list of comments. For each comment we have a text and an author.

Let's try to connect to **MongoDB Shell** from your terminale:

    mongo djangotest
    db.app_post.find().pretty()
    
Here an example of document:

    > db.app_post.find().pretty()
    {
        "_id" : ObjectId("5847e6539718d49ab2a1ca31"),
        "tags" : [
            "mongodb",
            "python",
            "django"
        ],
        "text" : "Hello world",
        "title" : "Post title",
        "comments" : [
            {
                "text" : "Bla Bla Bla!",
                "created_on" : ISODate("2016-12-07T10:36:01.410Z"),
                "id" : ObjectId("5847e6119718d49ab2a1ca30"),
                "author" : {
                    "name" : "alexcomu",
                    "id" : ObjectId("5847e5eb9718d49ab2a1ca2f")
                }
            }
        ],
        "created_on" : ISODate("2016-12-07T10:37:07.553Z")
    }

## On-Line Documentation

[HERE](http://django-mongodb-engine.readthedocs.io/en/latest/index.html) you can see the complete documentation for the Django non-relational project.

